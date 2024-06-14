from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker_maker = CoffeeMaker()
menu = Menu()

off = False

while not off:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "off":
        off = True
        break
    elif user_input == "report":
        coffee_maker_maker.report()
        money_machine.report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = menu.find_drink(user_input)
        if (coffee_maker_maker.is_resource_sufficient(drink)) == True:
            cash = money_machine.make_payment(drink.cost)
            coffee_maker_maker.make_coffee(drink)
        
