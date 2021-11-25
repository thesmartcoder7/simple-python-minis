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

money = 0
is_machine_running = True
money_given = 0.00

coin_process = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}


def report():
    print("")
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource} : {resources[resource]}ml")
        else:
            print(f"{resource} : {resources[resource]}g")

    print(f"money : ${money} \n\n\n")


def drink_process(drink_choice):
    global money
    global resources
    global is_machine_running
    user_amount = money_given
    drink = MENU[drink_choice]
    ingredients = drink["ingredients"]
    if ingredients["water"] > 300:
        print("\nSorry, the amount of water available is not enough to make your drink.\n")
    elif ingredients["coffee"] > 100:
        print("\nSorry, the amount of coffee available is not enough to make your drink\n")
    elif ingredients["milk"] > 200:
        print("\nSorry, the amount of milk available is not enough to make your drink\n")
    else:
        print(f"That costs: ${drink['cost']}\n")
        user_coins = float(input("Please insert the coins in the coin slot.\n How many quarters?: "))
        user_amount += user_coins * coin_process["quarter"]
        user_coins = float(input(" How many dimes?: "))
        user_amount += user_coins * coin_process["dime"]
        user_coins = float(input(" How many nickles?: "))
        user_amount += user_coins * coin_process["nickle"]
        user_coins = float(input(" How many pennies?: "))
        user_amount += user_coins * coin_process["penny"]

        if user_amount == drink["cost"]:
            print(f"\nHere is your {drink_choice.capitalize()}. Enjoy")
            resources = {
                "water": resources["water"] - ingredients["water"],
                "milk": resources["milk"] - ingredients["milk"],
                "coffee": resources["coffee"] - ingredients["coffee"]
            }
            money += drink["cost"]
        elif user_amount > drink["cost"]:
            change = round(user_amount - drink["cost"], 2)
            print(f"\nHere is your change: ${change}")
            print(f"Here is your {drink_choice.capitalize()}. Enjoy")
            resources = {
                "water": resources["water"] - ingredients["water"],
                "milk": resources["milk"] - ingredients["milk"],
                "coffee": resources["coffee"] - ingredients["coffee"]
            }
            money += drink["cost"]
        else:
            difference = drink["cost"] - user_amount
            print(f"\nSorry, you are ${difference} short. Top it up and try again")
            is_machine_running = False

        print("\n\n\n")


while is_machine_running:
    user_response = input("What would you like? \n a) Espresso\n b) Latte\n c) Cappuccino \n").lower()
    if user_response == 'report':
        report()
    elif user_response == 'a' or user_response == 'espresso':
        drink_process("espresso")
    elif user_response == 'b' or user_response == 'latte':
        drink_process("latte")
    else:
        drink_process("cappuccino")
