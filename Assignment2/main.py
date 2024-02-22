import data
from sandwich_maker import SandwichMaker
from Assignment2.cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        print("Hello, welcome to the Sandwich Maker")
        userInput = input("What would you like? (Small/Medium/Large/Off/Reprt): ").lower()

        if userInput == "off":
            print("Thank you, have a great day.")
            break

        elif userInput == "report":
            for ingredient, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{ingredient}: {amount}")
            continue


        elif userInput in recipes:
            size = userInput
            ingredients_needed = recipes[size]["ingredients"]
            recipe = recipes
            cost = recipes[size]["cost"]

            if sandwich_maker_instance.check_resources(ingredients_needed):
                print(f"Please insert ${cost} to make {size} sandwhich.")
                userCoins = cashier_instance.process_coins()
                transaction = cashier_instance.transaction_result(userCoins, cost)

                if transaction:
                    sandwich_maker_instance.make_sandwich(size, recipe)
                    print(f"Here is your {size} sandwich. Enjoy!")
            else:
                print(
                    f"Insufficient resource to make sandwich. We apologize for the inconvenience. Here is your Change")
        else:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    main()
