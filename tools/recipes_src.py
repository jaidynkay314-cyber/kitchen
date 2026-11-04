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
  ("butter", 10, "g", {"share": 1}), ("milk, trim", 2, "tbsp", {"share": 1}),
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
 desc="Freezer-friendly fried rice. Best as a pre-gym lunch: lower in fat.",
 tags=["chicken", "freezer", "rice"], time=40, base={"J": 4, "P": 3}, share=2/3,
 portions={"J": "1 regular container (a sixth of the batch)", "P": "2/3 of a regular container"},
 ingredients=[
  ("chicken breast", 1000, "g", {"label": "chicken breast, diced small"}), ("brown rice, uncooked", 2, "cup", {"label": "brown rice (cook the day before)"}),
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
  ("brown rice, uncooked", 1.5, "cup"),
 ],
 steps=[
  ("Brown the mince", "Brown the mince in a large pot over medium-high heat, breaking it up. No extra oil needed.", 600),
  ("Soften the veg", "Add the onion, capsicum and garlic and cook 4 to 5 minutes.", 300),
  ("Bloom the spices", "Stir in all the spices and cook 1 minute until fragrant.", 60),
  ("Simmer", "Add the tomatoes and beans and simmer uncovered until thick, stirring now and then.", 1500),
  ("Cook the rice", "Cook the rice separately. Season the chilli and add your hot sauce. Brown rice takes about 30 minutes.", 1800),
  ("Portion", "Weigh the chilli and divide by 6 for one regular serve. Pack 4 regular (3/4 cup rice) and 3 small (2/3 chilli, 1/2 cup rice).", 0),
 ], notes="The batch makes exactly 4 regular and 3 small serves.")

recipe(id="chicken-burritos", sauce="chipotle-lime-yoghurt", title="Chicken Burritos", category="lunch prep",
 desc="Grab-and-go freezer burritos for hungrier days.",
 tags=["chicken", "freezer", "grab and go"], time=45, base={"J": 4, "P": 3}, share=2/3,
 portions={"J": "1 large burrito", "P": "1 burrito on a regular tortilla with 2/3 of the filling"},
 ingredients=[
  ("chicken breast", 1000, "g"), ("brown rice, uncooked", 1.5, "cup"), ("black beans, tinned (drained)", 1, "tin", {"label": "black beans, drained and rinsed"}),
  ("cheddar, grated", 120, "g", {"label": "grated cheese"}),
  ("large tortillas", 4, "whole", {"per": {"J": 1, "P": 0}}), ("regular tortillas", 3, "whole", {"per": {"J": 0, "P": 1}}),
  ("salsa", 0.5, "cup"), ("ground cumin", 2, "tsp"), ("smoked paprika", 2, "tsp"), ("chipotle powder", 1, "tsp"), ("lime", 1, "whole", {"label": "lime (optional)"}),
 ],
 steps=[
  ("Cook the chicken", "Rub the chicken with the spices and bake at 200°C until cooked through. Rest 5 minutes, then shred with two forks.", 1350),
  ("Cook the rice", "Cook the rice and stir through the lime juice and a pinch of salt. Brown rice takes about 30 minutes.", 1800),
  ("Mix the filling", "Toss the chicken with the beans, salsa and hot sauce. Let everything cool before rolling.", 0),
  ("Roll", "Large tortillas: rice, chicken mix, cheese. Regular tortillas: about 2/3 as much of each. Fold the sides in and roll tightly.", 0),
  ("Wrap and freeze", "Wrap each one in cling wrap or foil, then bag and freeze.", 0),
 ], notes="Microwave from frozen 3 to 4 minutes (foil off), turning halfway.")

