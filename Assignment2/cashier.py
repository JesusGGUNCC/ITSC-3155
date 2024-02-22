class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0
        total += int(input("How many Dollars: ")) * 1.00
        total += int(input("How many Quarters: ")) * .25
        total += int(input("How many Dimes: ")) * .1
        total += int(input("How many Nickles: ")) * .05
        total += int(input("How many Pennies: ")) * .01

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Insufficient Fund")
            return False
        else:
            change = round(coins - cost, 2)
            print("Sufficient Funds! Thank you for your purchase")
            print(f"Here is your change: ${change}")
            return True
