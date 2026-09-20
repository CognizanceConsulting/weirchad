# Brand context: understand one brand before writing any SEO

This is Step 2 in SKILL.md and a gate. No title tag, meta description, product copy, collection copy or article gets written until the active brand's Brand Context Profile is built and confirmed. Understanding the brand first is what stops tone, voice and audience from bleeding between stores.

## The single-brand rule (restated because it matters most)

One brand per run. Poet Snow Sports, Fly Guys and I Think We Missed a Turn are separate businesses. They sell different things to different people in different voices.

- Never blend their voices, keywords, audiences or copy.
- Never open a second brand's `SEO.md` during a run.
- Never mention or compare one brand inside another brand's copy.
- If the user switches stores mid-run, stop and start a fresh run with fresh context.

A phrase that sounds right for skis will sound wrong for a different brand's customer. When a line could belong to more than one of these brands, it is too generic and it is wrong for all of them.

## The Brand Context Profile

Build this for the active brand and save it into `seo-strategy/{slug}/SEO.md` in the repo. Fields:

- **Positioning.** One line. What this brand is and why it exists, in its own terms.
- **What it sells.** The real product range. Categories, hero products, price posture.
- **Primary customer.** Who buys. Be specific: their level, their goal, their context.
- **Secondary customer.** The next audience, if any.
- **Customer vocabulary.** The words the customer actually uses to search and talk about the products. Not the words the brand wishes they used. This feeds keyword research.
- **Geography and market.** Where customers are. Language and region shape search terms, shipping and framing. Note the country and any region focus.
- **Seasonality.** When demand rises and falls for this brand's products, and the buying calendar behind it. This sets keyword timing: which terms to prioritize now, which to prepare ahead of a peak. Name the seasons and the products they lift.
- **Tone: do.** How the brand sounds. Rhythm, person, energy, humor. With 2 or 3 real example lines pulled from existing on-brand copy.
- **Tone: do not.** What the brand never sounds like. Words and registers to avoid. This is a firewall against generic copy and against a sibling brand's voice.
- **Competitors.** Who ranks against this brand for its terms. Used in keyword research, never named in customer copy.
- **Sibling brand firewall note.** State plainly: this brand is separate from the other stores on the account. Do not import their voice, keywords or audience.

## How to build it

Gather real signal before asking the user. Do not invent a brand voice.

1. **Read the store's own signals.** `get-shop-info` for name, domain and basics. Read the About page (`pages` query). Read 5 to 8 top product and collection descriptions. Note the person, rhythm and vocabulary actually in use.
2. **Look at the live site.** Web fetch the homepage and one or two key pages. See how the brand presents itself above the fold, the tagline, the imagery language.
3. **Check the customer's language.** Light web search on the core products to hear how customers and search actually phrase things. Feeds Customer vocabulary.
4. **Ask the user for the gaps.** Keep it short. Confirm positioning, primary customer, tone do's and don'ts and anything the store copy does not make obvious. If existing copy is off-brand (common, it is often why the SEO work is happening), the user's answer wins over the old copy.
5. **Write the profile. Read it back. Get confirmation.** Save the confirmed version into the brand's `SEO.md`.

## Using it in every workflow

- Before proposing any copy, check it against the profile's tone do's and don'ts and the banned terms list.
- Before a Workflow 8 write, confirm the connected store's domain still matches the profile's domain. Guard against writing one brand's copy into another brand's store.
- When the profile and the live store copy disagree on voice, the confirmed profile wins. Flag the mismatch to the user so old copy can be cleaned up.

## Re-confirming on later runs

On a return run for a brand that already has a profile, do not rebuild it blindly. Load it, read it back in one line, and ask if anything changed. Update only what the user confirms. The profile stays under human control like the rest of `SEO.md`.
