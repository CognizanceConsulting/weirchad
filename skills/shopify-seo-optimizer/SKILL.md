---
name: shopify-seo-optimizer
description: Audit and optimize SEO for Shopify stores through the Shopify Admin API MCP connection. Use this whenever the user wants to improve search rankings, run an SEO audit, rewrite product titles or meta descriptions, fix image alt text, optimize collection or blog copy, do keyword research, generate article briefs, check technical SEO, or push SEO fixes to a Shopify store. Works for Poet Snow Sports (poetskis.com), Fly Guys, and I Think We Missed a Turn. Trigger even when the user does not say the word "SEO" but asks to improve product copy, meta tags, alt text, collection descriptions, blog rankings, or store discoverability.
---

# Shopify SEO Optimizer

Audit and optimize search performance for Shopify stores using the Shopify MCP connection. This skill covers a full workflow: pick a store, load its keyword strategy, audit, research, rewrite, then push approved changes back to Shopify.

## The rules that never change

Every piece of customer-facing output this skill produces follows these rules. They are not style suggestions. They protect the brand and keep the copy honest.

- No em dashes ever. Use periods, commas or parentheses instead.
- No Oxford commas. Write "titles, meta and alt text" not "titles, meta, and alt text".
- Short sentences. One idea per sentence.
- Real numbers over vague language. Write "62 characters" not "a bit long". Write "12 of 40 products" not "many products".
- Never fabricate search volume or ranking data. If you do not have an exact number from a tool or source, say so plainly and use relative terms with a named source. Example: "Google autocomplete suggests 'powder skis' before 'all mountain skis', which points to higher relative demand." Do not invent monthly search volumes.

These apply to titles, meta descriptions, product and collection copy, blog articles, alt text and briefs. They do not need to constrain your own conversational messages to the user.

## Operating guardrails

Two hard gates protect the live store. Do not skip them.

1. **Confirm the store at the start of every run.** Never assume. Ask which store to target, then confirm the MCP is pointed at it before reading anything. See "Step 1".
2. **Confirm write access before any change.** Reading is safe. Writing is not. Always show a before/after table and get explicit confirmation before pushing to Shopify. See "Workflow 8".

## Stores

| Store | Domain | Notes |
|-------|--------|-------|
| Poet Snow Sports | poetskis.com | Primary store |
| Fly Guys | (confirm domain on connect) | Use when connected |
| I Think We Missed a Turn | ithinkwemissedaturn.com | Use when connected |

Store slug for file paths: lowercase, hyphenated. Poet Snow Sports becomes `poet-snow-sports`. Fly Guys becomes `fly-guys`. I Think We Missed a Turn becomes `i-think-we-missed-a-turn`.

## Step 1: Pick the store and confirm access (run this first, every time)

1. Ask the user which store to work on. Offer the three by name. Default suggestion is Poet Snow Sports.
2. Point the MCP at that store. The Shopify MCP exposes a `switch-shop` tool for multi-store accounts. If the user only has one store connected, `get-shop-info` confirms which one.
3. Call `get-shop-info` and read back the store name and domain to the user. Confirm it matches the store they asked for. If it does not match, stop and resolve the mismatch before doing anything else.
4. State clearly whether this run is read-only (audit, research) or will propose writes. Writes still need per-change confirmation later.

If a requested store is not connected, say so and stop. Do not audit the wrong store.

## Step 2: Load the keyword strategy file

Every store has a strategy file at `~/.claude/{store-slug}/SEO.md`. Read it at the start of every run. All content you write must align with it.

- If the file exists, read it fully. It holds primary keywords, secondary keywords, audience search terms, banned or off-brand terms and per-page keyword assignments.
- If it does not exist, this is the first run for this store. Create it. See `references/keyword-research.md` for the build process and `assets/SEO.md.template` for the structure.

Two rules govern this file:

