# coffee machine, 3 flavors espresso, latte, cappuccino
from menu import MENU, resources


def check_resources(order_in):
    for item in MENU[order_in]['ingredients']:
        if MENU[order_in]['ingredients'][item] >= resources[item]:
            print(f"There isn't enough {item}")
            return False
    return True


def make_order(order_in):
    if order_in == 'latte' or order_in == 'cappuccino':
        resources['water'] -= MENU[order_in]['ingredients']['water']
        resources['milk'] -= MENU[order_in]['ingredients']['milk']
        resources['coffee'] -= MENU[order_in]['ingredients']['coffee']
    elif order_in == 'espresso':
        resources['water'] -= MENU[order_in]['ingredients']['water']
        resources['coffee'] -= MENU[order_in]['ingredients']['coffee']


def coins(coin25, coin10, coin5, coin1):
    total = coin25 * 0.25 + coin10 * 0.1 + coin5 * 0.05 + coin1 * 0.01
    return total


def money_exchange(cash_in):
    if cash_in > MENU[customer_order]['cost']:
        cash_in -= MENU[customer_order]['cost']
        resources['Money'] += MENU[customer_order]['cost']
        print(f"Your change is $ {round(cash_in, 2)}")
        return True
    elif inserted_cash == MENU[customer_order]['cost']:
        resources['Money'] += cash_in
        return True
    else:
        return False


run = True
resources['Money'] = 0
while run:
    customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_order == 'off':
        run = False
    elif customer_order == 'report':
        print(resources)
    elif check_resources(customer_order):
        print("Insert coins:")
        quarters = float(input("how many quarters:"))
        dimes = float(input("how many dimes:"))
        nickels = float(input("how many nickels:"))
        pennies = float(input("how many pennies:"))
        inserted_cash = coins(quarters, dimes, nickels, pennies)
        if money_exchange(inserted_cash):
            make_order(customer_order)
            print(f"Enjoy your {customer_order} ")
        else:
            print("Here is your refund. Not enough money")
    elif not check_resources(customer_order):
        print("order something else")
