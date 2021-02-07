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
money =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 4. Check the resources are sufficient
def is_resources_sufficient(order_ingredients):
    """ Returns true when order can be made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

#TODO: 5. Process Coins
def process_Coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins.")
    quarter_coin = int(input("How many Quarters? : ")) * 0.25
    dimes_coin = int(input("How many dimes? : ")) * 0.1
    nickle_coin = int(input("How many nickles? : ")) * 0.05
    pennies_coin = int(input("How many pennies? : ")) * 0.01
    total = quarter_coin + dimes_coin + nickle_coin + pennies_coin
    return total

# TODO: 6. Check Transaction Successful
def is_transaction_successful(money_received,drink_cost):
    """Return true when payment is accepted or returns false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money.Money Refunded.")
        return False

#TODO: 7. Make Coffee
def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")

is_on = True
while is_on:
    # TODO: 1. Prompt the user by asking what would you like.
    user_choice = input("What would you like? (espresso/latte/cappuccino): \n")
    # TODO: 2. Turn Off the coffee machine by entering off to the prompt
    if user_choice=="off":
        is_on = False
    # TODO: 3. Print the report
    elif user_choice =="report":
        print(f"Water:{resources['water']} ")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']} ")
        print(f"Money: ${money}")
    else:
        drink = MENU[user_choice]

        if is_resources_sufficient(drink["ingredients"]):
            payment = process_Coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(user_choice,drink["ingredients"])



