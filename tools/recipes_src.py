# Source for the starter recipes. Each ingredient line is (food, batch qty, unit[, options]).
# The batch is what the method below makes for `base` serves (J = Jaidyn's serve, P = Paris's serve).
# By default each ingredient is split so Paris's serve is `share` of Jaidyn's. Options:
#   share: a different Paris share for this ingredient; per: explicit {"J": qty, "P": qty}; label: display name
R = []
def recipe(**k): R.append(k)

recipe(id="bbq-souvlaki-chicken-thighs", title="BBQ Souvlaki Chicken Thighs", category="dinner",
 desc="Lemon, garlic and oregano chicken thighs off the barbecue, with sweet potato mash, broccoli and a high-protein tzatziki.",
 tags=["chicken", "bbq", "high protein"], time=45, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "250 g chicken, about 300 g sweet potato mash, half the broccoli and tzatziki",
           "P": "150 g chicken, about 200 g sweet potato mash, half the broccoli and tzatziki"},
 ingredients=[
  ("chicken thigh fillet, skinless", 400, "g", {"per": {"J": 250, "P": 150}}),
  ("olive oil", 1, "tbsp", {"share": 1}), ("lemon", 1, "whole", {"share": 1, "label": "lemon, juiced and zested"}),
  ("garlic", 3, "clove", {"share": 1}), ("dried oregano", 2, "tsp", {"share": 1}), ("smoked paprika", 1, "tsp", {"share": 1}),
  ("salt", 0.5, "tsp", {"share": 1}),
  ("sweet potato", 500, "g", {"per": {"J": 300, "P": 200}, "label": "sweet potato, peeled and chopped"}),
  ("butter", 10, "g", {"share": 1}), ("milk, full cream", 2, "tbsp", {"share": 1}),
  ("broccoli", 300, "g", {"share": 1, "label": "broccoli, in florets"}),
  ("high-protein Greek yoghurt", 150, "g", {"share": 1}), ("Lebanese cucumber", 0.5, "whole", {"share": 1, "label": "Lebanese cucumber, grated and squeezed dry"}),
 ],
 steps=[
  ("Marinate the chicken", "Mix the oil, lemon juice and zest, two of the garlic cloves, oregano, paprika and salt. Toss the chicken through and leave at least 20 minutes, or up to a day in the fridge.", 1200),
  ("Boil the sweet potato", "Cover the sweet potato with cold salted water, bring to the boil and simmer until a knife slides straight through.", 900),
  ("Make the tzatziki", "Stir the cucumber and the last garlic clove through the yoghurt with a squeeze of lemon and a pinch of salt. Keep it in the fridge.", 0),
  ("Barbecue the chicken", "Cook on a hot barbecue plate or grill, 5 to 6 minutes a side, until charred and cooked through (75°C in the thickest part).", 660),
  ("Rest, and cook the broccoli", "Rest the chicken 5 minutes. Steam or microwave the broccoli until bright green and just tender.", 300),
  ("Mash and serve", "Drain the sweet potato and mash with the butter and milk, then season. Slice the chicken and serve with the mash, broccoli and tzatziki.", 0),
 ], notes="Leftover cooked thighs keep 3 days in the fridge for a lunch wrap.")

recipe(id="porterhouse-sweet-potato", sauce="garlic-herb-yoghurt", title="Porterhouse with Sweet Potato Mash and Broccolini", category="dinner",
 desc="A quick Sunday steak night: porterhouse, a fist of sweet potato mash and broccolini.",
 tags=["beef", "quick", "high protein"], time=25, base={"J": 1, "P": 1}, share=0.5,
 portions={"J": "2 steaks (2 × 200 g), a fist of mash, broccolini", "P": "1 steak (200 g), a smaller fist of mash, broccolini"},
 ingredients=[
  ("porterhouse steak", 600, "g", {"per": {"J": 400, "P": 200}, "label": "porterhouse steaks (200 g each)"}),
  ("sweet potato", 270, "g", {"per": {"J": 150, "P": 120}}), ("butter", 10, "g", {"share": 1}),
  ("broccolini", 1, "bunch", {"share": 1}), ("olive oil", 2, "tsp", {"share": 1}), ("salt", 0.5, "tsp", {"share": 1}),
 ],
 steps=[
  ("Bring the steak to room temp", "Take the steaks out 20 minutes before cooking. Pat dry and season well.", 1200),
  ("Boil the sweet potato", "Peel, chop and simmer the sweet potato until soft.", 900),
  ("Cook the steak", "Rub with oil and cook on a very hot pan or barbecue, about 3 to 4 minutes a side for medium rare.", 420),
  ("Rest and finish", "Rest the steak 5 minutes. Steam the broccolini and mash the sweet potato with the butter.", 300),
 ], notes="Fat trimmed off the steak saves about 80 kcal per 200 g.")