- **Never let two pages target the same primary keyword.** That creates keyword cannibalization where your own pages compete against each other. Before assigning a primary keyword to a page, check the assignments table. If it is taken, pick a different angle or a long-tail variant.
- **Never add keywords silently.** When research surfaces a new opportunity, propose it to the user and wait for approval before writing it into SEO.md. The file is the source of truth so it stays under human control.

## The eight workflows

Match the user's request to a workflow. Read the linked reference file before doing the work. Most reference files hold the exact queries, scoring rubrics and templates.

1. **Store SEO audit.** Pull every product, collection, page and blog article. Flag weak titles, meta, alt text, H1 structure, duplicate and thin content. Score each item and output a prioritized fix list. See `references/audit.md`.
2. **Product page optimization.** Rewrite titles under 60 characters, meta under 155, descriptions and alt text. One primary keyword plus 2 to 3 secondaries per product. Preserve the store's voice. See `references/writing-rules.md`.
3. **Collection page optimization.** Write or improve collection descriptions of 150 to 300 words with internal links to top products. See `references/writing-rules.md`.
4. **Blog SEO.** Audit articles for keyword targeting, title tags, meta, header structure and internal links. Rewrite on request. Generate briefs from keyword gaps. Every article links to at least 2 relevant products or collections. See `references/writing-rules.md` and `references/keyword-research.md`.
5. **Keyword research.** Use web search to find search intent, competitor rankings and long-tail opportunities before writing anything. See `references/keyword-research.md`.
6. **Keyword strategy file.** Build and maintain `~/.claude/{store-slug}/SEO.md`. See `references/keyword-research.md`.
7. **Technical checks.** Verify handles are clean, check redirect chains, confirm structured data basics and flag theme-controlled items that need manual fixes. See `references/technical-checks.md`.
8. **Apply changes.** Push approved updates via the Admin API. Before/after table and confirmation first. See below and `references/shopify-api.md`.

For any workflow, the exact Shopify read and write operations live in `references/shopify-api.md`. Read it before touching the API so you use the right fields. Two facts that trip people up: product and collection SEO live in a `seo { title description }` object, but page and article SEO live in `global.title_tag` and `global.description_tag` metafields, not direct fields.

## Workflow 8: Applying changes (the write gate)

This is the only workflow that mutates the store. Treat it carefully.

1. Assemble every proposed change into a before/after table. One row per field. Show the current value, the new value and the character count for length-limited fields.
2. Present the table to the user. State how many items and fields will change with real numbers. Example: "This updates 14 fields across 6 products."
3. Wait for explicit confirmation. "Looks good", "go ahead" or "approved" is enough. Silence is not.
4. Push only the approved rows. If the user approves some and rejects others, push only the approved ones.
5. After writing, verify by re-reading the changed fields and reporting what landed. Report any `userErrors` from the API verbatim. Do not claim success you did not confirm.

Before/after table format:

```
| Item | Field | Before | After | Chars |
|------|-------|--------|-------|-------|
| Poet Powder Ski | Title tag | Poet Powder Ski | Poet Powder Skis for Deep Snow | 30 |
| Poet Powder Ski | Meta desc | (empty) | Float through deep snow on the Poet Powder ski. Hand built in Canada. Free shipping over 200 dollars. | 101 |
```

## Suggested run shape

A typical first engagement with a store runs in this order. Adapt to what the user asks for.

1. Step 1 and Step 2. Pick store, confirm access, load or build SEO.md.
2. Workflow 5 keyword research if the strategy is thin or missing.
3. Workflow 1 full audit. Produce the prioritized fix list.
4. Workflows 2, 3, 4 to draft fixes for the top priorities.
5. Workflow 7 technical checks in parallel. Flag manual items.
6. Workflow 8 to apply approved changes with the before/after gate.

Report progress with real numbers at each stage. Example: "Audited 40 products. 12 have empty meta descriptions. 7 have title tags over 60 characters."
