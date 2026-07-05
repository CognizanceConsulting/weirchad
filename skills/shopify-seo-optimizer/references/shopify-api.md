# Shopify Admin API: SEO reads and writes

Exact operations for reading and writing SEO fields. Use the Shopify MCP tools. Prefer the built-in shortcut tools (`get-product`, `update-product`, `get-collection`, `update-collection`, `search_products`, `search_collections`) when they cover the field. Fall back to `graphql_query` and `graphql_mutation` for pages, blogs, articles, metafields, redirects and alt text.

## Contents

1. Where SEO fields actually live
2. Verify before you write
3. Reading (audit pulls)
4. Writing (apply changes)
5. Redirects and handles
6. Pagination and rate limits

## 1. Where SEO fields actually live

This is the part people get wrong. The field location differs by resource.

| Resource | SEO title | SEO meta description | Body copy | Image alt text |
|----------|-----------|----------------------|-----------|----------------|
| Product | `seo.title` | `seo.description` | `descriptionHtml` | media `alt` / image `altText` |
| Collection | `seo.title` | `seo.description` | `descriptionHtml` | image `altText` |
| Page (OnlineStorePage) | `global.title_tag` metafield | `global.description_tag` metafield | `body` | n/a |
| Article (blog) | `global.title_tag` metafield | `global.description_tag` metafield | `body` | image `altText` |

Products and collections have a real `seo` object. Pages and articles do not. Their title tag and meta description live in metafields under the `global` namespace with keys `title_tag` and `description_tag`. Confirmed against the live store: a query for `seo` on `Article` returns "Field 'seo' doesn't exist on type 'Article'".

## 2. Verify before you write

API versions differ between stores and change over time. The exact input shape of a mutation (for example `productUpdate(input:...)` versus `productUpdate(product:...)`) can vary by version. Before running an unfamiliar mutation, confirm its current shape:

- `graphql_schema` with a `type_name` (for example `"Mutation"`) and a `query` term to inspect the field signature.
- `validate_graphql_codeblocks` to check a drafted operation before sending it.
- `search_docs_chunks` to pull the relevant Admin API doc.

When a mutation returns `userErrors`, read them back to the user verbatim and stop. Do not retry blindly.

## 3. Reading (audit pulls)

### Products

```graphql
{
  products(first: 50, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      title
      handle
      descriptionHtml
      seo { title description }
      featuredImage { altText url }
      media(first: 20) {
        nodes { ... on MediaImage { id alt image { url altText } } }
      }
      onlineStoreUrl
    }
  }
}
```

### Collections

```graphql
{
  collections(first: 50, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      title
      handle
      descriptionHtml
      seo { title description }
      image { altText url }
      productsCount { count }
    }
  }
}
```

### Pages

```graphql
{
  pages(first: 50, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      title
      handle
      body
      titleTag: metafield(namespace: "global", key: "title_tag") { value }
      descTag: metafield(namespace: "global", key: "description_tag") { value }
    }
  }
}
```

### Blogs and articles

```graphql
{
  blogs(first: 10) {
    nodes {
      id
      title
      handle
      articles(first: 50, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          title
          handle
          summary
          body
          image { altText url }
          titleTag: metafield(namespace: "global", key: "title_tag") { value }
          descTag: metafield(namespace: "global", key: "description_tag") { value }
        }
      }
    }
  }
}
```

## 4. Writing (apply changes)

Only run these after the before/after table is approved. Every mutation below requests `userErrors`. Always read that array.

### Product: title, body and SEO

```graphql
mutation {
  productUpdate(input: {
    id: "gid://shopify/Product/123",
    title: "Poet Powder Skis for Deep Snow",
    descriptionHtml: "<p>...</p>",
    seo: { title: "Poet Powder Skis for Deep Snow | Poet", description: "Float through deep snow. Hand built in Canada." }
  }) {
    product { id title seo { title description } }
    userErrors { field message }
  }
}
```

Note: on some API versions the argument is `product:` instead of `input:`. Confirm with `graphql_schema` if `input` is rejected.

### Product image alt text

Alt text sits on the media object, not the product input. Update it with `productUpdateMedia`.

```graphql
mutation {
  productUpdateMedia(
    productId: "gid://shopify/Product/123",
    media: [{ id: "gid://shopify/MediaImage/456", alt: "Poet powder skis standing upright in fresh snow" }]
  ) {
    media { ... on MediaImage { id alt } }
    mediaUserErrors { field message }
  }
}
```

`productUpdateMedia` returns `mediaUserErrors`, not `userErrors`. Check the right field.

### Collection: body and SEO

```graphql
mutation {
  collectionUpdate(input: {
    id: "gid://shopify/Collection/123",
    descriptionHtml: "<p>...</p>",
    seo: { title: "Powder Skis | Poet", description: "Shop hand built powder skis..." }
  }) {
    collection { id seo { title description } }
    userErrors { field message }
  }
}
```

### Page: body plus SEO metafields

Page title tag and meta description are metafields. Set them with `metafieldsSet` in the same run as the body update.

```graphql
mutation {
  metafieldsSet(metafields: [
    { ownerId: "gid://shopify/Page/123", namespace: "global", key: "title_tag", type: "single_line_text_field", value: "About Poet | Hand Built Skis" },
    { ownerId: "gid://shopify/Page/123", namespace: "global", key: "description_tag", type: "single_line_text_field", value: "Poet builds skis by hand in Canada..." }
  ]) {
    metafields { id key value }
    userErrors { field message }
  }
}
```

Update the page body separately with `pageUpdate` if the API version supports it. If `pageUpdate` is unavailable on the store's version, note it and handle body edits in the Shopify admin manually.

### Article: body plus SEO metafields

Same pattern as pages. Set `title_tag` and `description_tag` with `metafieldsSet` using `ownerId` of the article gid. Update body and image alt with `articleUpdate` where supported, otherwise flag for manual edit.

```graphql
mutation {
  metafieldsSet(metafields: [
    { ownerId: "gid://shopify/Article/123", namespace: "global", key: "title_tag", type: "single_line_text_field", value: "..." },
    { ownerId: "gid://shopify/Article/123", namespace: "global", key: "description_tag", type: "single_line_text_field", value: "..." }
  ]) {
    metafields { id key value }
    userErrors { field message }
  }
}
```

## 5. Redirects and handles

Handles are the URL slug. Read them in the pulls above. A clean handle is lowercase, hyphenated, keyword-relevant and free of Shopify's auto-appended suffixes like `-1` or random ids.

Changing a handle breaks the old URL. Always create a redirect from the old path to the new one so link equity and bookmarks survive. Read existing redirects and create new ones:

```graphql
# read
{ urlRedirects(first: 50) { nodes { id path target } } }

# create
mutation {
  urlRedirectCreate(urlRedirect: { path: "/products/old-handle", target: "/products/new-handle" }) {
    urlRedirect { id path target }
    userErrors { field message }
  }
}
```

A redirect chain is when A points to B and B points to C. Check that no new redirect targets a path that is itself redirected. Collapse chains so each old path points straight to the final URL.

## 6. Pagination and rate limits

- Page through everything with `first: 50` and the `endCursor` from `pageInfo`. Do not assume the first page is the whole catalog. Report the total count you pulled.
- The Admin GraphQL API uses a cost-based rate limit. If a query is throttled, reduce `first`, request fewer nested fields, or space calls out. Batch reads where you can. Do not fire hundreds of tiny queries.
- For large catalogs, `search_products` and `search_collections` help you target a subset instead of pulling everything.