recipe(id="chicken-fried-rice", sauce="sriracha-lime-yoghurt", title="Chicken Fried Rice", category="lunch prep",
 desc="Freezer-friendly fried rice. Best as a pre-gym lunch: lower fat and fibre.",
 tags=["chicken", "freezer", "rice"], time=40, base={"J": 4, "P": 3}, share=2/3,
 portions={"J": "1 regular container (a sixth of the batch)", "P": "2/3 of a regular container"},
 ingredients=[
  ("chicken breast", 1000, "g", {"label": "chicken breast, diced small"}), ("white rice, uncooked", 2, "cup", {"label": "white rice (cook the day before)"}),
  ("eggs", 6, "whole"), ("frozen mixed veg", 500, "g"), ("spring onions", 4, "whole", {"label": "spring onions, sliced"}),
  ("garlic", 4, "clove"), ("fresh ginger, grated", 1, "tbsp"), ("soy sauce", 80, "ml", {"label": "soy sauce (salt-reduced if you like)"}),
  ("olive oil", 1, "tbsp", {"label": "oil"}),
 ],
 steps=[
  ("Cook the chicken", "Heat half the oil in a wok on high and cook the chicken in two batches until browned and cooked through. Set aside.", 600),
  ("Scramble the eggs", "Scramble the eggs in the same pan, break them up and set aside with the chicken.", 120),
  ("Aromatics and veg", "Add the rest of the oil, the garlic and ginger. Stir 30 seconds, add the frozen veg and cook 3 to 4 minutes.", 240),
  ("Fry the rice", "Add the cold rice and toss on high heat for 4 to 5 minutes, breaking up clumps.", 300),
  ("Combine", "Return the chicken and egg, add the soy sauce and spring onion and toss through.", 0),
  ("Portion", "Spread on a tray to cool fast, then portion: 4 regular and 3 small containers.", 0),
 ], notes="Keeps 2 to 3 months frozen. Reheat until steaming hot all the way through.")

recipe(id="chipotle-chilli-con-carne", sauce="chipotle-lime-yoghurt", title="Chipotle Chilli Con Carne", category="lunch prep",
 desc="Smoky chilli with rice. Post-gym or rest days.",
 tags=["beef", "pork", "freezer", "rice"], time=50, base={"J": 4, "P": 3}, share=2/3,
 portions={"J": "a sixth of the chilli (weigh the pot, divide by 6) and 3/4 cup cooked rice", "P": "2/3 of Jaidyn's chilli scoop and 1/2 cup cooked rice"},
 ingredients=[
  ("lean pork and beef mince (50/50)", 1000, "g"), ("kidney beans, tinned (drained)", 2, "tin", {"label": "kidney beans, drained and rinsed"}),
  ("diced tomatoes, tinned", 2, "tin"), ("brown onion", 1, "whole", {"label": "brown onion, diced"}), ("red capsicum", 1, "whole", {"label": "red capsicum, diced"}),
  ("garlic", 4, "clove"), ("chipotle powder", 2, "tsp"), ("ground cumin", 2, "tsp"), ("smoked paprika", 2, "tsp"), ("dried oregano", 1, "tsp"),
  ("white rice, uncooked", 1.5, "cup"),
 ],
 steps=[
  ("Brown the mince", "Brown the mince in a large pot over medium-high heat, breaking it up. No extra oil needed.", 600),
  ("Soften the veg", "Add the onion, capsicum and garlic and cook 4 to 5 minutes.", 300),
  ("Bloom the spices", "Stir in all the spices and cook 1 minute until fragrant.", 60),
  ("Simmer", "Add the tomatoes and beans and simmer uncovered until thick, stirring now and then.", 1500),
  ("Cook the rice", "Cook the rice separately. Season the chilli and add your hot sauce.", 900),
  ("Portion", "Weigh the chilli and divide by 6 for one regular serve. Pack 4 regular (3/4 cup rice) and 3 small (2/3 chilli, 1/2 cup rice).", 0),
 ], notes="The batch makes exactly 4 regular and 3 small serves.")

