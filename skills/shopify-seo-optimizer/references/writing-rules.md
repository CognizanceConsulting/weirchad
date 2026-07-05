# Writing rules: products, collections and blog

How to rewrite copy for Workflows 2, 3 and 4. Every output here follows the five rules in SKILL.md: no em dashes, no Oxford commas, short sentences, real numbers, never fabricate data.

Before writing anything, read SEO.md for the store. Every page has an assigned primary keyword. Write to it. Never target a primary keyword that another page already owns.

## Preserving brand voice

The store's existing copy is your voice reference. Do not invent a new tone. Before rewriting, read 3 to 5 of the store's current product and collection descriptions and note:

- Sentence rhythm. Punchy or flowing.
- Person. "You" versus "we" versus neutral.
- Vocabulary the brand uses for its products and its customer.
- What it never says. Cross-check the banned terms list in SEO.md.

Poet Snow Sports, Fly Guys and I Think We Missed a Turn are distinct brands with distinct voices. Match the one you are working on. When unsure whether a phrase fits, quote it back to the user and ask.

## Workflow 2: Product page optimization

Rewrite four fields per product. Keep the assigned keywords front and center without stuffing.

**Keyword targeting.** One primary keyword. Two to three secondary keywords. Pull all of them from the product's row in SEO.md. If the product has no assignment yet, propose one, check it does not collide with an existing primary, and add it to SEO.md only after approval.

**Title tag. Under 60 characters.** Lead with the primary keyword where it reads naturally. Add the brand at the end when space allows.
- Pattern: `{Primary keyword} {qualifier} | {Brand}`
- Example: `Powder Skis for Deep Snow | Poet` (32 chars)
- Count the characters. Report the count. If over 60, cut words, not the keyword.

**Meta description. Under 155 characters.** One or two short sentences. Include the primary keyword once. Add a concrete reason to click: a benefit, a proof point or an offer. No hype.
- Example: `Float through deep snow on Poet powder skis. Hand built in Canada. Free shipping over 200 dollars.` (98 chars)
- Count the characters. Report the count.

**Description.** Rewrite the body so it reads for a human first and search second. Structure:
- Opening line states what it is and who it is for, using the primary keyword once.
- Two to four short benefit lines. Weave in secondary keywords where they fit naturally.
- Specifics customers actually want: materials, dimensions, use case, what is included. Real numbers.
- Keep it above 50 words so it is not thin. Do not pad to hit a count.

**Image alt text.** Describe what is in the image for someone who cannot see it. Include the product and a defining detail. Vary alt text across a product's images. Do not repeat the same string on every photo.
- Good: `Poet powder skis standing upright in fresh snow`
- Good: `Base graphic detail on the Poet powder ski`
- Bad: `powder skis powder skis best powder skis` (stuffed)
- Bad: `IMG_2931` (filename junk)

## Workflow 3: Collection page optimization

Write or improve a collection description of 150 to 300 words.

- Open with what the collection is and who it serves, using the collection's assigned primary keyword.
- Explain what unites the products and how to choose between them. This is genuinely useful and it ranks.
- Link to the top products in the collection. Use analytics (`run-analytics-query`) to find the real top sellers, not guesses. Link with descriptive anchor text that reads naturally, for example "the Poet powder ski" not "click here".
- Weave secondary keywords in where they fit. Do not list keywords.
- Also write the collection's title tag (under 60) and meta (under 155) using the product-page rules above.

Internal links use standard relative HTML paths inside `descriptionHtml`:

```html
<p>Our <a href="/products/poet-powder-ski">powder ski</a> floats through deep snow.</p>
```

## Workflow 4: Blog SEO

Two modes: audit existing articles, and produce new work.

### Auditing existing articles

For each article check:
- Title tag and meta description present and within limits (metafields, see `references/shopify-api.md`).
- A clear target keyword and search intent. Does the article answer the question its title implies.
- Header structure. One H1. Logical H2s. Keyword in at least one header where natural.
- Internal links. Every article must link to at least 2 relevant products or collections. This is a hard requirement. Flag any article that does not.
- Word count and depth. Under 300 words is thin. Note it.

Output the same scored, prioritized style as the audit.

### Rewriting an underperforming article

Only on request. Preserve the article's real information and voice. Fix the target keyword focus, headers, meta and internal links. Keep the minimum 2 product or collection links. Show a before/after summary before writing back.

### Generating new article briefs

Build briefs from gaps found in keyword research (Workflow 5). A brief is a plan, not a draft. Each brief contains:

```
## Brief: {working title}
- Target keyword: {primary, from a gap not already owned in SEO.md}
- Search intent: {informational, commercial or transactional, with the evidence}
- Audience: {who searches this and why}
- Suggested title tag: {under 60 chars}
- Suggested meta: {under 155 chars}
- Outline:
  - H1: {main}
  - H2: {section} ...
- Internal link targets: {at least 2 specific products or collections with URLs}
- Word count target: {a real number, for example 900}
```

Every brief names at least 2 specific internal link targets. Propose the target keyword as an SEO.md addition and wait for approval before locking the brief to it.
