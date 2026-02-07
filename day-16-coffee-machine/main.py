import time
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0.0
coffee_emoji = "☕"
money_bag_emoji = "💰"

#Create a function that prints a report like the following
# Water: 300ml, Milk: 200ml, Coffee: 100g, Money: $0
def print_report(resource_data):
    """Prints a report of the machine resources and collected money."""
    return (f"Water: {resource_data['water']}ml\n"
            f"Milk: {resource_data['milk']}ml\n"
            f"Coffee: {resource_data['coffee']}g\n"
            f"Money: ${money}")

def change_back(inserted_cents):
    """Calculates how many of each coin the user gets returned when there is overpayment."""
    coin_values = {
        'quarters': 25,
        'dimes': 10,
        'nickels': 5,
        'pennies': 1
    }
    money_back = {}
    remaining_cents = inserted_cents

    for coin_type, coin_value in coin_values.items():
        money_back[coin_type] = remaining_cents // coin_value
        remaining_cents = remaining_cents % coin_value
    return money_back

def print_change_back(change_back_dict):
    """Prints back the returned change formatted nicely."""
    change_back_total = sum(change_back_dict.values())
    if change_back_total == 0:
        print("No change back.")
    else:
        print(f"Don't forget to grab your change!\n{money_bag_emoji}")

        for coin_type, count in change_back_dict.items():
            if count > 0:
                if coin_type == 'pennies':
                    coin = 'penny' if count == 1 else 'pennies'
                else:
                    coin = coin_type if count > 1 else coin_type [:-1]
                print(f"{count} {coin}")

def get_coffee_ingredients(menu_data, user_selection):
    """"Retrieves coffee ingredients needed for each menu seleltion."""
    return menu_data[user_selection]['ingredients']

def get_coffee_cost(menu_data, user_selection):
    """Retrieves the cost of each menu selection."""
    return menu_data[user_selection]['cost']

#Create a function that checks if there are enough resources for user coffee choice
def check_sufficient_resource_bool(menu_data, user_selection):
    """Checks if there are enought resources to make the menu selection."""
    global resources
    coffee_ingredients = get_coffee_ingredients(menu_data, user_selection)

    #You can turn this into a for loop such as:
    # for item in coffe_ingredients ...
    if resources['water'] < coffee_ingredients['water']:
        print(f"Sorry there is not enough water.")
        return False
    elif resources['milk'] < coffee_ingredients['milk']:
        print(f"Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < coffee_ingredients['coffee']:
        print(f"Sorry there is not enough coffee.")
        return False
    else:
        return True

def process_inserted_coins(quarters, dimes, nickels, pennies):
    """Returns the total money value of all the inserted coins."""
    return (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies

def making_coffee(seconds = 3):
    """Simulates making coffee. Uses time.sleep with parameter seconds. Default is 3 seconds."""
    print("Making coffee...")
    time.sleep(seconds)
    print(f"Coffee is ready!")
    print(coffee_emoji)

def update_resources(resources_dict, menu_data, user_selection):
    """Updates the resources once coffe is successfully made."""
    coffee_ingredients = get_coffee_ingredients(menu_data, user_selection)
    resources_dict['water'] -= coffee_ingredients['water']
    resources_dict['milk'] -= coffee_ingredients['milk']
    resources_dict['coffee'] -= coffee_ingredients['coffee']

def reset_resources(resources_dict):
    """Resets the resources to the initial default values."""
    resources_dict['water'] = 300
    resources_dict['milk'] = 200
    resources_dict['coffee'] = 100

continue_coffee_transactions = True
def coffee_machine():
    """"Main coffee vending machine function."""
    global continue_coffee_transactions
    global money
    global resources

    while continue_coffee_transactions:

        #Prompt user for their order
        # besides 'espresso', 'latte', and 'cappuccino', 'report' is also a choice
        selection = input("What would you like? (espresso/latte/cappuccino/report/service): ").lower()

        if selection == 'report':
            print(f"Resources:\n{print_report(resources)}")
            print(f"Profit: ${money:.2f}")
            if input("Would you like to make another selection? Type 'y' for Yes or 'n' for No: ").lower() == 'y':
                continue_coffee_transactions = True
            else:
                continue_coffee_transactions = False
        elif selection == 'service':
            reset_resources(resources)
        else:
            if check_sufficient_resource_bool(MENU, selection):
                cost_in_cents = int(get_coffee_cost(MENU, selection) * 100)
                print(f"(Cost in cents): {cost_in_cents}")
                print(f"Insert ${get_coffee_cost(MENU, selection):.2f} in coins.")
                inserted_quarters = int(input("How many quarters?: "))
                inserted_dimes = int(input("How many dimes?: "))
                inserted_nickels = int(input("How many nickels?: "))
                inserted_pennies = int(input("How many pennies?: "))
                total_inserted_payment = process_inserted_coins(inserted_quarters, inserted_dimes, inserted_nickels, inserted_pennies)
                print(f"You inserted a total of {total_inserted_payment} cents.")

                if cost_in_cents <= total_inserted_payment:
                    making_coffee()
                    difference_from_cost = total_inserted_payment - cost_in_cents
                    change_returned = change_back(difference_from_cost)
                    print_change_back(change_returned)
                    #update resources
                    update_resources(resources, MENU, selection)
                    #increment money
                    money += get_coffee_cost(MENU, selection)

                    if input(
                            "Would you like to make another selection? Type 'y' for Yes or 'n' for No: ").lower() == 'y':
                        continue_coffee_transactions = True
                    else:
                        print("See you again soon!")
                        continue_coffee_transactions = False

                elif cost_in_cents > total_inserted_payment:
                    print(f"Insufficient payment. Your payment of ${total_inserted_payment/100:.2f} is returned.")

                    if input(
                            "Would you like to make another selection? Type 'y' for Yes or 'n' for No: ").lower() == 'y':
                        continue_coffee_transactions = True
                    else:
                        print("See you again soon!")
                        continue_coffee_transactions = False
            else:
                print(f"Sorry. Not enough resources for {selection}.")
                if input(
                        "Would you like to make another selection? Type 'y' for Yes or 'n' for No: ").lower() == 'y':
                    continue_coffee_transactions = True
                else:
                    print("See you again soon!")
                    continue_coffee_transactions = False


coffee_machine()