recipe(id="chicken-burritos", sauce="chipotle-lime-yoghurt", title="Chicken Burritos", category="lunch prep",
 desc="Grab-and-go freezer burritos for hungrier days.",
 tags=["chicken", "freezer", "grab and go"], time=45, base={"J": 4, "P": 3}, share=2/3,
 portions={"J": "1 large burrito", "P": "1 burrito on a regular tortilla with 2/3 of the filling"},
 ingredients=[
  ("chicken breast", 1000, "g"), ("white rice, uncooked", 1.5, "cup"), ("black beans, tinned (drained)", 1, "tin", {"label": "black beans, drained and rinsed"}),
  ("cheddar, grated", 120, "g", {"label": "grated cheese"}),
  ("large tortillas", 4, "whole", {"per": {"J": 1, "P": 0}}), ("regular tortillas", 3, "whole", {"per": {"J": 0, "P": 1}}),
  ("salsa", 0.5, "cup"), ("ground cumin", 2, "tsp"), ("smoked paprika", 2, "tsp"), ("chipotle powder", 1, "tsp"), ("lime", 1, "whole", {"label": "lime (optional)"}),
 ],
 steps=[
  ("Cook the chicken", "Rub the chicken with the spices and bake at 200°C until cooked through. Rest 5 minutes, then shred with two forks.", 1350),
  ("Cook the rice", "Cook the rice and stir through the lime juice and a pinch of salt.", 900),
  ("Mix the filling", "Toss the chicken with the beans, salsa and hot sauce. Let everything cool before rolling.", 0),
  ("Roll", "Large tortillas: rice, chicken mix, cheese. Regular tortillas: about 2/3 as much of each. Fold the sides in and roll tightly.", 0),
  ("Wrap and freeze", "Wrap each one in cling wrap or foil, then bag and freeze.", 0),
 ], notes="Microwave from frozen 3 to 4 minutes (foil off), turning halfway.")

recipe(id="friday-chicken-veg-bowl", sauce="lemon-tahini-yoghurt", title="Lean Chicken and Veg Bowl", category="friday",
 desc="Light, high-protein freezer lunch for Fridays before beers.",
 tags=["chicken", "freezer", "low calorie"], time=35, base={"J": 6, "P": 0}, share=2/3,
 portions={"J": "1 container (a sixth of the batch)", "P": "2/3 of a container"},
 ingredients=[
  ("chicken breast", 1100, "g", {"label": "chicken breast, diced"}), ("frozen mixed veg", 900, "g"), ("white rice, uncooked", 125, "g", {"label": "jasmine rice (about 2/3 cup)"}),
  ("soy sauce", 3, "tbsp"), ("sweet chilli sauce", 2, "tbsp"), ("garlic", 2, "clove"), ("fresh ginger, grated", 1, "tsp"),
 ],
 steps=[
  ("Cook the rice", "Cook the rice and spread it on a tray to cool.", 900),
  ("Brown the chicken", "Spray a large pan and brown the chicken in two batches over high heat.", 840),
  ("Veg", "Add the garlic, ginger and frozen veg and cook until just tender.", 300),
  ("Sauce", "Return the chicken, add the soy and sweet chilli and toss 1 minute.", 60),
  ("Portion", "Divide the rice and chicken between 6 containers. Cool, lid and freeze.", 0),
 ], notes="")

recipe(id="friday-beef-meatballs", sauce="garlic-herb-yoghurt", title="Beef Meatballs in Tomato and Veg", category="friday",
 desc="Oven-baked lean meatballs in a veggie passata. Freezes well.",
 tags=["beef", "freezer", "low calorie"], time=40, base={"J": 6, "P": 0}, share=0.6,
 portions={"J": "5 meatballs with sauce", "P": "3 meatballs with sauce"},
 ingredients=[
  ("lean beef mince (5% fat)", 1000, "g"), ("eggs", 1, "whole"), ("rolled oats", 40, "g"), ("brown onion", 0.66, "whole", {"label": "small onion, grated"}),
  ("garlic", 2, "clove"), ("dried oregano", 1, "tsp"), ("passata", 700, "g"), ("zucchini", 2, "whole", {"label": "zucchini, diced"}),
  ("red capsicum", 1, "whole", {"label": "red capsicum, diced"}), ("parmesan, grated", 50, "g"),
 ],
 steps=[
  ("Roll", "Heat the oven to 200°C. Mix the mince, egg, oats, onion, garlic, oregano, salt and pepper and roll about 30 balls.", 0),
  ("Bake", "Bake on lined trays until browned.", 1000),
  ("Sauce", "Meanwhile simmer the passata with the zucchini and capsicum.", 600),
  ("Combine and portion", "Add the meatballs to the sauce and simmer 5 minutes. Pack 5 meatballs plus sauce per container, top with parmesan, cool and freeze.", 300),
 ], notes="")

recipe(id="friday-beef-bean-chilli", sauce="chipotle-lime-yoghurt", title="Lean Beef and Bean Chilli", category="friday",
 desc="No-rice chilli: high protein, lower calorie.",
 tags=["beef", "freezer", "low calorie"], time=45, base={"J": 6, "P": 0}, share=2/3,
 portions={"J": "1 container (a sixth of the batch)", "P": "2/3 of a container"},
 ingredients=[
  ("lean beef mince (5% fat)", 1000, "g"), ("kidney beans, tinned (drained)", 2, "tin"), ("diced tomatoes, tinned", 2, "tin"),
  ("brown onion", 1, "whole"), ("red capsicum", 1, "whole"), ("garlic", 3, "clove"), ("ground cumin", 2, "tsp"), ("smoked paprika", 2, "tsp"),
  ("chipotle powder", 1, "tsp"), ("dried oregano", 1, "tsp"), ("olive oil", 1, "tbsp"),
 ],
 steps=[
  ("Soften", "Heat the oil and soften the onion and capsicum, then add the garlic and spices for 1 minute.", 360),
  ("Brown", "Add the mince and brown, breaking it up.", 480),
  ("Simmer", "Add the tomatoes, beans and half a cup of water. Simmer uncovered until thick.", 1650),
  ("Portion", "Season, portion into 6 containers, cool and freeze.", 0),
 ], notes="Top with a spoon of high-protein yoghurt instead of sour cream.")