recipe(id="friday-chicken-veg-bowl", sauce="lemon-tahini-yoghurt", title="Lean Chicken and Veg Bowl", category="friday",
 desc="Light, high-protein freezer lunch for Fridays before beers.",
 tags=["chicken", "freezer", "low calorie"], time=35, base={"J": 6, "P": 0}, share=2/3,
 portions={"J": "1 container (a sixth of the batch)", "P": "2/3 of a container"},
 ingredients=[
  ("chicken breast", 1100, "g", {"label": "chicken breast, diced"}), ("frozen mixed veg", 900, "g"), ("brown rice, uncooked", 125, "g", {"label": "brown rice (about 2/3 cup)"}),
  ("soy sauce", 3, "tbsp"), ("sweet chilli sauce", 2, "tbsp"), ("garlic", 2, "clove"), ("fresh ginger, grated", 1, "tsp"),
 ],
 steps=[
  ("Cook the rice", "Cook the rice and spread it on a tray to cool. Brown rice takes about 30 minutes.", 1800),
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
  ("wholemeal English muffins", 12, "whole", {"label": "wholemeal or wholegrain English muffins"}), ("lean pork and beef mince (50/50)", 1440, "g", {"per": {"J": 160, "P": 80}, "label": "pork and beef mince (80 g patties)"}),
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
  ("milk, trim", 2, "tbsp", {"share": 1, "label": "trim milk, for the mash"}),
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
  ("brown rice, uncooked", RICE_J + RICE_P, "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "brown rice"}),
  ("coleslaw mix", 200, "g", {"per": {"J": 120, "P": 80}}), ("spring onions", 2, "whole", {"share": 1, "label": "spring onions, sliced"}),
  ("lime juice", 1, "tbsp", {"share": 1, "label": "lime juice, for the slaw"}),
 ],
 steps=[
  ("Marinate", "Mix the soy, honey, garlic, ginger and sesame oil. Toss the chicken through and leave 20 minutes (or overnight). If using bamboo skewers, soak them now.", 1200),
  ("Cook the rice", "Rinse the rice and cook it (absorption or rice cooker). Brown rice takes about 30 minutes.", 1800),
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
  ("brown rice, uncooked", 0.25 + 0.17, "cup", {"per": {"J": 0.25, "P": 0.17}, "label": "brown rice"}),
 ],
 steps=[
  ("Rice and lettuce", "Put the rice on. Separate the lettuce into whole cup-shaped leaves, rinse, and chill them in the fridge so they're crisp. Brown rice takes about 30 minutes.", 1800),
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
  ("brown rice, uncooked", 2 * (RICE_J + RICE_P), "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "brown rice"}),
 ],
 steps=[
  ("Marinate the chicken", "Mix the chicken with 100 g of the yoghurt, 1 tsp garam masala, the paprika and a pinch of salt. Leave 20 minutes, or overnight.", 1200),
  ("Rice on", "Rinse and cook the rice. Brown rice takes about 30 minutes.", 1800),
  ("Sear the chicken", "Hot non-stick pan, a little spray oil if needed. Sear the chicken in batches until browned on the outside (it finishes in the sauce). Set aside.", 480),
  ("Build the sauce", "Lower the heat. Melt the butter, cook the onion until soft, then the garlic, ginger, cumin and remaining garam masala for a minute. Stir in the tomato paste, then the passata.", 600),
  ("Simmer", "Return the chicken and simmer gently until cooked through and the sauce thickens.", 600),
  ("Finish with yoghurt", "Take it off the heat and let it cool for a minute, then stir in the remaining yoghurt (off the heat stops it splitting). Season and top with coriander.", 0),
 ], notes="Leftovers keep 3 days or freeze well. Reheat gently and don't boil it, or the yoghurt splits.")

# ---- Batch 3 dinners (picked 2 Nov 2026) ----
recipe(id="korean-beef-bowl", title="Korean Beef Bowl", category="dinner", short="Korean beef bowl",
 desc="Sweet, spicy gochujang beef mince over rice with quick-pickled cucumber and a fried egg.",
 tags=["beef", "asian", "quick"], time=25, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "200 g raw mince, a cup of cooked rice, 1 egg, half the cucumber", "P": "130 g raw mince, 2/3 cup cooked rice, 1 egg, half the cucumber"},
 ingredients=[
  ("lean beef mince (5% fat)", 330, "g", {"per": {"J": 200, "P": 130}}),
  ("gochujang", 1.5, "tbsp", {"share": 1}), ("soy sauce", 1, "tbsp", {"share": 1, "label": "soy sauce (salt-reduced)"}), ("honey", 2, "tsp", {"share": 1}),
  ("garlic", 2, "clove", {"share": 1}), ("fresh ginger, grated", 1, "tsp", {"share": 1}), ("sesame oil", 1, "tsp", {"share": 1}),
  ("brown rice, uncooked", RICE_J + RICE_P, "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "brown rice"}),
  ("Lebanese cucumber", 1, "whole", {"share": 1, "label": "Lebanese cucumber, thinly sliced"}), ("rice vinegar", 2, "tbsp", {"share": 1}),
  ("eggs", 2, "whole", {"share": 1}), ("spring onions", 2, "whole", {"share": 1, "label": "spring onions, sliced"}),
 ],
 steps=[
  ("Rice and pickles", "Put the rice on. Toss the cucumber with the rice vinegar and a pinch each of salt and sugar. Leave it to pickle while you cook. Brown rice takes about 30 minutes.", 1800),
  ("Mix the sauce", "Stir together the gochujang, soy, honey, garlic and ginger.", 0),
  ("Cook the beef", "Hot pan, high heat. Brown the mince well, breaking it up, until any liquid cooks off and it starts to crisp.", 420),
  ("Sauce the beef", "Add the sauce and toss for a minute until sticky. Finish with the sesame oil.", 60),
  ("Fry the eggs", "Wipe the pan, a little spray oil, and fry the eggs to your liking.", 180),
  ("Bowl up", "Rice, beef, drained cucumber, egg on top, spring onion over everything.", 0),
 ], notes="Gochujang is in the Asian aisle at Woolies. It varies in heat by brand, so start with 1 tbsp.")

recipe(id="satay-chicken", title="Satay Chicken with Rice and Greens", category="dinner", short="Satay chicken, rice, greens",
 desc="Chicken breast in a light peanut and coconut satay sauce, with rice and steamed bok choy.",
 tags=["chicken", "asian"], time=30, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "220 g raw chicken with half the sauce, a cup of cooked rice, half the greens", "P": "140 g raw chicken with a bit less sauce, 2/3 cup cooked rice, half the greens"},
 ingredients=[
  ("chicken breast", 360, "g", {"per": {"J": 220, "P": 140}, "label": "chicken breast, sliced"}),
  ("peanut butter", 2, "tbsp", {"label": "smooth peanut butter"}), ("light coconut milk", 125, "ml"),
  ("soy sauce", 1, "tbsp", {"label": "soy sauce (salt-reduced)"}), ("lime juice", 1, "tbsp"), ("honey", 1, "tsp"), ("garlic", 1, "clove"),
  ("brown rice, uncooked", RICE_J + RICE_P, "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "brown rice"}),
  ("bok choy", 3, "whole", {"share": 1, "label": "baby bok choy, halved"}),
 ],
 steps=[
  ("Rice on", "Rinse and cook the rice. Brown rice takes about 30 minutes.", 1800),
  ("Make the satay", "Whisk the peanut butter, coconut milk, soy, lime juice, honey and grated garlic until smooth.", 0),
  ("Cook the chicken", "Hot non-stick pan with a little spray oil. Cook the chicken until golden and just cooked through.", 360),
  ("Sauce it", "Pour in the satay and simmer a minute or two until it coats the chicken. Loosen with a splash of water if it's thick.", 120),
  ("Greens and serve", "Steam or microwave the bok choy for 2 to 3 minutes. Serve the chicken over rice with the greens.", 180),
 ], notes="Most of the calories here are in the peanut butter. It's measured, not scooped.")

recipe(id="thai-basil-chicken", title="Thai Basil Chicken (Pad Kra Pao)", category="dinner", short="Thai basil chicken, rice, egg",
 desc="Fast, fiery chicken mince with garlic, chilli, green beans and basil over rice, with a crispy fried egg.",
 tags=["chicken", "thai", "quick"], time=20, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "220 g raw mince, a cup of cooked rice, 1 egg", "P": "140 g raw mince, 2/3 cup cooked rice, 1 egg"},
 ingredients=[
  ("chicken mince", 360, "g", {"per": {"J": 220, "P": 140}}),
  ("garlic", 4, "clove", {"share": 1}), ("fresh chilli", 2, "whole", {"share": 1, "label": "red chillies (bird's eye if you like it hot)"}),
  ("green beans", 150, "g", {"share": 1, "label": "green beans, in short pieces"}),
  ("oyster sauce", 1.5, "tbsp", {"share": 1}), ("soy sauce", 1, "tbsp", {"share": 1, "label": "soy sauce (salt-reduced)"}),
  ("fish sauce", 2, "tsp", {"share": 1}), ("honey", 1, "tsp", {"share": 1, "label": "honey or sugar"}),
  ("fresh herbs (dill, mint, parsley or chives)", 4, "tbsp", {"share": 1, "label": "Thai basil (or regular basil), a big handful"}),
  ("olive oil", 2, "tsp", {"share": 1, "label": "oil"}), ("eggs", 2, "whole", {"share": 1}),
  ("brown rice, uncooked", RICE_J + RICE_P, "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "brown rice"}),
 ],
 steps=[
  ("Rice on, prep", "Cook the rice. Pound or finely chop the garlic and chilli together. Mix the oyster, soy, fish sauce and honey. Brown rice takes about 30 minutes.", 1800),
  ("Fry the eggs", "Heat the oil in a wok until very hot and fry the eggs until the edges are crispy. Set aside.", 120),
  ("Garlic, chilli, chicken", "Same wok, high heat. Fry the garlic and chilli 20 seconds, add the mince and cook, breaking it up, until browned.", 300),
  ("Beans and sauce", "Add the beans and sauce and toss 2 minutes until the beans are just tender.", 120),
  ("Basil and serve", "Off the heat, stir through the basil until wilted. Serve over rice with the egg on top.", 0),
 ], notes="This one is meant to be hot. Seed the chillies or use one for a milder version.")

recipe(id="garlic-chilli-prawn-linguine", title="Garlic Chilli Prawn Linguine", category="dinner", short="Garlic chilli prawn linguine",
 desc="Prawns, garlic, chilli, cherry tomatoes and lemon through linguine. Light on the oil, big on flavour.",
 tags=["seafood", "pasta", "quick"], time=25, base={"J": 1, "P": 1}, share=0.65,
 portions={"J": "200 g raw prawns, 100 g dry pasta (about 2 cups cooked)", "P": "130 g raw prawns, 65 g dry pasta (about 1.3 cups cooked)"},
 ingredients=[
  ("raw prawns, peeled", 330, "g", {"per": {"J": 200, "P": 130}}),
  ("linguine, dry", 165, "g", {"per": {"J": 100, "P": 65}, "label": "linguine"}),
  ("olive oil", 1, "tbsp", {"share": 1}), ("garlic", 4, "clove", {"share": 1, "label": "garlic, thinly sliced"}),
  ("spices (your mix)", 1, "tsp", {"share": 1, "label": "chilli flakes (to taste)"}),
  ("cherry tomatoes", 250, "g", {"share": 1, "label": "cherry tomatoes, halved"}), ("lemon", 1, "whole", {"share": 1, "label": "lemon, zested and juiced"}),
  ("baby spinach", 60, "g", {"share": 1}), ("parmesan, grated", 20, "g", {"per": {"J": 12, "P": 8}}),
  ("fresh herbs (dill, mint, parsley or chives)", 2, "tbsp", {"share": 1, "label": "parsley, chopped"}),
 ],
 steps=[
  ("Pasta on", "Cook the linguine in well-salted water. Save a mug of pasta water before draining.", 600),
  ("Garlic and chilli", "Meanwhile, warm the oil in a big pan on medium. Add the garlic and chilli and cook gently until the garlic is just golden.", 120),
  ("Tomatoes", "Turn up the heat, add the tomatoes and cook until they start to burst.", 180),
  ("Prawns", "Add the prawns and cook until pink and curled, about 2 minutes. Don't overcook them.", 120),
  ("Toss it all", "Add the drained pasta, spinach, lemon zest and juice and a good splash of pasta water. Toss until glossy and the spinach wilts. Top with parmesan and parsley.", 0),
 ], notes="The pasta water does the job extra oil would do. Use it.")

# ---- Batch 4 dinners (picked 2 Nov 2026) ----
recipe(id="chimichurri-steak", title="Chimichurri Steak with Corn and Charred Capsicum Salad", category="dinner", short="Chimichurri steak, corn, salad",
 desc="Barbecued rump with a bright, light-on-oil chimichurri, corn on the cob and a charred capsicum and rocket salad.",
 tags=["beef", "bbq", "high protein"], time=35, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "250 g raw rump (about 190 g cooked), 1 cob of corn, half the salad", "P": "150 g raw rump (about 115 g cooked), 1 cob of corn, half the salad"},
 ingredients=[
  ("lean rump steak", 400, "g", {"per": {"J": 250, "P": 150}, "label": "rump steak, fat trimmed"}),
  ("corn cob", 2, "whole", {"share": 1}),
  ("red capsicum", 2, "whole", {"share": 1, "label": "capsicums, quartered"}), ("red onion", 0.5, "whole", {"share": 1, "label": "red onion, thinly sliced"}),
  ("rocket", 60, "g", {"share": 1}),
  ("fresh herbs (dill, mint, parsley or chives)", 8, "tbsp", {"share": 1, "label": "flat-leaf parsley, a big bunch, finely chopped"}),
  ("olive oil", 1, "tbsp", {"share": 1}), ("red wine vinegar", 2, "tbsp", {"share": 1}), ("garlic", 2, "clove", {"share": 1}),
  ("dried oregano", 1, "tsp", {"share": 1}), ("spices (your mix)", 0.5, "tsp", {"share": 1, "label": "chilli flakes"}),
 ],
 steps=[
  ("Make the chimichurri", "Mix the parsley, oil, vinegar, crushed garlic, oregano, chilli flakes, salt and 2 tbsp water. It's better after 15 minutes.", 900),
  ("Steak out", "Take the steak out to come up to room temperature. Pat dry and season well.", 0),
  ("Grill the veg", "Hot barbecue. Grill the corn, turning, until charred in spots, and the capsicum until blistered and soft.", 600),
  ("Grill the steak", "Cook the rump on the hottest part, 3 to 4 minutes a side for medium rare depending on thickness.", 420),
  ("Rest and salad", "Rest the steak 5 minutes. Slice the capsicum and toss with the onion, rocket and a spoon of the chimichurri.", 300),
  ("Serve", "Slice the steak across the grain and spoon chimichurri over the top. Corn and salad on the side.", 0),
 ], notes="Rump is lean and full of flavour, but it can be chewy: slice thin and across the grain.")

recipe(id="tandoori-chicken", sauce="tzatziki", title="Tandoori Chicken with Cucumber Salad and Naan", category="dinner", short="Tandoori chicken, salad, naan",
 desc="Yoghurt-marinated tandoori chicken thighs off the barbecue, with a crunchy cucumber and onion salad and a mini naan.",
 tags=["chicken", "bbq", "indian"], time=40, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "220 g raw chicken, 1 mini naan, half the salad", "P": "140 g raw chicken, 1 mini naan, half the salad"},
 ingredients=[
  ("chicken thigh fillet, skinless", 360, "g", {"per": {"J": 220, "P": 140}}),
  ("high-protein Greek yoghurt", 100, "g", {"share": 1, "label": "Greek yoghurt, for the marinade"}),
  ("garam masala", 2, "tsp", {"share": 1}), ("smoked paprika", 2, "tsp", {"share": 1}), ("ground cumin", 1, "tsp", {"share": 1}),
  ("spices (your mix)", 1, "tsp", {"share": 1, "label": "chilli powder and turmeric, to taste"}),
  ("lemon juice", 1, "tbsp", {"share": 1}), ("garlic", 2, "clove", {"share": 1}), ("fresh ginger, grated", 1, "tsp", {"share": 1}),
  ("Lebanese cucumber", 1, "whole", {"share": 1, "label": "Lebanese cucumber, diced"}), ("red onion", 0.5, "whole", {"share": 1, "label": "red onion, finely sliced"}),
  ("fresh herbs (dill, mint, parsley or chives)", 2, "tbsp", {"share": 1, "label": "fresh mint or coriander"}),
  ("mini naan", 2, "whole", {"share": 1}),
 ],
 steps=[
  ("Marinate", "Mix the yoghurt, spices, lemon juice, garlic, ginger and salt. Slash the chicken a few times and coat well. At least 30 minutes, ideally overnight.", 1800),
  ("Salad", "Toss the cucumber, onion and mint with a squeeze of lemon and a pinch of salt.", 0),
  ("Grill", "Hot barbecue. Cook the chicken until charred at the edges and cooked through, about 5 to 6 minutes a side.", 660),
  ("Naan and serve", "Warm the naan on the barbecue for the last minute. Serve with the salad and tzatziki.", 60),
 ], notes="The yoghurt marinade is what keeps the thighs so tender. Don't skip the slashes.")

