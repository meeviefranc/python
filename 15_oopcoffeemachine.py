"""
Created on 03 Jun 2023
@author: meeviefranc
"""
import os
import importlib

# initialize all the classes
menupy = importlib.import_module("oopcoffeemachine.menu")
Menu = getattr(menupy, "Menu")
MenuItem = getattr(menupy, "MenuItem")
coffee_makerpy = importlib.import_module("oopcoffeemachine.coffee_maker")
CoffeeMaker = getattr(coffee_makerpy, "CoffeeMaker")
money_machinepy = importlib.import_module("oopcoffeemachine.money_machine")
MoneyMachine = getattr(money_machinepy, "MoneyMachine")
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def report():
    coffee_maker.report()
    money_machine.report()


def choose(q, choice):
    ask = True
    while ask:
        ans = input(q).lower()
        """secret words for the application prompts (coffee choice, order again) are off and report"""
        if ans == "off":
            ask = False
        elif ans == "report":
            report()
            ask = True
        elif ans not in choice:
            print("Not a valid choice. Pick one: ", choice)
            ask = True
        else:
            ask = False
    return ans


def order_again():
    if (choose('Do you want to order again? (y/n): ', ["y", "n"])) == "y":
        return True
    else:
        return False


def oopcoffeemachine():
    have_supply = True
    make_order = True
    while make_order:
        just = os.system('clear')
        kopi = choose(f'What would you like? ({menu.get_items()}): ', ["espresso", "latte", "cappuccino"])
        if kopi == "off":
            make_order = False
        else:
            order = menu.find_drink(kopi)
            have_supply = coffee_maker.is_resource_sufficient(order)
            if have_supply:
                if (money_machine.make_payment(order.cost)):
                    coffee_maker.make_coffee(order)
                make_order = order_again()
            else:
                print("Oh no! It looks like I've run out of my supply. I have to close shop. Come back tomorrow!")
                make_order = False
    coffee_maker.refill()
    money_machine.backto()