recipe(id="friday-frittata-muffins", sauce="sriracha-lime-yoghurt", title="Egg and Veg Frittata Muffins", category="friday",
 desc="24 muffins, frozen in fours. Microwave 60 to 90 seconds from frozen.",
 tags=["eggs", "freezer", "low calorie"], time=35, base={"J": 6, "P": 0}, share=0.75,
 portions={"J": "4 muffins", "P": "3 muffins"},
 ingredients=[
  ("eggs", 12, "whole"), ("liquid egg whites", 500, "ml"), ("shaved ham, lean", 200, "g", {"label": "lean ham or cooked chicken, diced"}),
  ("baby spinach", 150, "g"), ("red capsicum", 1, "whole"), ("spring onions", 4, "whole"), ("reduced-fat cheese, grated", 100, "g"),
 ],
 steps=[
  ("Prep", "Heat the oven to 180°C and spray two 12-hole muffin tins well.", 0),
  ("Fill", "Divide the ham, spinach, capsicum and spring onion between the holes.", 0),
  ("Pour", "Whisk the eggs, whites, salt and pepper, pour over the fillings about three-quarters full and top with cheese.", 0),
  ("Bake", "Bake until set, then cool on a rack.", 1200),
  ("Freeze", "Freeze on a tray, then bag in fours.", 0),
 ], notes="")

recipe(id="breakie-burgers", title="Breakie Burgers", category="breakfast",
 desc="Freezer breakfast burgers: English muffin, pork and beef patty, cheese, homemade pickles and hot sauce.",
 tags=["breakfast", "freezer", "grab and go"], time=40, base={"J": 6, "P": 6}, share=1,
 portions={"J": "1 burger with a double lean patty (160 g raw)", "P": "1 burger with a single patty (80 g raw)"},
 ingredients=[
  ("English muffins", 12, "whole"), ("lean pork and beef mince (50/50)", 1440, "g", {"per": {"J": 160, "P": 80}, "label": "pork and beef mince (80 g patties)"}),
  ("cheddar slice", 12, "whole", {"label": "small cheese slices"}),
 ],
 steps=[
  ("Shape", "Shape the mince into 80 g patties, a little wider than the muffins. Season.", 0),
  ("Cook", "Cook in a hot pan or on the barbecue about 3 to 4 minutes a side until cooked through.", 480),
  ("Build", "Muffin, patty (two for Jaidyn's), cheese slice, pickles and hot sauce.", 0),
  ("Freeze", "Cool, wrap each burger and freeze. Microwave from frozen about 90 seconds, then toast if you like.", 0),
 ], notes="Add an egg for about 70 kcal and 6 g protein.")

recipe(id="bbq-spiced-chicken-breast", title="BBQ Spiced Chicken Breast with Sweet Potato Mash and Broccolini", category="dinner", short="BBQ chicken breast, mash, broccolini",
 desc="Lean weeknight barbecue: dry-rubbed chicken breast, sweet potato mash and broccolini. Good with a yoghurt sauce.",
 tags=["chicken", "bbq", "high protein", "lean"], time=35, base={"J": 1, "P": 1}, share=0.6, sauce="mustard-lime-yoghurt",
 portions={"J": "On the plate: about 190 g cooked chicken (250 g raw), 300 g mash (a heaped cup and a half), 100 g broccolini",
           "P": "On the plate: about 120 g cooked chicken (160 g raw), 175 g mash (a cup), 75 g broccolini"},
 ingredients=[
  ("chicken breast", 410, "g", {"per": {"J": 250, "P": 160}, "label": "chicken breast"}),
  ("spices (your mix)", 2, "tsp", {"share": 1, "label": "Spices (paprika, garlic and onion powder, whatever you like)"}),
  ("sweet potato", 475, "g", {"per": {"J": 300, "P": 175}, "label": "sweet potato, peeled and chopped"}),
  ("milk, full cream", 2, "tbsp", {"share": 1, "label": "milk, for the mash"}),
  ("broccolini", 1, "bunch", {"per": {"J": 100 / 175, "P": 75 / 175}, "label": "broccolini (or 175 g broccoli)"}),
 ],
 steps=[
  ("Rub the chicken", "If the breasts are thick, butterfly them or pound to an even thickness so they cook evenly without drying out. Coat both sides with the spices and a pinch of salt.", 0),
  ("Boil the sweet potato", "Cover with cold salted water, bring to the boil and simmer until a knife slides straight through.", 900),
  ("Barbecue the chicken", "Hot barbecue, no oil needed on a clean, well-heated grill. About 5 to 6 minutes a side until it hits 74°C in the thickest part. Pull it the moment it gets there: that's what keeps breast juicy.", 660),
  ("Rest, and cook the broccolini", "Rest the chicken 5 minutes under foil. Steam or microwave the broccolini until bright green and just tender, or throw it on the barbecue for the last 3 minutes.", 300),
  ("Mash and serve", "Drain the sweet potato, mash with the milk and season. Slice the chicken and plate up with the mash, broccolini and your sauce.", 0),
 ], notes="Raw chicken breast loses about a quarter of its weight cooking, so 250 g raw is about 190 g on the plate. Weigh raw if you can; the cooked weights are a guide. A knob of butter in the mash adds about 70 kcal.")