recipe(id="thai-green-chicken-curry", title="Thai Green Chicken Curry", category="dinner", short="Thai green chicken curry, rice",
 desc="Green curry with chicken, zucchini, capsicum and snow peas, made with light coconut milk.",
 tags=["chicken", "thai", "curry"], time=30, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "200 g raw chicken and a generous ladle of curry, a cup of cooked rice", "P": "130 g raw chicken and a smaller ladle, 2/3 cup cooked rice"},
 ingredients=[
  ("chicken thigh fillet, skinless", 330, "g", {"per": {"J": 200, "P": 130}, "label": "chicken thigh, sliced"}),
  ("green curry paste", 2, "tbsp"), ("light coconut milk", 270, "ml", {"label": "light coconut milk (a small tin)"}),
  ("zucchini", 1, "whole", {"label": "zucchini, sliced"}), ("red capsicum", 1, "whole", {"label": "red capsicum, sliced"}), ("snow peas", 100, "g"),
  ("fish sauce", 2, "tsp"), ("honey", 1, "tsp", {"label": "honey or brown sugar"}), ("lime juice", 1, "tbsp"),
  ("fresh herbs (dill, mint, parsley or chives)", 3, "tbsp", {"share": 1, "label": "Thai basil or coriander"}),
  ("brown rice, uncooked", RICE_J + RICE_P, "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "brown rice"}),
 ],
 steps=[
  ("Rice on", "Rinse and cook the rice. Brown rice takes about 30 minutes.", 1800),
  ("Fry the paste", "In a deep pan or wok on medium, fry the curry paste with a splash of the coconut milk until fragrant.", 120),
  ("Brown the chicken", "Add the chicken and stir until it's coated and sealed.", 180),
  ("Simmer", "Add the rest of the coconut milk, half a cup of water, the zucchini and capsicum. Simmer until the chicken is cooked through.", 480),
  ("Finish", "Add the snow peas for the last 2 minutes. Season with the fish sauce, honey and lime, tasting as you go. Stir through the basil.", 120),
 ], notes="Curry pastes vary a lot in heat. Start with 1.5 tbsp if you're not sure about the brand.")

