# -*- coding: utf-8 -*-
"""
Created on 11 May 2023
@author: meeviefranc
replit: https://replit.com/@appbrewery/coffee-machine-final
"""
import os

recipe = [
    {
        'name': 'stock',
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'price': 0
    },
    {
        'name': 'espresso',
        'water': 50,
        'milk': 0,
        'coffee': 18,
        'price': 1.50
    },
    {
        'name': 'latte',
        'water': 200,
        'milk': 150,
        'coffee': 24,
        'price': 2.50
    },
    {
        'name': 'cappuccino',
        'water': 250,
        'milk': 100,
        'coffee': 24,
        'price': 3.00
    }]


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


def report():
    stock_index = next((i for (i, r) in enumerate(recipe) if r['name'] == "stock"))
    print(f'Water: {recipe[stock_index]["water"]}ml')
    print(f'Milk: {recipe[stock_index]["milk"]}ml')
    print(f'Coffee: {recipe[stock_index]["coffee"]}g')
    print(f'Money: ${recipe[stock_index]["price"]:.2f}')


def coins(q):
    while True:
        try:
            ans = int(input(q))
        except ValueError:
            print("That's not an integer!\n")
            continue
        else:
            break
    return ans


def dollar():
    """a dollar is worth 100 cents.
    penny = 1 cent x 100 . nickel = 5 cents x 20. dime = 10 cents x 10. quarter = 25 cents x 4. """
    total_dollar = 0
    print("Please insert coins.")
    quarter = coins("How many quarters?: ")
    dime = coins("How many dimes?: ")
    nickel = coins("How many nickels?: ")
    penny = coins("How many pennies?: ")
    penny_dollar = 0.01 * penny
    nickel_dollar = 0.05 * nickel
    dime_dollar = 0.10 * dime
    quarter_dollar = 0.25 * quarter
    total_dollar = penny_dollar + nickel_dollar + dime_dollar + quarter_dollar
    print(f"You gave me a total of ${total_dollar:.2f}.")
    return total_dollar


def inventory_update(stock_index, order_dict, profit):
    stock_dict = recipe[stock_index]
    if profit > 0:
        recipe[stock_index]["price"] += profit
    for item in order_dict:
        if item not in ("name", "price"):
            stock_dict[item] = stock_dict[item] - order_dict[item]


def inventory_refill(supply_dict):
    supply_dict["water"] = 300
    supply_dict["milk"] = 200
    supply_dict["coffee"] = 100
    supply_dict["price"] = 0


def no_stock(order_dict, supply_dict):
    return order_dict["water"] > supply_dict["water"], order_dict["milk"] > supply_dict["milk"], order_dict["coffee"] > supply_dict["coffee"]


def cash_register(pymt, order, stock_index, order_dict):
    profit = pymt
    change = pymt - order_dict["price"]
    print(f'Coffee \N{hot beverage} price is ${order_dict["price"]:.2f}.')
    if change < 0:
        print(f"Sorry that's not enough money for {order}. Money refunded.")
    else:
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
            profit = pymt - change
        else:
            print(f"You don't have any change.")
        print(f'Here is your {order} \N{hot beverage}. Enjoy!')
        """update inventory"""
        inventory_update(stock_index, order_dict, profit)


def order_again():
    if (choose('Do you want to order again? (y/n): ', ["y", "n"])) == "y":
        return True
    else:
        return False


def coffeemachine():
    """main game"""
    no_supply = False
    make_order = True
    while make_order:
        stock_index = next((i for (i, r) in enumerate(recipe) if r['name'] == "stock"))
        no_supply = (recipe[stock_index]["water"] <= 0) or (recipe[stock_index]["water"] <= 0) or (recipe[stock_index]["water"] <= 0)
        if no_supply:
            print("Oh no! It looks like I've run out of my supply. I have to close shop. Come back tomorrow!")
            make_order = False
        else:
            just = os.system('clear')
            profit = 0
            order = choose('What would you like? (espresso/latte/cappuccino): ', ["espresso", "latte", "cappuccino"])
            """secret word to turn off the machine"""
            if order == "off":
                make_order = False
            else:
                """check resources"""
                order_index = next((i for (i, r) in enumerate(recipe) if r['name'] == order))
                no_water, no_milk, no_coffee = no_stock(recipe[order_index], recipe[stock_index])
                if no_water:
                    print("Sorry there is not enough water. Order another.")
                elif no_coffee:
                    print("Sorry there is not enough coffee. Order another.")
                elif no_milk:
                    print("Sorry there is not enough milk. Order another.")
                else:
                    """accept payment"""
                    cash_register(dollar(), order, stock_index, recipe[order_index])
                make_order = order_again()
    inventory_refill(recipe[stock_index])