# ---- Sauces: serves are tablespoons. Each ingredient line is the whole batch; it is divided by the yield. ----
def sauce(id, title, desc, yield_tbsp, ings, steps, notes="", tags=()):
    recipe(id=id, title=title, category="sauce", desc=desc, tags=["sauce", *tags], time=5, base={"J": 3, "P": 2}, share=1,
           serve="tbsp", yield_tbsp=yield_tbsp, portions={"J": "3 tablespoons", "P": "2 tablespoons"},
           ingredients=[(f, q, u, {"per": {"J": q / yield_tbsp, "P": q / yield_tbsp}, **({"label": l} if l else {})}) for f, q, u, l in ings],
           steps=steps, notes=notes)

YOG = "Made with high-protein Greek yoghurt (about 60 kcal and 10 g protein per 100 g). Full-fat Greek yoghurt roughly doubles the calories and halves the protein."
sauce("mustard-lime-yoghurt", "Mustard Lime Yoghurt", "Jaidyn's sauce: Greek yoghurt, wholegrain mustard and lime. Fresh and sharp, great on barbecued chicken.", 12,
  [("high-protein Greek yoghurt", 170, "g", "Greek yoghurt"), ("wholegrain mustard", 1, "tbsp", ""), ("lime juice", 3, "tsp", ""), ("spices (your mix)", 1, "tsp", "spices to taste")],
  [("Mix", "Stir everything together and season with salt and pepper. Taste and add more lime or mustard as you like. Keeps 4 days in the fridge.", 0)], YOG, ["chicken"])
sauce("tzatziki", "Tzatziki", "Greek yoghurt, cucumber, garlic, lemon and dill or mint.", 14,
  [("high-protein Greek yoghurt", 170, "g", "Greek yoghurt"), ("Lebanese cucumber", 0.5, "whole", "Lebanese cucumber, grated and squeezed dry"),
   ("garlic", 1, "clove", "garlic, finely grated"), ("lemon juice", 2, "tsp", ""), ("fresh herbs (dill, mint, parsley or chives)", 1, "tbsp", "fresh dill or mint, chopped")],
  [("Squeeze the cucumber", "Grate the cucumber and squeeze it hard in your hands or a clean tea towel. This stops the tzatziki going watery.", 0),
   ("Mix", "Stir everything into the yoghurt with a pinch of salt. Best after 10 minutes in the fridge. Keeps 3 days.", 0)], YOG, ["greek", "chicken", "lamb"])
sauce("garlic-herb-yoghurt", "Garlic Herb Yoghurt", "Garlicky yoghurt with lemon and fresh herbs. Good with steak, chicken and roast veg.", 12,
  [("high-protein Greek yoghurt", 170, "g", "Greek yoghurt"), ("garlic", 2, "clove", "garlic, finely grated"), ("lemon juice", 1, "tbsp", ""),
   ("fresh herbs (dill, mint, parsley or chives)", 2, "tbsp", "parsley or chives, chopped")],
  [("Mix", "Stir everything together with salt and pepper. Let it sit 10 minutes so the garlic mellows. Keeps 3 days.", 0)], YOG, ["beef", "chicken"])
sauce("chipotle-lime-yoghurt", "Chipotle Lime Yoghurt", "Smoky, a little hot. Made for the burritos, chilli and anything Mexican.", 12,
  [("high-protein Greek yoghurt", 170, "g", "Greek yoghurt"), ("chipotle powder", 1, "tsp", "chipotle powder (half for mild)"), ("lime juice", 2, "tsp", ""), ("ground cumin", 0.25, "tsp", "pinch of ground cumin")],
  [("Mix", "Stir everything together with a pinch of salt. It gets hotter as it sits. Keeps 4 days.", 0)], YOG, ["mexican"])
