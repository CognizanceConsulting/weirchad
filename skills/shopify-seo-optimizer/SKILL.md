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

Four hard gates protect the live store. Do not skip them.

1. **One brand per run.** Work on exactly one store at a time. Never audit, research or write for two brands in the same run. If the user asks for two, do them as separate sequential runs and re-establish brand context from scratch for each. See "The single-brand firewall".
2. **Confirm the store at the start of every run.** Never assume. Ask which store to target, then confirm the MCP is pointed at it before reading anything. See "Step 1".
3. **Establish brand context before writing.** Identify and understand the one brand first: what it sells, who it serves, how it sounds. No title, meta, description or copy gets written until the brand profile is confirmed. See "Step 2".
4. **Confirm write access before any change.** Reading is safe. Writing is not. Always show a before/after table and get explicit confirmation before pushing to Shopify. See "Workflow 8".

## The single-brand firewall

These stores are separate businesses with separate voices, customers and keywords. They are not one account with a name swapped in. Treat them as sealed from each other.

| Store | Domain | Slug |
|-------|--------|------|
| Poet Snow Sports | poetskis.com | `poet-snow-sports` |
| Fly Guys | (confirm domain on connect, it is a distinct site) | `fly-guys` |
| I Think We Missed a Turn | ithinkwemissedaturn.com | `i-think-we-missed-a-turn` |

Firewall rules, non-negotiable:

- Work on one brand per run. Pick it, confirm it, finish it.
- Never reuse voice, tone, keywords, audience notes, product framing or copy from one brand for another. What fits Poet snow gear will not fit a different brand's customer.
- During a run, read only the active brand's `SEO.md`. Do not open another brand's strategy file.
- Never reference or compare one brand inside another brand's copy.
- If mid-run the user pivots to a different store, stop, close out the current brand, and start a fresh run with fresh context. Do not carry anything over.

Slug is lowercase and hyphenated. It keys the per-brand strategy directory `seo-strategy/{slug}/` in this repo. Strategy files live in the repo, not in `~/.claude`, so they persist across remote and web sessions and stay version controlled. If you ever run this skill outside a repo, fall back to `~/.claude/{slug}/SEO.md`.

## Step 1: Pick the one store and confirm access (run this first, every time)

1. Ask the user which single store to work on this run. Confirm it is only one.
2. Point the MCP at that store. The Shopify MCP exposes a `switch-shop` tool for multi-store accounts. If the user only has one store connected, `get-shop-info` confirms which one.
3. Call `get-shop-info` and read back the store name and domain to the user. Confirm it matches the store they asked for and the domain in that brand's row above. If it does not match, stop and resolve the mismatch before doing anything else. Working on the wrong store is worse than doing nothing.
4. State clearly whether this run is read-only (audit, research) or will propose writes. Writes still need per-change confirmation later.

If a requested store is not connected, say so and stop. Do not audit the wrong store.

## Step 2: Establish brand context (gate: no writing before this is confirmed)

Before any SEO content is written, understand this one brand on its own terms. Skipping this is how tone, voice and audience get mixed between brands. See `references/brand-context.md` for the full process.

1. Read the brand's `SEO.md` (see Step 3). If it holds a confirmed Brand Context Profile, load it and skip to confirming it still holds.
2. If there is no profile yet, build one. Read the store's real signals first: `get-shop-info`, the About page, top product and collection descriptions, and the live homepage via web fetch. Then run a short brand discovery with the user for the gaps.
3. Fill the Brand Context Profile: one-line positioning, what the brand sells, primary and secondary customer, the customer's own search vocabulary, geography and market, tone do's and don'ts, competitors, and the explicit note that sibling brands are separate and must not bleed in.
4. Read the profile back to the user and get confirmation. Only then write copy. Save the confirmed profile into the brand's `SEO.md`.

Every piece of copy in later workflows is checked against this profile before it is proposed. If a line would fit a different brand better than this one, it is wrong.

