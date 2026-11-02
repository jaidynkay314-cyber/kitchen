"""Builds recipes/<category>/<id>.json and .md, plus data/recipes.js (the bundle the app loads).
Run from the repo root: python3 tools/build.py"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from foods import FOODS, grams
from recipes_src import R

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEOPLE = {"J": "Jaidyn", "P": "Paris"}
def slugcat(c): return c.replace(" ", "-")
def nice(x):
    x = round(x, 2)
    return int(x) if x == int(x) else x

def build(r):
    b, share = r["base"], r["share"]
    ings = []
    for i, line in enumerate(r["ingredients"]):
        food, qty, unit = line[:3]; opt = line[3] if len(line) > 3 else {}
        k100, p100, aisle, units = FOODS[food]
        if "per" in opt: per = opt["per"]
        else:
            sh = opt.get("share", share); j = qty / (b["J"] + b["P"] * sh); per = {"J": j, "P": j * sh}
        gpu = grams(food, 1, unit)
        ings.append({"id": f"i{i+1}", "name": opt.get("label", food), "food": food, "unit": unit, "gpu": gpu,
                     "k100": k100, "p100": p100, "aisle": aisle, "per": {k: round(v, 4) for k, v in per.items()}})
    macros = {}
    for x in PEOPLE:
        k = sum(g["per"][x] * g["gpu"] * g["k100"] / 100 for g in ings); p = sum(g["per"][x] * g["gpu"] * g["p100"] / 100 for g in ings)
        macros[x] = {"kcal": round(k, 1), "protein": round(p, 1)} if r.get("serve") else {"kcal": round(k), "protein": round(p)}
    return {"schema": "kitchen-recipe", "schemaVersion": 1, "id": r["id"], "title": r["title"], "category": r["category"],
            "desc": r["desc"], "tags": r["tags"], "time": r["time"], "base": b, "portions": r["portions"], "ingredients": ings,
            "steps": [{"title": t, "text": s, "timer": tm} for t, s, tm in r["steps"]], "notes": r.get("notes", ""), "macros": macros,
            **({"serve": r["serve"], "yield": r["yield_tbsp"]} if r.get("serve") else {}), **({"sauce": r["sauce"]} if r.get("sauce") else {}), **({"short": r["short"]} if r.get("short") else {})}

def md(o):
    b = o["base"]; lines = [f"# {o['title']}", "", o["desc"], "", f"Category: {o['category']} · {o['time']} min · tags: {', '.join(o['tags'])}", "",
        "| | Portion | kcal | Protein |", "|---|---|---|---|"]
    for x, n in PEOPLE.items(): lines.append(f"| {n} | {o['portions'][x]} | {o['macros'][x]['kcal']} | {o['macros'][x]['protein']} g |")
    if o.get("serve"): lines += ["", f"Per tablespoon: {round(o['macros']['J']['kcal'])} kcal, {o['macros']['J']['protein']} g protein (macros above are per tablespoon).", "", f"## Ingredients (makes about {o['yield']} tbsp)", ""]
    else: lines += ["", f"## Ingredients (makes {b['J']} of Jaidyn's{f' and {b[chr(80)]} of Paris' + chr(39) + 's' if b['P'] else ''} serves)", ""]
    for g in o["ingredients"]:
        tot = o["yield"] * g["per"]["J"] if o.get("serve") else b["J"] * g["per"]["J"] + b["P"] * g["per"]["P"]
        if tot: lines.append(f"- {nice(tot)} {g['unit']} {g['name']}")
    lines += ["", "## Method", ""]
    for n, s in enumerate(o["steps"], 1): lines.append(f"{n}. **{s['title']}.** {s['text']}" + (f" ({round(s['timer']/60)} min)" if s["timer"] else ""))
    if o["notes"]: lines += ["", "## Notes", "", o["notes"]]
    return "\n".join(lines) + "\n"

out = []
for r in R:
    o = build(r); out.append(o)
    d = os.path.join(ROOT, "recipes", slugcat(o["category"])); os.makedirs(d, exist_ok=True)
    json.dump(o, open(os.path.join(d, o["id"] + ".json"), "w"), indent=1, ensure_ascii=False)
    open(os.path.join(d, o["id"] + ".md"), "w").write(md(o))
    print(f"{o['title']:<48} J {o['macros']['J']['kcal']:>4} kcal {o['macros']['J']['protein']:>3} g   P {o['macros']['P']['kcal']:>4} kcal {o['macros']['P']['protein']:>3} g")
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
import subprocess; subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "bundle.py")], check=True)
foods = [{"n": k, "k100": v[0], "p100": v[1], "aisle": v[2], "units": v[3]} for k, v in FOODS.items()]
# plus Solo Lifting's generic food list, so the ingredient search knows the same everyday foods
AISLES = [("Meat", r"chicken|beef|pork|lamb|steak|mince|bacon|turkey"), ("Seafood", r"salmon|tuna|prawn|fish"), ("Deli", r"ham"),
  ("Dairy and eggs", r"milk|yoghurt|cheese|egg|butter|cottage"), ("Produce", r"banana|apple|orange|berr|grape|mango|avocado|broccoli|carrot|salad|tomato|potato|corn|peas"),
  ("Frozen", r"frozen"), ("Bakery", r"bread|wrap|tortilla"), ("Drinks", r"coffee|cola|juice|beer|wine")]
have = {f["n"].lower() for f in foods}
for n, k, p, g, u in json.load(open(os.path.join(os.path.dirname(__file__), "generic.json"))):
    if n.lower() in have: continue
    aisle = next((a for a, rx in AISLES if re.search(rx, n.lower())), "Pantry")
    foods.append({"n": n, "k100": k, "p100": p, "aisle": aisle, "units": {"serve": g} if g else {}, "serve": u})
open(os.path.join(ROOT, "data", "foods.js"), "w").write("/* Ingredient nutrition per 100 g. Built by tools/build.py. */\nwindow.KITCHEN_FOODS = " + json.dumps(foods, ensure_ascii=False) + ";\n")