sauce("lemon-tahini-yoghurt", "Lemon Tahini Yoghurt", "Nutty and creamy. Great with chicken, lamb or roast veg. A bit richer than the others.", 13,
  [("high-protein Greek yoghurt", 170, "g", "Greek yoghurt"), ("tahini", 1, "tbsp", ""), ("lemon juice", 1, "tbsp", ""), ("garlic", 1, "clove", "small garlic clove, grated")],
  [("Mix", "Whisk the tahini with the lemon juice first (it thickens, then loosens), then stir through the yoghurt and garlic. Thin with a splash of water. Keeps 4 days.", 0)], YOG, ["chicken", "lamb"])
sauce("sriracha-lime-yoghurt", "Sriracha Lime Yoghurt", "Creamy chilli kick. Good on fried rice, chicken bowls and the frittata muffins.", 12,
  [("high-protein Greek yoghurt", 170, "g", "Greek yoghurt"), ("sriracha", 1, "tbsp", "sriracha (more to taste)"), ("lime juice", 2, "tsp", "")],
  [("Mix", "Stir together. Keeps 4 days.", 0)], YOG, ["asian"])

# ---- Batch 2 dinners (picked 2 Nov 2026) ----
RICE_J, RICE_P = 0.4, 0.25  # cups uncooked: about 220 g and 140 g cooked
recipe(id="honey-soy-chicken-skewers", sauce="sriracha-lime-yoghurt", title="Honey Soy Chicken Skewers with Rice and Slaw", category="dinner", short="Honey soy chicken skewers, rice, slaw",
 desc="Sticky honey soy chicken thigh skewers off the barbecue, with rice and a crunchy lime slaw.",
 tags=["chicken", "bbq", "asian"], time=40, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "3 skewers (220 g raw chicken), a cup of cooked rice, a big handful of slaw", "P": "2 skewers (140 g raw chicken), 2/3 cup cooked rice, a handful of slaw"},
 ingredients=[
  ("chicken thigh fillet, skinless", 360, "g", {"per": {"J": 220, "P": 140}, "label": "chicken thigh, cut into 3 cm pieces"}),
  ("soy sauce", 2, "tbsp", {"share": 1, "label": "soy sauce (salt-reduced)"}), ("honey", 1, "tbsp", {"share": 1}),
  ("garlic", 2, "clove", {"share": 1}), ("fresh ginger, grated", 1, "tsp", {"share": 1}), ("sesame oil", 1, "tsp", {"share": 1}),
  ("white rice, uncooked", RICE_J + RICE_P, "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "jasmine rice"}),
  ("coleslaw mix", 200, "g", {"per": {"J": 120, "P": 80}}), ("spring onions", 2, "whole", {"share": 1, "label": "spring onions, sliced"}),
  ("lime juice", 1, "tbsp", {"share": 1, "label": "lime juice, for the slaw"}),
 ],
 steps=[
  ("Marinate", "Mix the soy, honey, garlic, ginger and sesame oil. Toss the chicken through and leave 20 minutes (or overnight). If using bamboo skewers, soak them now.", 1200),
  ("Cook the rice", "Rinse the rice and cook it (absorption or rice cooker).", 900),
  ("Thread and grill", "Thread the chicken onto skewers. Barbecue on medium-high, turning every couple of minutes, until sticky, charred at the edges and cooked through. Brush with leftover marinade only in the first half of cooking.", 600),
  ("Slaw and serve", "Toss the slaw mix and spring onion with the lime juice and a pinch of salt. Serve the skewers over rice with the slaw.", 0),
 ], notes="The honey catches easily: medium-high, not blazing, and keep them moving.")

