# Technical SEO checks

Workflow 7. Verify the mechanical parts of SEO that sit outside the copy. Some you can read and fix through the API. Some the theme controls and only a human can fix. Separate the two clearly so the user knows what to action.

## What you can check and fix through the API

### URL handles

A clean handle is lowercase, hyphenated, keyword-relevant and free of clutter. Pull handles for every product, collection, page and article (see `references/shopify-api.md`).

Flag handles that are:
- Auto-suffixed. Trailing `-1`, `-2` or random ids from duplicate creation.
- Junk or non-descriptive. Random strings, SKU codes, "untitled".
- Off-keyword. The handle ignores the page's assigned primary keyword.
- Overlong. Very long handles with stop words padding them out.

Changing a handle is a real fix but it breaks the old URL. Never change a handle without creating a redirect from the old path to the new one. Handle changes go through the Workflow 8 write gate like any other change.

### Redirect chains

Pull existing redirects with `urlRedirects` (query in `references/shopify-api.md`). Check for:
- Chains. A points to B, B points to C. Each hop loses a little link equity and slows the page. Collapse so A points straight to C.
- Loops. A points to B, B points back to A. These break the page. Flag immediately.
- Redirects to dead targets. The target path no longer exists.

When you create a new redirect for a handle change, confirm the target is a final URL, not itself a redirected path.

### Structured data basics

Shopify and the theme generate most structured data (Product, Breadcrumb, Organization schema). You cannot fully audit rendered JSON-LD through the Admin API alone. What you can do:
- Confirm the fields that feed structured data are populated: product title, description, images, price, availability, vendor. Rich results need these present and accurate.
- Fetch a live product URL with web fetch and check for a JSON-LD block and Product schema in the HTML. Report what you find. If the theme emits no Product schema, that is a theme-level item for a human.

## What the theme controls (flag for manual fix)

These affect SEO but are not editable through the product and collection API. List them plainly with the specific fix so a human or theme developer can action them.

- **H1 on templates.** The theme usually renders the product or collection title as the page H1. If a template has no H1, two H1s, or an H1 that is not the page subject, that is a theme fix.
- **Title tag templates.** Some themes wrap every title tag in a global template (for example appending the store name). Note it so title tag character budgets account for it.
- **Canonical tags.** Duplicate content across variant URLs or filtered collection URLs is handled by canonical tags the theme emits. Flag suspected duplication for canonical review.
- **Robots and sitemap.** Shopify generates `robots.txt` and `sitemap.xml`. Custom rules live in `robots.txt.liquid` in the theme.
- **Page speed and Core Web Vitals.** Image sizes, app scripts and theme code drive these. Out of API scope. Flag if the user asks.
- **Breadcrumbs and internal nav.** Theme-controlled. Note gaps.
- **Hreflang and markets.** If the store sells across regions, hreflang setup is theme and Markets configuration.

## Output format

Split the report into two blocks so the boundary is obvious. Keep the output rules.

```
## Technical checks for {store}

### Fixable through the API
| Item | Issue | Fix | Needs redirect |
|------|-------|-----|----------------|
| /products/poet-powder-ski-1 | Auto-suffixed handle | Change to /products/poet-powder-ski | Yes |
| Redirect /a to /b to /c | 2-hop chain | Collapse /a straight to /c | n/a |

### Manual, theme-controlled (for a human)
| Item | Issue | Who fixes |
|------|-------|-----------|
| Collection template | No H1 rendered | Theme developer |
| Product schema | No JSON-LD Product block on live page | Theme developer |
```

Fixable items with the store's approval go through Workflow 8. Manual items just get reported. Do not claim to have fixed something the theme controls.
