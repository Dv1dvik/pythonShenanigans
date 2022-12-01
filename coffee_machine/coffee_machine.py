MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_earned = 0
should_run = True
# Checking if in inventory is enough materials
def is_drink_doable(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, we don't have enough {item} in the machine.")
            return False
        return True
# Input and calculating money
def payment():
    global money_earned
    quarter = int(input("How many quartets?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total_money_input = 0.25 * quarter + 0.20 * dime + 0.05 * nickel + 0.01 * penny
    if total_money_input < MENU[prompt]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        money_earned += total_money_input
        money_returned = round(total_money_input - MENU[prompt]["cost"], 2)
        print(f"Here is {money_returned} in change.")
        print(f"Here is your {prompt} ☕️. Enjoy!")

# Update inventory after making coffee
def upadte_inventory(order_ingredients):
    global resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

# Off, report status of inventory and making coffee
def answer():
    global prompt
    global should_run
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    # Turn off teh coffee machine
    if prompt == "off":
        should_run = False
    # Print the report of the resources
    elif prompt == "report":
        report = f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_earned}"
        resources["money"] = money_earned
        return report
    # Checking if coffee is doable and making it
    else:
        if is_drink_doable(order_ingredients = MENU[prompt]["ingredients"]):
            payment()
            upadte_inventory(order_ingredients = MENU[prompt]["ingredients"])



# running the coffee machine
while should_run:
    print(answer())