recipe(id="san-choy-bow", sauce="sriracha-lime-yoghurt", title="San Choy Bow", category="dinner", short="San choy bow with rice",
 desc="Savoury pork and chicken mince in crisp lettuce cups, with a little rice on the side.",
 tags=["pork", "chicken", "asian", "quick"], time=25, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "About 250 g of the cooked mince filling (5 or 6 lettuce cups), 2/3 cup cooked rice", "P": "The rest of the filling (3 or 4 lettuce cups), 1/2 cup cooked rice"},
 ingredients=[
  ("lean pork mince", 200, "g"), ("chicken mince", 200, "g"),
  ("garlic", 2, "clove", {"share": 1}), ("fresh ginger, grated", 1, "tbsp", {"share": 1}),
  ("carrot", 1, "whole", {"label": "carrot, grated"}), ("red capsicum", 0.5, "whole", {"label": "red capsicum, finely diced"}),
  ("spring onions", 3, "whole", {"share": 1, "label": "spring onions, sliced"}),
  ("oyster sauce", 2, "tbsp"), ("soy sauce", 1, "tbsp", {"label": "soy sauce (salt-reduced)"}), ("hoisin sauce", 1, "tbsp"), ("sesame oil", 1, "tsp", {"share": 1}),
  ("iceberg lettuce", 1, "whole", {"share": 1, "label": "iceberg lettuce, leaves separated into cups"}),
  ("white rice, uncooked", 0.25 + 0.17, "cup", {"per": {"J": 0.25, "P": 0.17}, "label": "jasmine rice"}),
 ],
 steps=[
  ("Rice and lettuce", "Put the rice on. Separate the lettuce into whole cup-shaped leaves, rinse, and chill them in the fridge so they're crisp.", 900),
  ("Brown the mince", "Heat the sesame oil in a wok on high. Add both minces and cook, breaking it up, until browned and any liquid has cooked off.", 420),
  ("Add the veg", "Add the garlic, ginger, carrot and capsicum and stir-fry 2 minutes.", 120),
  ("Sauce it", "Add the oyster, soy and hoisin sauces and toss until glossy. Stir through most of the spring onion.", 60),
  ("Serve", "Spoon into lettuce cups, top with the rest of the spring onion, and serve with the rice on the side.", 0),
 ], notes="Tinned water chestnuts, diced, add good crunch for almost no calories.")

recipe(id="chicken-fajitas", sauce="chipotle-lime-yoghurt", title="Chicken Fajitas", category="dinner", short="Chicken fajitas",
 desc="Spiced chicken breast with charred capsicum and onion, in mini tortillas.",
 tags=["chicken", "mexican", "quick"], time=30, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "4 mini tortillas, 220 g raw chicken, half the veg", "P": "3 mini tortillas, 140 g raw chicken, half the veg"},
 ingredients=[
  ("chicken breast", 360, "g", {"per": {"J": 220, "P": 140}, "label": "chicken breast, in strips"}),
  ("spices (your mix)", 3, "tsp", {"share": 1, "label": "Fajita spices (smoked paprika, cumin, garlic powder, oregano, chilli)"}),
  ("red capsicum", 2, "whole", {"share": 1, "label": "capsicums (mixed colours), sliced"}), ("red onion", 1, "whole", {"share": 1, "label": "red onion, sliced"}),
  ("olive oil", 2, "tsp", {"share": 1}), ("lime juice", 1, "tbsp", {"share": 1}),
  ("mini tortillas", 7, "whole", {"per": {"J": 4, "P": 3}}), ("salsa", 0.25, "cup", {"share": 1}),
 ],
 steps=[
  ("Season", "Toss the chicken with the spices, half the oil and a pinch of salt.", 0),
  ("Char the veg", "Very hot pan or barbecue plate. Cook the capsicum and onion with the rest of the oil until soft and charred at the edges. Set aside.", 360),
  ("Cook the chicken", "Same pan, high heat. Cook the chicken strips in one layer, turning once, until browned and cooked through.", 360),
  ("Serve", "Squeeze the lime over the chicken and veg. Warm the tortillas in a dry pan and load them up with the salsa and sauce.", 0),
 ], notes="Swap a tortilla each for shredded lettuce to cut about 75 kcal.")

recipe(id="lemon-herb-salmon", sauce="garlic-herb-yoghurt", title="Lemon Herb Salmon with Baby Potatoes and Beans", category="dinner", short="Lemon herb salmon, potatoes, beans",
 desc="Oven-baked salmon with lemon and herbs, crispy baby potatoes and green beans. One tray, mostly hands off.",
 tags=["fish", "tray bake", "omega 3"], time=40, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "200 g salmon (a large fillet), 250 g potatoes, 125 g beans", "P": "130 g salmon (a regular fillet), 150 g potatoes, 100 g beans"},
 ingredients=[
  ("salmon fillet, skin on", 330, "g", {"per": {"J": 200, "P": 130}}),
  ("baby potatoes", 400, "g", {"per": {"J": 250, "P": 150}, "label": "baby potatoes, halved"}),
  ("green beans", 225, "g", {"per": {"J": 125, "P": 100}, "label": "green beans, trimmed"}),
  ("olive oil", 2, "tsp", {"share": 1}), ("lemon", 1, "whole", {"share": 1, "label": "lemon, zested and sliced"}),
  ("garlic", 2, "clove", {"share": 1}), ("fresh herbs (dill, mint, parsley or chives)", 2, "tbsp", {"share": 1, "label": "fresh dill or parsley, chopped"}),
 ],
 steps=[
  ("Potatoes in", "Oven to 220°C (200°C fan). Toss the potatoes with the oil, salt and pepper on a lined tray and roast.", 1200),
  ("Season the salmon", "Mix the lemon zest, crushed garlic and herbs. Pat the salmon dry and press the mix on top.", 0),
  ("Salmon and beans in", "Push the potatoes to the sides. Add the salmon skin side down, lay lemon slices around, and scatter the beans. Roast until the salmon just flakes.", 720),
  ("Serve", "Squeeze some of the roasted lemon over everything.", 0),
 ], notes="Salmon is higher in fat than the other dinners, but it's mostly omega 3. Pull it when the centre is still slightly translucent; it finishes on the plate.")

