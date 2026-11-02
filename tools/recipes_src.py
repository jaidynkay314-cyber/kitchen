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
