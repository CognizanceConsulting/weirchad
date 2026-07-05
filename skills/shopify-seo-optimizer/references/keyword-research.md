# Keyword research and the SEO.md strategy file

Covers Workflow 5 (research) and Workflow 6 (the strategy file). Do research before you write copy. The strategy file is the source of truth all copy is written against.

## Workflow 5: Keyword research

Research finds three things: search intent, competitor rankings and long-tail opportunities. Use web search. Never invent numbers.

### The honesty rule on data

You do not have a paid keyword tool. That is fine. Do not fabricate monthly search volumes to fill the gap. When you lack an exact figure, say so and reason from evidence you can actually see:

- Google autocomplete order. Terms suggested first tend to have higher relative demand. Name it as the source.
- "People also ask" and related searches. These show real adjacent questions.
- Competitor pages that rank on page one for a term. If three competitors all target "all mountain skis", that term has commercial pull.
- Whether results are product pages (commercial or transactional intent) or articles (informational intent).

Report findings like this: "Google autocomplete suggests 'powder skis' before 'freeride skis', which points to higher relative demand. Source: Google autocomplete, {date}." Not like this: "Powder skis gets 12,000 searches a month" unless a named tool gave you that number.

### Process

1. Start from the store's products and collections. What does it actually sell.
2. For each core theme, run web searches for the head term and its variants. Read the autocomplete, the related searches and the top ranking pages.
3. Identify search intent per term. Informational means write an article. Commercial or transactional means optimize a product or collection.
4. Find long-tail opportunities. Longer, specific phrases with clearer intent and less competition. "powder skis for beginners" beats "skis" for a small brand. These are where a small store can actually rank.
5. Look at what competitors rank for and where the store has no page. Those gaps become article briefs (Workflow 4).
6. Bring findings back to the user. Propose additions to SEO.md. Wait for approval.

## Workflow 6: The SEO.md strategy file

Location: `~/.claude/{store-slug}/SEO.md`. One file per store. Read it at the start of every run. Write all content against it.

### First run: build it

If the file does not exist, this is the first run for the store.

1. Make the directory: `~/.claude/{store-slug}/`.
2. Copy the structure from `assets/SEO.md.template`.
3. Do a keyword research pass (Workflow 5) and pull the store's catalog so assignments map to real products and collections.
4. Fill in primary keywords, secondary keywords, audience search terms, banned or off-brand terms and the per-page assignments table.
5. Show the draft to the user. Get approval before saving it as the source of truth.

### The two unbreakable rules

**One primary keyword per page. Never shared.** Two pages targeting the same primary keyword is cannibalization. Your own pages then split rankings and compete against each other. Before assigning a primary keyword, scan the assignments table. If the term is taken, choose a different angle or a long-tail variant for the new page.

**No silent additions.** When research surfaces a new keyword worth targeting, propose it to the user with your reasoning. Wait for approval. Only then write it into SEO.md. The file stays under human control so the strategy does not drift.

### Maintaining it

- When a page is optimized, update its row: mark it done and note the date.
- When a new product, collection or article is created, add a row and assign a unique primary keyword.
- When the user approves a new keyword, add it to the right section and, if it maps to a page, the assignments table.
- Keep banned and off-brand terms current. If the user flags a phrase as off-brand during a review, add it here so it never reappears.

### Banned and off-brand terms

This section protects voice. It holds words and phrases the brand must never use: competitor trademarks, tone-wrong hype words, claims the brand cannot back, and anything the user has rejected before. Check every piece of copy against it before proposing the copy.
