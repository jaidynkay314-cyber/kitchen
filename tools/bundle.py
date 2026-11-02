"""Collects every recipes/**/*.json into data/recipes.js, the file the app loads.
Runs automatically on GitHub (see .github/workflows/bundle.yml) whenever a recipe file changes."""
import json, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = []
for p in sorted(glob.glob(os.path.join(ROOT, "recipes", "**", "*.json"), recursive=True)):
    try:
        o = json.load(open(p, encoding="utf-8"))
        if o.get("schema") == "kitchen-recipe": out.append(o)
    except Exception as e: print("skipped", p, e)
out.sort(key=lambda o: (o.get("category", ""), o.get("title", "")))
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
open(os.path.join(ROOT, "data", "recipes.js"), "w", encoding="utf-8").write(
    "/* Built by tools/bundle.py from recipes/. Do not edit by hand. */\nwindow.KITCHEN_RECIPES = " + json.dumps(out, ensure_ascii=False) + ";\n")
print(len(out), "recipes bundled")