recipe(id="sweet-and-sour-pork", title="Sweet and Sour Pork", category="dinner", short="Sweet and sour pork, rice",
 desc="A lighter sweet and sour: lean pork fillet, pineapple, capsicum and onion in a glossy sauce. No deep frying.",
 tags=["pork", "asian", "fakeaway"], time=30, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "200 g raw pork, half the veg and sauce, a cup of cooked rice", "P": "130 g raw pork, half the veg and sauce, 2/3 cup cooked rice"},
 ingredients=[
  ("pork fillet", 330, "g", {"per": {"J": 200, "P": 130}, "label": "pork fillet, in bite-size pieces"}),
  ("cornflour", 1, "tbsp", {"share": 1, "label": "cornflour (plus 1 tsp for the sauce)"}),
  ("pineapple pieces in juice, tinned", 1, "tin", {"share": 1, "label": "pineapple pieces in juice (keep the juice)"}),
  ("red capsicum", 1, "whole", {"share": 1, "label": "red capsicum, in chunks"}), ("brown onion", 1, "whole", {"share": 1, "label": "onion, in chunks"}),
  ("tomato sauce", 2, "tbsp", {"share": 1}), ("rice vinegar", 2, "tbsp", {"share": 1}), ("honey", 1, "tbsp", {"share": 1}), ("soy sauce", 1, "tbsp", {"share": 1, "label": "soy sauce (salt-reduced)"}),
  ("olive oil", 2, "tsp", {"share": 1, "label": "oil"}), ("spring onions", 2, "whole", {"share": 1, "label": "spring onions, sliced"}),
  ("brown rice, uncooked", RICE_J + RICE_P, "cup", {"per": {"J": RICE_J, "P": RICE_P}, "label": "brown rice"}),
 ],
 steps=[
  ("Rice on", "Rinse and cook the rice. Brown rice takes about 30 minutes.", 1800),
  ("Mix the sauce", "Whisk the tomato sauce, vinegar, honey, soy, 1 tsp cornflour and the pineapple juice from the tin.", 0),
  ("Coat and sear the pork", "Toss the pork in the cornflour with a pinch of salt. Heat the oil in a wok on high and sear the pork until golden and just cooked. Set aside.", 360),
  ("Veg", "Same wok, stir-fry the onion and capsicum 2 to 3 minutes so they keep some crunch. Add the pineapple.", 180),
  ("Sauce and serve", "Pour in the sauce and bubble until glossy and thick, then toss the pork back through. Serve over rice with spring onion.", 120),
 ], notes="The cornflour coating gives a crisp edge with 2 tsp of oil instead of a deep fryer.")