## Step 3: Load the keyword strategy file

The active brand has a strategy file at `seo-strategy/{slug}/SEO.md` in this repo. Read it at the start of every run. Read only this brand's file. All content you write must align with it.

- If the file exists, read it fully. It holds primary keywords, secondary keywords, audience search terms, banned or off-brand terms and per-page keyword assignments.
- If it does not exist, this is the first run for this store. Create it. See `references/keyword-research.md` for the build process and `assets/SEO.md.template` for the structure.

Two rules govern this file:

- **Never let two pages target the same primary keyword.** That creates keyword cannibalization where your own pages compete against each other. Before assigning a primary keyword to a page, check the assignments table. If it is taken, pick a different angle or a long-tail variant.
- **Never add keywords silently.** When research surfaces a new opportunity, propose it to the user and wait for approval before writing it into SEO.md. The file is the source of truth so it stays under human control.

## The eight workflows

Match the user's request to a workflow. Read the linked reference file before doing the work. Most reference files hold the exact queries, scoring rubrics and templates.

1. **Store SEO audit.** Pull every product, collection, page and blog article. Flag weak titles, meta, alt text, H1 structure, duplicate and thin content. Score each item and output a prioritized fix list. See `references/audit.md`.
2. **Product page optimization.** Rewrite titles under 60 characters, meta under 155, descriptions and alt text. One primary keyword plus 2 to 3 secondaries per product. Write in the active brand's confirmed voice, checked against its Brand Context Profile. See `references/writing-rules.md`.
3. **Collection page optimization.** Write or improve collection descriptions of 150 to 300 words with internal links to top products. See `references/writing-rules.md`.
4. **Blog SEO.** Audit articles for keyword targeting, title tags, meta, header structure and internal links. Rewrite on request. Generate briefs from keyword gaps. Every article links to at least 2 relevant products or collections. See `references/writing-rules.md` and `references/keyword-research.md`.
5. **Keyword research.** Use web search to find search intent, competitor rankings and long-tail opportunities before writing anything. See `references/keyword-research.md`.
6. **Keyword strategy file.** Build and maintain `seo-strategy/{slug}/SEO.md`, including the Brand Context Profile. See `references/keyword-research.md` and `references/brand-context.md`.
7. **Technical checks.** Verify handles are clean, check redirect chains, confirm structured data basics and flag theme-controlled items that need manual fixes. See `references/technical-checks.md`.
8. **Apply changes.** Push approved updates via the Admin API. Before/after table and confirmation first. See below and `references/shopify-api.md`.

For any workflow, the exact Shopify read and write operations live in `references/shopify-api.md`. Read it before touching the API so you use the right fields. Two facts that trip people up: product and collection SEO live in a `seo { title description }` object, but page and article SEO live in `global.title_tag` and `global.description_tag` metafields, not direct fields.

## Workflow 8: Applying changes (the write gate)

This is the only workflow that mutates the store. Treat it carefully.

1. **Voice self-check first.** Before anything reaches the table, reread the active brand's Brand Context Profile and re-check every proposed line against its Tone: do not list and the banned terms in SEO.md. Apply the test: could this sentence belong to a different brand just as well. Fix or drop anything that fails. Nothing off-brand reaches the before/after table.
2. Assemble every approved-in-voice change into a before/after table. One row per field. Show the current value, the new value and the character count for length-limited fields.
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

1. Steps 1, 2 and 3. Pick the one store, confirm access, establish and confirm brand context, load or build SEO.md.
2. Workflow 5 keyword research if the strategy is thin or missing.
3. Workflow 1 full audit. Produce the prioritized fix list.
4. Workflows 2, 3, 4 to draft fixes for the top priorities.
5. Workflow 7 technical checks in parallel. Flag manual items.
6. Workflow 8 to apply approved changes with the before/after gate.

Report progress with real numbers at each stage. Example: "Audited 40 products. 12 have empty meta descriptions. 7 have title tags over 60 characters."
