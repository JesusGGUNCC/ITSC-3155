class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredients, amount in ingredients.items():
            if self.machine_resources.get(ingredients, 0) < amount:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):

        recipe = order_ingredients[sandwich_size]["ingredients"]

        for ingredient, amount in recipe.items():
            self.machine_resources[ingredient] -= amount