recipe(id="chicken-caesar-wraps", title="Chicken Caesar Wraps", category="dinner", short="Chicken caesar wraps",
 desc="Grilled chicken, crispy short-cut bacon, cos and parmesan with a creamy Greek yoghurt caesar dressing, rolled in wholemeal wraps.",
 tags=["chicken", "quick", "high protein"], time=25, base={"J": 1, "P": 1}, share=0.6,
 portions={"J": "2 wraps: 200 g raw chicken, 40 g bacon", "P": "1 big wrap: 130 g raw chicken, 20 g bacon"},
 ingredients=[
  ("chicken breast", 330, "g", {"per": {"J": 200, "P": 130}}),
  ("short-cut bacon", 60, "g", {"per": {"J": 40, "P": 20}}),
  ("wholemeal wraps", 3, "whole", {"per": {"J": 2, "P": 1}}),
  ("cos lettuce", 1, "whole", {"share": 1, "label": "cos lettuce, shredded"}),
  ("parmesan, grated", 20, "g", {"per": {"J": 12, "P": 8}}),
  ("high-protein Greek yoghurt", 100, "g", {"share": 1, "label": "Greek yoghurt, for the dressing"}),
  ("lemon juice", 1, "tbsp", {"share": 1}), ("garlic", 1, "clove", {"share": 1, "label": "small garlic clove, grated"}),
  ("wholegrain mustard", 1, "tsp", {"share": 1, "label": "mustard (Dijon or wholegrain)"}),
  ("spices (your mix)", 1, "tsp", {"share": 1, "label": "Spices for the chicken (garlic powder, paprika, pepper)"}),
 ],
 steps=[
  ("Dressing", "Mix the yoghurt, lemon juice, garlic, mustard, half the parmesan, black pepper and a splash of water to make it pourable.", 0),
  ("Cook the chicken", "Flatten the breasts to an even thickness, season with the spices and cook on a hot pan or barbecue, about 4 to 5 minutes a side.", 540),
  ("Crisp the bacon", "Same pan, cook the bacon until crisp, then chop it.", 240),
  ("Assemble", "Rest and slice the chicken. Toss the cos in most of the dressing. Fill the wraps with lettuce, chicken, bacon and the rest of the parmesan, drizzle the last of the dressing and roll tight.", 0),
 ], notes="Leftover chicken makes these a 5-minute lunch the next day.")