recipe(id="greek-chicken-tray-bake", sauce="tzatziki", title="Greek Chicken Tray Bake", category="dinner", short="Greek chicken tray bake",
 desc="Lemon, garlic and oregano chicken thighs roasted with potatoes, capsicum and red onion, finished with feta.",
 tags=["chicken", "tray bake", "greek"], time=50, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "220 g raw chicken, 250 g potatoes, half the veg, 30 g feta", "P": "140 g raw chicken, 150 g potatoes, half the veg, 20 g feta"},
 ingredients=[
  ("chicken thigh fillet, skinless", 360, "g", {"per": {"J": 220, "P": 140}}),
  ("baby potatoes", 400, "g", {"per": {"J": 250, "P": 150}, "label": "baby potatoes, halved"}),
  ("red capsicum", 1, "whole", {"share": 1, "label": "red capsicum, in chunks"}), ("red onion", 1, "whole", {"share": 1, "label": "red onion, in wedges"}),
  ("olive oil", 1, "tbsp", {"share": 1}), ("lemon", 1, "whole", {"share": 1, "label": "lemon, juiced"}),
  ("garlic", 3, "clove", {"share": 1}), ("dried oregano", 2, "tsp", {"share": 1}),
  ("light feta", 50, "g", {"per": {"J": 30, "P": 20}, "label": "light feta, crumbled"}),
 ],
 steps=[
  ("Mix the marinade", "Oven to 220°C (200°C fan). Whisk the oil, lemon juice, crushed garlic, oregano, salt and pepper.", 0),
  ("Potatoes first", "Toss the potatoes in a third of the marinade on a big lined tray and roast.", 900),
  ("Everything else", "Toss the chicken, capsicum and onion in the rest of the marinade and add to the tray in a single layer. Roast until the chicken is golden and cooked through.", 1500),
  ("Feta and serve", "Crumble the feta over and give it 2 more minutes. Serve with tzatziki.", 120),
 ], notes="Use two trays if it's crowded; crowded trays steam instead of roast.")

recipe(id="butter-chicken-light", title="Lighter Butter Chicken", category="dinner", short="Lighter butter chicken, rice",
 desc="Butter chicken made with Greek yoghurt instead of cream. Makes two nights' worth, or dinner plus lunch.",
 tags=["chicken", "curry", "freezer"], time=45, base={"J": 2, "P": 2}, share=0.65,
 portions={"J": "A quarter of the curry (about 1.5 cups), a cup of cooked rice", "P": "About 1 cup of curry, 2/3 cup cooked rice"},
 ingredients=[
  ("chicken thigh fillet, skinless", 660, "g", {"per": {"J": 200, "P": 130}, "label": "chicken thigh, diced"}),
  ("high-protein Greek yoghurt", 270, "g", {"label": "Greek yoghurt (100 g to marinate, 170 g for the sauce)"}),
  ("garam masala", 3, "tsp"), ("smoked paprika", 1, "tsp"), ("ground cumin", 1, "tsp"),
  ("brown onion", 1, "whole", {"label": "brown onion, finely diced"}), ("garlic", 4, "clove"), ("fresh ginger, grated", 1, "tbsp"),
  ("butter", 15, "g"), ("tomato paste", 2, "tbsp"), ("passata", 400, "g"),
  ("fresh herbs (dill, mint, parsley or chives)", 2, "tbsp", {"label": "fresh coriander, to serve"}),
  ("white rice, uncooked", 2 * (RICE_J + RICE_P), "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "basmati rice"}),
 ],
 steps=[
  ("Marinate the chicken", "Mix the chicken with 100 g of the yoghurt, 1 tsp garam masala, the paprika and a pinch of salt. Leave 20 minutes, or overnight.", 1200),
  ("Rice on", "Rinse and cook the rice.", 900),
  ("Sear the chicken", "Hot non-stick pan, a little spray oil if needed. Sear the chicken in batches until browned on the outside (it finishes in the sauce). Set aside.", 480),
  ("Build the sauce", "Lower the heat. Melt the butter, cook the onion until soft, then the garlic, ginger, cumin and remaining garam masala for a minute. Stir in the tomato paste, then the passata.", 600),
  ("Simmer", "Return the chicken and simmer gently until cooked through and the sauce thickens.", 600),
  ("Finish with yoghurt", "Take it off the heat and let it cool for a minute, then stir in the remaining yoghurt (off the heat stops it splitting). Season and top with coriander.", 0),
 ], notes="Leftovers keep 3 days or freeze well. Reheat gently and don't boil it, or the yoghurt splits.")
