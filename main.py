### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

        # Iterate through the dictionary and return False if ingredients is less than amount
        # Return True otherwise
        for ingredients, amount in ingredients.items():
            if self.machine_resources.get(ingredients, 0) < amount:
                return False
        return True

    def process_coins(self, cost):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        # Declare total variable
        # While total is less than cost, the user inputs coins and is added to total
        # Returns total after total is greater than cost
        total = 0
        while total < cost:
            try:
                coins = float(input("Enter coins: "))
                total += coins
            except ValueError:
                print("Invalid input. Please enter valid input")
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Insufficient Funds")
            return False
        elif coins > cost:
            change = coins - cost
            print("Your change is $", change)
            return True
        else:
            print("Thank you for your purchase!")
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        recipe = recipes[sandwich_size]["ingredients"]
        for ingredient, amount in recipe.items():
            self.machine_resources[ingredient] -= amount


### Make an instance of SandwichMachine class and write the rest of the codes ###
def main():


    sandwichMachine = SandwichMachine(resources)

    while True:
        print("Hello, welcome to the Sandwich Maker")
        userInput = input("What would you like? (Small/Medium/Large/Off/Reprt): ").lower()

        if userInput == "off":
            print("Thank you, have a great day.")
            break

        elif userInput == "report":
            for ingredient, amount in sandwichMachine.machine_resources.items():
                print(f"{ingredient}: {amount}")
            continue
        elif userInput in recipes:
            size = userInput
            ingredients_needed = recipes[size]["ingredients"]
            cost = recipes[size]["cost"]

            if sandwichMachine.check_resources(ingredients_needed):
                print(f"Please insert ${cost} to make {size} sandwhich.")
                userCoins = sandwichMachine.process_coins(cost)
                transaction = sandwichMachine.transaction_result(userCoins, cost)

                if transaction:
                    sandwichMachine.make_sandwich(size,ingredients_needed)
                    print(f"Here is your {size} sandwich. Enjoy!")
            else:
                print(f"Insufficient resource to make sandwich. We apologize for the inconvenience. Here is your Change")
        else:
            print("Invalid input. Please try again")

if __name__ == "__main__":
    main()