recipe(id="haloumi-chicken-salad", sauce="lemon-tahini-yoghurt", title="Haloumi and Chicken Salad with Roast Pumpkin and Quinoa", category="dinner", short="Haloumi chicken salad, pumpkin, quinoa",
 desc="A big warm salad: grilled chicken and light haloumi with roast pumpkin, quinoa, rocket and cherry tomatoes.",
 tags=["chicken", "salad", "high protein"], time=40, base={"J": 1, "P": 1}, share=0.65,
 portions={"J": "180 g raw chicken, 50 g haloumi, 3/4 cup cooked quinoa, half the veg", "P": "120 g raw chicken, 30 g haloumi, 1/2 cup cooked quinoa, half the veg"},
 ingredients=[
  ("chicken breast", 300, "g", {"per": {"J": 180, "P": 120}}),
  ("light haloumi", 80, "g", {"per": {"J": 50, "P": 30}, "label": "light haloumi, sliced"}),
  ("quinoa, uncooked", 0.42, "cup", {"per": {"J": 0.25, "P": 0.17}, "label": "quinoa"}),
  ("butternut pumpkin", 400, "g", {"share": 1, "label": "butternut pumpkin, in 2 cm cubes"}), ("red onion", 1, "whole", {"share": 1, "label": "red onion, in wedges"}),
  ("olive oil", 1, "tbsp", {"share": 1}), ("spices (your mix)", 1, "tsp", {"share": 1, "label": "Spices (cumin, smoked paprika)"}),
  ("rocket", 80, "g", {"share": 1}), ("cherry tomatoes", 150, "g", {"share": 1, "label": "cherry tomatoes, halved"}),
  ("lemon juice", 1, "tbsp", {"share": 1}),
 ],
 steps=[
  ("Roast the pumpkin", "Oven to 220°C (200°C fan). Toss the pumpkin and onion with half the oil, the spices and salt, and roast until golden.", 1500),
  ("Quinoa", "Rinse the quinoa and simmer in twice its volume of water until the water's absorbed. Fluff and cool a little.", 900),
  ("Chicken", "Season the chicken and cook on a hot pan or barbecue, about 4 to 5 minutes a side. Rest and slice.", 540),
  ("Haloumi", "Same pan, dry, cook the haloumi until golden on both sides. It goes squeaky and rubbery if it cools, so do it last.", 180),
  ("Toss and serve", "Toss the rocket, tomatoes, quinoa and pumpkin with the lemon juice and the rest of the oil. Top with the chicken and haloumi.", 0),
 ], notes="Leftover roast pumpkin and quinoa make this a quick work lunch.")

# ---- Batch 5 dinners (picked 2 Nov 2026) ----
recipe(id="bbq-pulled-chicken", title="Smoky BBQ Pulled Chicken Sliders", category="dinner", short="BBQ pulled chicken sliders",
 desc="Slow cooker pulled chicken thighs in smoky barbecue sauce, in slider buns with a yoghurt slaw. Makes two nights' worth.",
 tags=["chicken", "slow cooker", "fakeaway"], time=20, base={"J": 2, "P": 2}, share=0.6,
 portions={"J": "2 sliders loaded with 250 g raw chicken (about 190 g pulled), plus slaw", "P": "1 slider plus a bowl of chicken and slaw: 150 g raw chicken"},
 ingredients=[
  ("chicken thigh fillet, skinless", 800, "g"),
  ("BBQ sauce", 4, "tbsp"), ("smoked paprika", 2, "tsp", {"share": 1}), ("garlic", 2, "clove", {"share": 1}),
  ("brown onion", 1, "whole", {"share": 1, "label": "brown onion, sliced"}), ("red wine vinegar", 1, "tbsp", {"share": 1, "label": "vinegar (apple cider or red wine)"}),
  ("slider buns", 6, "whole", {"per": {"J": 2, "P": 1}}),
  ("coleslaw mix", 300, "g", {"share": 1}), ("high-protein Greek yoghurt", 60, "g", {"share": 1, "label": "Greek yoghurt, for the slaw"}),
 ],
 steps=[
  ("Into the slow cooker", "Onion on the bottom, chicken on top. Mix the BBQ sauce, paprika, garlic, vinegar and a pinch of salt and pour over. No extra liquid.", 0),
  ("Cook", "Low for 6 hours or high for 3 to 4, until it falls apart.", 0),
  ("Pull", "Shred the chicken with two forks right in the sauce and stir it through. Taste and add a splash more BBQ sauce if you like.", 0),
  ("Slaw", "Toss the slaw mix with the yoghurt, a squeeze of lemon, salt and pepper.", 0),
  ("Serve", "Warm the buns and load them up with chicken and slaw.", 0),
 ], notes="Half the batch is the next night (or lunches). Lettuce cups instead of buns save about 110 kcal each.")

recipe(id="teriyaki-chicken-burgers", sauce="sriracha-lime-yoghurt", title="Teriyaki Chicken Burgers", category="dinner", short="Teriyaki chicken burgers",
 desc="Grilled teriyaki chicken thigh fillets with charred pineapple and crunchy Asian slaw in a soft bun.",
 tags=["chicken", "bbq", "fakeaway"], time=30, base={"J": 1, "P": 1}, share=0.65,
 portions={"J": "1 burger with 2 thigh fillets (about 180 g raw)", "P": "1 burger with 1 large thigh fillet (about 120 g raw)"},
 ingredients=[
  ("chicken thigh fillet, skinless", 300, "g", {"per": {"J": 180, "P": 120}}),
  ("teriyaki sauce", 3, "tbsp", {"share": 1}),
  ("pineapple pieces in juice, tinned", 0.5, "tin", {"share": 1, "label": "pineapple rings or pieces in juice"}),
  ("burger buns", 2, "whole", {"share": 1}),
  ("coleslaw mix", 120, "g", {"per": {"J": 70, "P": 50}}), ("lime juice", 2, "tsp", {"share": 1, "label": "lime juice, for the slaw"}),
  ("sesame oil", 0.5, "tsp", {"share": 1}),
 ],
 steps=[
  ("Marinate", "Flatten the thighs a little and toss in 2 tbsp of the teriyaki. 15 minutes is enough.", 900),
  ("Slaw", "Toss the slaw mix with the lime juice, sesame oil and a pinch of salt.", 0),
  ("Grill", "Medium-high barbecue. Cook the chicken about 5 minutes a side, brushing with the last of the teriyaki in the final minute. Grill the pineapple until charred.", 600),
  ("Build", "Toast the buns. Chicken, pineapple, slaw and sauce.", 0),
 ])

