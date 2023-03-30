import resources
import menu
import money
import os

shut_down = False
print("Hello, I can make you coffee")

while not shut_down:
    os.system('cls' if os.name == 'nt' else 'clear')
    resources.print_resources()
    menu.print_menu()
    coffee_to_make = input("Enter please name of coffee you want: ")
    if resources.check_resources(menu.MENU[coffee_to_make]):
        while money.calculate_money() <= menu.MENU[coffee_to_make]['cost']:
            print(f"Insert please: ${menu.MENU[coffee_to_make]['cost']}")
            money.insert_coins()
            print(f"Inserted total: ${money.calculate_money()}")
        if money.calculate_money() > menu.MENU[coffee_to_make]['cost']:
            print(f"Your change is ${money.calculate_money() - menu.MENU[coffee_to_make]['cost']}")
        resources.make_order(menu.MENU[coffee_to_make])
        money.clean_money_memory()
        print("Your coffee is ready")

    if input("Do you want something else?: (y/n): ") == "n":
        shut_down = True
        print("Bye")
