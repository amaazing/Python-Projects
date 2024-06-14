'''Author: Maaz Ali
Date: May 13 2024
Program that simulates a coffee machine
'''
import data

def resource_check(flavor: str, resources: dict) -> bool:
    for entry in data.MENU[flavor]["ingredients"]:
        if data.MENU[flavor]["ingredients"][entry] > resources[entry]:
            print(f"Sorry there is not enough {entry}.")
            return False
    return True
        
def report(resources: dict) -> None:
    for entry in resources:
        if entry == "money":
            print(f"{entry.title()}: ${resources[entry]}")
        else:
            print(f"{entry.title()}: {resources[entry]}mL")
    return

def coin_request() -> int:
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*(0.25) + dimes*(0.10) + nickels*(0.05) + pennies*(0.01)
    return total

def deduct_resources(flavor: str, resources: dict) -> dict:
    for entry in data.MENU[flavor]["ingredients"]:
        resources[entry] -= data.MENU[flavor]["ingredients"][entry]
    return resources

if __name__ == '__main__':
    resources = {"water": 500,
                 "milk": 500,
                 "coffee": 500,
                 "money": 0
    }
    off = False
    while not off:
        flavor = input("What would you like? (espresso/latte/cappucino):")
        if flavor == "off":
            exit()
        elif flavor == "report":
            report(resources)
        elif flavor == "espresso" or flavor == "latte" or flavor == "cappucino":
            if (resource_check(flavor, resources)) == True:
                cash = coin_request()
                if data.MENU[flavor]["cost"] > cash:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["money"] += data.MENU[flavor]["cost"]
                    change = cash - data.MENU[flavor]["cost"]
                    print(f"Here is ${change:.2f} in change.")
                    resources = deduct_resources(flavor, resources)
                    print(f"Here is your {flavor}. Enjoy!")

