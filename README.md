# Kitchen

Recipes with portions and macros for Jaidyn and Paris. Pick a meal, get the shopping list, cook it step by step, and log your portion in Solo Lifting.

Live app: https://jaidynkay314-cyber.github.io/kitchen/

## Quick guide

**Install.** Open the link in Chrome on your phone, tap the three dots, then **Add to Home screen**. It works offline after the first open, and picks up new recipes every time it opens with signal.

**Cook something.**
1. **Recipes** tab: search or filter, then tap a recipe.
2. Set how many serves each of you wants with − and +. Ingredient amounts update to match.
3. Your portion and its calories and protein are on each person's card. **Log to Solo Lifting** opens Solo Lifting with Quick add already filled in: just tap **Add**. **Send to Paris** shares her numbers.
4. **Start cooking** for cook mode: one step per screen, big text, tap to start a timer (it beeps and buzzes), and the screen stays on.

**Plan the week and shop.**
1. On a recipe, **Add to plan** and pick a day. Or on the **Plan** tab, **+ Add** on any day.
2. Change each person's serves in the plan if needed.
3. **Shop** tab: everything for the week, merged and grouped by aisle, rounded up to what you'd buy. Tick things off as you go. Pantry staples (salt, oil, spices) are hidden unless you show them. **Share** sends the list to Messages or wherever.

**Add your own recipe.**
1. **Add** tab. Name it and pick a category.
2. Say how many serves the batch makes for each of you, and Paris's share (2/3 by default).
3. **+ Ingredient**: search the food list, search packaged products online, scan a barcode, or type the label's numbers in. Enter the raw amount for the **whole batch**. Calories and protein for each person work out live at the bottom.
4. If Paris has a different share of one ingredient (less rice, a smaller tortilla), change **Paris share** on that row. **Jaidyn only** and **Paris only** are there too.
5. Add the plating guide, steps (with optional timer minutes), and notes. **Save to this phone.**
6. To get it into the shared repo: open it, **Export file**, and send the file to Claude. Or set up publishing (below).

**Sauces.** Every meal has an optional **Sauce** row. Pick one (★ marks the suggested pairing) and set tablespoons for each of you (3 and 2 to start). The sauce adds to each person's calories and protein, its ingredients join the list, and "Make the sauce" becomes step 1. The **Sauces** filter on the Recipes tab lists them all. The shopping list buys enough for a full batch, since it keeps a few days.

To change one of the built-in recipes, open it and tap **Edit a copy**.

**Share the plan and shopping list with Paris.**
1. One-off setup (already done if Kitchen says "Shared"): run `kitchen-setup.sql` in Supabase (SQL Editor, New query, paste, Run). It's the same Supabase project as Solo Lifting.
2. Settings, **Start sharing**, then **Send invite link** and send it to Paris.
3. Paris opens the link on her phone and taps **Join**. Anything already planned on either phone is kept.
4. From then on, either of you can add or change meals, tick things off or add extras. The other phone catches up when it opens the app, comes back to it, or sits on the Plan or Shop tab (every 30 seconds). It works offline and sends changes when there's signal. Plan and Shop show "Shared" with the sync status.

**Settings.** Pantry staples list, optional GitHub publishing, and **Back up everything** / **Restore a backup** for recipes and foods saved on the phone.

## Technical details

### Files
| Path | What |
|---|---|
| `index.html` | The whole app. Hash routes: `#recipes`, `#r/<id>`, `#plan`, `#shop`, `#add[/<id>]`, `#settings`. Cook mode is an overlay. |
| `data/recipes.js` | `window.KITCHEN_RECIPES = [...]`, built from `recipes/**/*.json`. Loaded with `<script src>`. |
| `data/foods.js` | `window.KITCHEN_FOODS = [...]`, nutrition per 100 g plus aisle and units. |
| `recipes/<category>/<id>.json` | One recipe each, the source of truth. A matching `.md` is a readable copy. |
| `tools/build.py` | Builds the starter recipes from `tools/recipes_src.py` and `tools/foods.py`, writes the JSON and `.md`, then `data/foods.js`. |
| `tools/bundle.py` | Bundles every `recipes/**/*.json` into `data/recipes.js`. |
| `.github/workflows/bundle.yml` | Runs `bundle.py` on any push to `recipes/**` and commits `data/recipes.js`. So adding a JSON file is enough. |
| `sw.js` | Offline cache. App shell cache-first; `data/` and the page network-first so new recipes show on launch. Bump `VERSION` each release. |

