"""Scale the cookie recipe to however many people turned up."""

BASE_SERVINGS = 12

# Grams, all of it. Eggs included, because "2.4 eggs" helps nobody.
RECIPE = {
    "butter": 225,
    "sugar": 200,
    "eggs": 100,
    "flour": 300,
    "chocolate": 200,
}


def scale(servings):
    """Every ingredient, multiplied by how far off twelve we are."""
    factor = servings / BASE_SERVINGS
    return {name: round(grams * factor, 1) for name, grams in RECIPE.items()}


if __name__ == "__main__":
    for name, grams in scale(24).items():
        print(f"{name:>10}: {grams}g")
