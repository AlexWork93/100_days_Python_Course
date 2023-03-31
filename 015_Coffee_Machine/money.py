coins = {
    "quarter": 0,
    "dime": 0,
    "nickel": 0,
    "penny": 0
}


def calculate_money():
    amount_of_money = coins['quarter'] * 0.25
    amount_of_money += coins['dime'] * 0.10
    amount_of_money += coins['nickel'] * 0.5
    amount_of_money += coins['penny'] * 0.1
    return amount_of_money


def insert_coins():
    for key in coins:
        coins[key] += float(input(f"How many {key} do you want to insert: "))


def clean_money_memory():
    for key in coins:
        coins[key] = 0