### Recipe schema (`kitchen-recipe` v1)
```json
{ "schema": "kitchen-recipe", "schemaVersion": 1, "id": "chicken-fried-rice", "title": "...", "category": "lunch prep",
  "desc": "...", "tags": ["..."], "time": 40, "base": { "J": 4, "P": 3 }, "portions": { "J": "plating guide", "P": "..." },
  "ingredients": [{ "id": "i1", "name": "shown as", "food": "food list name", "unit": "g", "gpu": 1,
                    "k100": 106, "p100": 23, "aisle": "Meat", "per": { "J": 166.67, "P": 111.11 } }],
  "steps": [{ "title": "...", "text": "...", "timer": 600 }], "notes": "...", "macros": { "J": { "kcal": 561, "protein": 53 }, "P": {...} } }
```
- `per` is one person's portion in `unit`. `gpu` is grams per unit. Macros = Σ per × gpu × k100 / 100.
- Batch amount = J serves × per.J + P serves × per.P, so any mix of serves scales exactly.
- `macros` is stored for readability only; the app always recalculates.

### Sauces
A sauce is a recipe with `"serve": "tbsp"` and `"yield"` (tablespoons per batch): its serves are tablespoons and `per` is one tablespoon. A meal's optional `"sauce"` is the suggested pairing. The chosen sauce and tablespoons are stored per recipe in `ST.sauce[id] = { id, J, P }` and copied onto plan items as `sc`. Meal macros = meal + tbsp × sauce per tbsp, rounded once at the end.

### Shared plan and shopping list
- Supabase table `kitchen_items (hh, kind, id, body, updated_at)`, one row per planned meal (`plan`, id = item key, body = item plus `d` date), shopping tick (`tick`, id = shopping key, body 1) or extra item (`extra`, body `{n}`). `body` null means deleted. A trigger stamps `updated_at`.
- Row level security is on with no policies, so the table can't be read or listed directly. The app only calls two `security definer` functions: `kitchen_push(p_hh, p_rows)` (upsert) and `kitchen_pull(p_hh, p_since)` (changes since, 500 at a time). Both need the household code, a random 20-character string that only appears in the invite link.
- Each phone keeps `ST.hh`, `ST.outbox` (pending changes keyed `kind|id`, with an edit counter so a change made mid-upload isn't lost) and `ST.since`. Sync = push the outbox, then pull and apply anything newer, skipping keys that still have a local change waiting. Two people editing different meals or ticks never clash; the same item edited on both phones goes to whoever synced last.
- Sync runs on start, when the app comes back to the foreground, when signal returns, when you open Plan or Shop, 0.7 s after any change, and every 30 s while Plan or Shop is open.
- Joining queues everything already on that phone, so nothing is lost. **Stop sharing on this phone** keeps the local copy. Backups never include the household code.

### Editor model
Batch amount plus serve counts plus a Paris share (recipe default, or per ingredient: a ratio, Jaidyn only, Paris only). `per.J = batch / (J + P × share)`, `per.P = per.J × share`. Opening any recipe in the editor reproduces its stored macros exactly (tested across all recipes).

### Storage
`localStorage` key `kitchen.v1`: recipes saved on the phone, custom foods, plan, shopping ticks and extras, pantry list, made counts, GitHub settings. Every read and write is in `try/catch`. Unsaved editor work goes to `kitchen.draft` and is offered back (never restored automatically). Backups are versioned JSON (`kitchen-backup` v1) and never include the GitHub token.

### Outside connections
- Open Food Facts (search and barcode), only when the ingredient picker asks. Same source Solo Lifting uses.
- GitHub contents API, only if a token is set in Settings. Use a fine-grained token limited to this repo with Contents read and write. The token stays on the phone.
- Solo Lifting: `?go=food&qa={"n","k","p"}` (Solo Lifting v9.1+) fills Quick add.
- Google Fonts for headings and body text, falling back to system fonts offline.

### Adding recipes (for Claude)
Either add to `tools/recipes_src.py` (and `tools/foods.py` for new foods) and run `python3 tools/build.py`, or write a `recipes/<category>/<id>.json` directly in the schema above. Push; the Action rebundles.
