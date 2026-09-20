# Store SEO audit

Pull the whole store, score every item, output a prioritized fix list. This is Workflow 1.

## Process

1. Confirm store and load SEO.md first (SKILL.md Steps 1 and 2).
2. Pull all products, collections, pages and articles using the queries in `references/shopify-api.md`. Page through every result. Report the real counts. Example: "Pulled 40 products, 8 collections, 5 pages, 12 articles."
3. Score each item against the rubric below.
4. Sort by priority. Output the fix list.

## What to flag

Check each item for these issues. Each maps to a real, fixable field.

**Title tag**
- Missing. No `seo.title` set, so Shopify falls back to the product title plus store name.
- Too long. Over 60 characters gets truncated in search results.
- Too short. Under 30 characters usually wastes the space.
- No target keyword. The page's assigned primary keyword from SEO.md does not appear.
- Duplicate. The same title tag on two or more pages.

**Meta description**
- Missing. Empty `seo.description`. Search engines then scrape random body text.
- Too long. Over 155 characters gets truncated.
- Too short. Under 70 characters usually underuses the space.
- No call to action or keyword. Reads like filler.
- Duplicate. Same meta on multiple pages.

**Image alt text**
- Missing. Empty `altText` or `alt`. Bad for accessibility and image search.
- Filename junk. Values like "IMG_2931.jpg" or "Screenshot_20250826". These are not alt text.
- Keyword stuffed. Same keyword jammed in repeatedly across every image.
- Duplicate across all images. Every image on a product carrying the identical alt string.

**H1 and header structure**
- Body copy where the H1 is missing, duplicated or not the main product or page name. Note: the theme often renders the product title as the H1. You can only inspect headers inside `descriptionHtml` and `body`. Flag multiple H1s or skipped levels (H1 then H3) in the copy you can see. Header issues the theme controls go to `references/technical-checks.md`.

**Duplicate content**
- Two products or collections sharing near-identical descriptions. Common with variant-heavy catalogs and copy-pasted supplier text.
- Boilerplate supplier copy repeated verbatim across many items.

**Thin content**
- Product descriptions under 50 words. Collections with no description. Articles under 300 words. Thin pages rank poorly and convert worse.

## Scoring rubric

Score each item 0 to 100. Start at 100 and subtract. This makes the number mean something concrete.

| Issue | Points off |
|-------|-----------|
| Missing title tag | 20 |
| Title tag over 60 or under 30 chars | 10 |
| Missing meta description | 20 |
| Meta over 155 or under 70 chars | 10 |
| Assigned primary keyword absent from title | 15 |
| Any image missing alt text | 10 |
| Filename-junk alt text | 8 |
| Duplicate title or meta with another page | 15 |
| Thin body copy (product under 50 words) | 15 |
| Duplicate body content with another item | 12 |

Cap total deductions so no item goes below 0. An item at 100 is clean. Report the score with the specific issues, not just the number.

## Priority ordering

Sort the fix list so the highest-impact, lowest-effort work rises to the top.

1. **Priority 1.** Missing title tags and missing meta on the store's highest-traffic or highest-revenue pages. Use `run-analytics-query` to find which products and collections actually get traffic and sales. Fixing a blank meta on a top seller beats fixing a top seller.
2. **Priority 2.** Missing title or meta on everything else. Duplicate title or meta anywhere.
3. **Priority 3.** Length and keyword issues on existing tags. Thin content on important pages.
4. **Priority 4.** Alt text gaps. Header structure inside body copy. Thin content on low-traffic pages.

Use analytics to rank within each tier. Real traffic and revenue numbers decide order, not guesses. If analytics is unavailable, say so and rank by catalog position or collection membership instead.

## Output format

Produce a table plus a short summary. Keep to the output rules: no em dashes, no Oxford commas, short sentences, real numbers.

```
## Audit summary for {store}
Pulled 40 products, 8 collections, 5 pages, 12 articles.
23 items scored below 70. 12 products have empty meta descriptions. 7 title tags exceed 60 characters.

## Prioritized fix list

| Priority | Item | Type | Score | Issues | Suggested action |
|----------|------|------|-------|--------|------------------|
| 1 | Poet Powder Ski | Product | 45 | Empty meta. Title 8 chars. Top seller. | Write title and meta targeting "powder skis" |
| 1 | Powder Skis | Collection | 55 | Empty description. High traffic. | Write 200 word description with 4 product links |
| 2 | Poet Carbon Ski | Product | 60 | Duplicate meta with Poet Powder Ski | Rewrite meta unique to carbon model |
```

After the table, offer to start on Priority 1 with Workflows 2, 3 or 4. Do not start writing until the user picks scope.