recipe(id="chicken-pesto-pasta", title="Chicken Pesto Pasta", category="dinner", short="Chicken pesto pasta",
 desc="Chicken, light basil pesto, cherry tomatoes and spinach through pasta. A 20-minute weeknight.",
 tags=["chicken", "pasta", "quick"], time=20, base={"J": 1, "P": 1}, share=0.67,
 portions={"J": "180 g raw chicken, 90 g dry pasta (about 2 cups cooked)", "P": "120 g raw chicken, 60 g dry pasta (about 1.3 cups cooked)"},
 ingredients=[
  ("chicken breast", 300, "g", {"per": {"J": 180, "P": 120}, "label": "chicken breast, sliced"}),
  ("pasta, dry", 150, "g", {"per": {"J": 90, "P": 60}, "label": "pasta (penne or spirals)"}),
  ("light basil pesto", 3, "tbsp"), ("cherry tomatoes", 200, "g", {"share": 1, "label": "cherry tomatoes, halved"}),
  ("baby spinach", 60, "g", {"share": 1}), ("garlic", 1, "clove", {"share": 1}),
  ("parmesan, grated", 15, "g", {"per": {"J": 9, "P": 6}}),
 ],
 steps=[
  ("Pasta on", "Cook the pasta in well-salted water. Save a mug of pasta water.", 600),
  ("Chicken", "Season and cook the chicken in a hot non-stick pan until golden and cooked through. Set aside.", 360),
  ("Tomatoes and garlic", "Same pan, cook the tomatoes and garlic until the tomatoes just soften.", 120),
  ("Toss", "Off the heat, add the drained pasta, chicken, pesto, spinach and a splash of pasta water. Toss until glossy and the spinach wilts. Top with parmesan.", 0),
 ], notes="Pesto on a hot pan goes dark and bitter. Off the heat keeps it bright.")

recipe(id="singapore-noodles", title="Singapore Noodles", category="dinner", short="Singapore noodles",
 desc="Curried rice vermicelli stir-fried with prawns, chicken, egg, capsicum and spring onion.",
 tags=["seafood", "chicken", "asian", "fakeaway"], time=30, base={"J": 1, "P": 1}, share=0.65,
 portions={"J": "80 g dry noodles, 100 g prawns, 100 g chicken, 1 egg", "P": "55 g dry noodles, 65 g prawns, 65 g chicken, 1 egg"},
 ingredients=[
  ("rice vermicelli, dry", 135, "g", {"per": {"J": 80, "P": 55}, "label": "rice vermicelli"}),
  ("raw prawns, peeled", 165, "g", {"per": {"J": 100, "P": 65}}), ("chicken breast", 165, "g", {"per": {"J": 100, "P": 65}, "label": "chicken breast, thinly sliced"}),
  ("eggs", 2, "whole", {"share": 1}), ("red capsicum", 1, "whole", {"share": 1, "label": "red capsicum, thinly sliced"}),
  ("spring onions", 3, "whole", {"share": 1, "label": "spring onions, in 4 cm lengths"}), ("garlic", 2, "clove", {"share": 1}),
  ("curry powder", 2, "tsp", {"share": 1}), ("soy sauce", 2, "tbsp", {"share": 1, "label": "soy sauce (salt-reduced)"}), ("oyster sauce", 1, "tbsp", {"share": 1}),
  ("sesame oil", 1, "tsp", {"share": 1}), ("olive oil", 2, "tsp", {"share": 1, "label": "oil"}),
 ],
 steps=[
  ("Soak the noodles", "Cover the vermicelli with boiling water for 3 to 4 minutes, drain, rinse cold and snip into shorter lengths with scissors.", 240),
  ("Egg", "Hot wok, a drop of the oil. Scramble the eggs into a thin omelette, roll it up and slice. Set aside.", 120),
  ("Chicken and prawns", "Add the rest of the oil, cook the chicken until nearly done, then the prawns until pink. Set aside.", 300),
  ("Veg and spice", "Stir-fry the capsicum, garlic and spring onion 1 minute, then add the curry powder for 30 seconds.", 90),
  ("Toss it together", "Add the noodles, soy, oyster sauce, sesame oil and a splash of water and toss until evenly yellow. Return the chicken, prawns and egg and toss through.", 120),
 ], notes="Tongs are your friend here: lift and toss rather than stir, or the noodles clump.")

