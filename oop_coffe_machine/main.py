from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# variables
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True

while is_on:
    # Gets an order
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ")
    # Turn machine off
    if choice == "off":
        is_on = False
    # Make report of inventory
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # Makes coffee
    else:
        # Picking coffee
        drink = menu.find_drink(choice)
        # Is it able to make it coffee
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)