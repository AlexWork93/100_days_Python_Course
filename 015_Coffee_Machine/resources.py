resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_resources():
    print("Available resources")
    for key in resources:
        print(f"{key}: {resources[key]}")


def check_resources(product):
    enough_resources = True
    for key in product['ingredients']:
        if resources[key] < product['ingredients'][key]:
            enough_resources = False
            print(f"Sorry, for your order is required {product['ingredients'][key]} {key} but I have only {resources[key]}")
    return enough_resources


def make_order(product):
    for key in product['ingredients']:
        resources[key] -= product['ingredients'][key]