recipe(id="loaded-sweet-potatoes", sauce="chipotle-lime-yoghurt", title="Loaded Sweet Potatoes with Chilli Beef", category="dinner", short="Loaded sweet potatoes, chilli beef",
 desc="Baked sweet potatoes split and loaded with a quick chilli beef and bean mince, cheese and spring onion.",
 tags=["beef", "mexican", "high protein"], time=50, base={"J": 1, "P": 1}, share=0.65,
 portions={"J": "1 large sweet potato (350 g), 180 g raw mince worth of chilli, 18 g cheese", "P": "1 medium sweet potato (250 g), 120 g raw mince worth of chilli, 12 g cheese"},
 ingredients=[
  ("sweet potato", 600, "g", {"per": {"J": 350, "P": 250}, "label": "sweet potatoes, 1 each, scrubbed"}),
  ("lean beef mince (5% fat)", 300, "g", {"per": {"J": 180, "P": 120}}),
  ("brown onion", 0.5, "whole", {"share": 1, "label": "onion, diced"}), ("garlic", 2, "clove", {"share": 1}),
  ("spices (your mix)", 2, "tsp", {"share": 1, "label": "Chilli spices (cumin, smoked paprika, chipotle or chilli)"}),
  ("kidney beans, tinned (drained)", 0.5, "tin", {"label": "kidney beans, drained (half a tin)"}), ("diced tomatoes, tinned", 0.5, "tin", {"share": 1, "label": "diced tomatoes (half a tin)"}),
  ("reduced-fat cheese, grated", 30, "g", {"per": {"J": 18, "P": 12}}), ("spring onions", 2, "whole", {"share": 1, "label": "spring onions, sliced"}),
 ],
 steps=[
  ("Bake the sweet potatoes", "Oven to 200°C (180°C fan). Prick the sweet potatoes all over and bake on a tray until completely soft. (Or microwave 8 to 10 minutes, then 10 minutes in the oven to crisp the skin.)", 2700),
  ("Brown the mince", "Hot pan, brown the mince with the onion until any liquid cooks off.", 420),
  ("Chilli", "Add the garlic and spices for a minute, then the beans and tomatoes. Simmer until thick.", 600),
  ("Load and serve", "Split the sweet potatoes, fluff the insides with a fork, pile in the chilli, then cheese and spring onion.", 0),
 ], notes="The chilli doubles easily and freezes, for an even faster version next time.")

recipe(id="chicken-gyros", sauce="tzatziki", title="Chicken Gyros", category="dinner", short="Chicken gyros",
 desc="Garlic, lemon and oregano chicken thighs, sliced and wrapped in warm pita with tomato, onion, lettuce and tzatziki.",
 tags=["chicken", "greek", "fakeaway"], time=35, base={"J": 1, "P": 1}, share=0.65,
 portions={"J": "2 pitas with 200 g raw chicken", "P": "1 pita with 130 g raw chicken (the extra chicken on the side)"},
 ingredients=[
  ("chicken thigh fillet, skinless", 330, "g", {"per": {"J": 200, "P": 130}}),
  ("high-protein Greek yoghurt", 50, "g", {"share": 1, "label": "Greek yoghurt, for the marinade"}),
  ("lemon juice", 1, "tbsp", {"share": 1}), ("garlic", 3, "clove", {"share": 1}), ("dried oregano", 2, "tsp", {"share": 1}), ("smoked paprika", 1, "tsp", {"share": 1}),
  ("pita bread", 3, "whole", {"per": {"J": 2, "P": 1}}),
  ("tomato", 2, "whole", {"share": 1, "label": "tomatoes, sliced"}), ("red onion", 0.5, "whole", {"share": 1, "label": "red onion, thinly sliced"}),
  ("cos lettuce", 0.5, "whole", {"share": 1, "label": "cos lettuce, shredded"}),
 ],
 steps=[
  ("Marinate", "Mix the yoghurt, lemon juice, crushed garlic, oregano, paprika and salt. Coat the chicken and leave at least 20 minutes, or overnight.", 1200),
  ("Cook", "Hot barbecue or grill pan. Cook the chicken until charred and cooked through, about 5 minutes a side.", 600),
  ("Slice", "Rest 5 minutes, then slice thinly.", 300),
  ("Wrap", "Warm the pitas. Load with chicken, tomato, onion, lettuce and tzatziki, and roll up in baking paper to hold it together.", 0),
 ])

recipe(id="prawn-saganaki", title="Prawn Saganaki", category="dinner", short="Prawn saganaki with sourdough",
 desc="Prawns baked in a garlicky tomato sauce with feta and oregano, with sourdough to mop it up.",
 tags=["seafood", "greek", "quick"], time=30, base={"J": 1, "P": 1}, share=0.65,
 portions={"J": "200 g raw prawns, half the sauce, 2 slices sourdough", "P": "130 g raw prawns, half the sauce, 1 slice sourdough"},
 ingredients=[
  ("raw prawns, peeled", 330, "g", {"per": {"J": 200, "P": 130}}),
  ("diced tomatoes, tinned", 1, "tin", {"share": 1}), ("brown onion", 1, "whole", {"share": 1, "label": "onion, finely diced"}),
  ("garlic", 3, "clove", {"share": 1}), ("olive oil", 2, "tsp", {"share": 1}), ("dried oregano", 1, "tsp", {"share": 1}),
  ("spices (your mix)", 0.5, "tsp", {"share": 1, "label": "chilli flakes"}),
  ("light feta", 60, "g", {"per": {"J": 35, "P": 25}, "label": "light feta, crumbled"}),
  ("fresh herbs (dill, mint, parsley or chives)", 2, "tbsp", {"share": 1, "label": "parsley or dill, chopped"}),
  ("sourdough", 3, "slice", {"per": {"J": 2, "P": 1}}),
 ],
 steps=[
  ("Sauce", "Oven to 200°C (180°C fan). In an ovenproof pan, cook the onion in the oil until soft, then the garlic, oregano and chilli for a minute.", 420),
  ("Simmer", "Add the tomatoes and simmer until thick, about 10 minutes. Season.", 600),
  ("Prawns and feta", "Nestle the prawns into the sauce and crumble the feta over the top.", 0),
  ("Bake", "Bake until the prawns are pink and the feta is soft and golden at the edges.", 600),
  ("Serve", "Scatter with herbs and serve with toasted sourdough.", 0),
 ], notes="No ovenproof pan? Simmer the prawns in the sauce with the lid on for 3 to 4 minutes, then add the feta.")
