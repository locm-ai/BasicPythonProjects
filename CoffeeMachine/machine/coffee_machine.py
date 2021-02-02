"""

Let's simulate an actual coffee machine! What do we need for that? This coffee machine will have a limited supply of water, milk, coffee beans, and disposable cups. Also, it will calculate how much money it gets for selling coffee.
There are several options for the coffee machine we want you to implement: first, it should sell coffee. It can make different types of coffee: espresso, latte, and cappuccino. Of course, each variety requires a different amount of supplies, however, in any case, you will need only one disposable cup for a drink. Second, the coffee machine must get replenished by a special worker. Third, another special worker should be able to take out money from the coffee machine.
Objectives

The program offers to buy one cup of coffee or to fill the supplies or to take its money out. Note that the program is supposed to do one of the mentioned actions at a time. It should also calculate how many ingredients and money have left. Display the number of supplies before and after purchase.
    First, your program reads one option from the standard input, which can be
"buy", "fill", "take". If a user wants to buy some coffee, the input is "buy".
If a special worker thinks that it is time to fill out all the supplies for
the coffee machine, the input line will be "fill". If another special worker
decides that it is time to take out the money from the coffee machine, you'll
get the input "take".
    If the user writes "buy" then they must choose one of three types of
coffee that the coffee machine can make: espresso, latte, or cappuccino.
    For one espresso, the coffee machine needs 250 ml of water and 16 g of
coffee beans. It costs $4.
    For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and
20 g of coffee beans. It costs $7.
    And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of
milk, and 12 g of coffee. It costs $6.
    If the user writes "fill", the program should ask them how much water,
    milk, coffee and how many disposable cups they want to add into the coffee
machine.
    If the user writes "take" the program should give all the money that it
earned from selling coffee.
    At the moment, the coffee machine has $550, 400 ml of water, 540 ml of
milk, 120 g of coffee beans, and 9 disposable cups.

To sum up, your program should print the coffee machine's state, process one
query from the user, as well as print the coffee machine's state after that.
Try to use functions for implementing every action that the coffee machine can do.

"""
available_water = 400
available_milk = 540
available_coffee_beans = 120
available_cups = 9
available_money = 550


def machine_display():
    print("The coffee machine has:")
    print(f"{available_water} of water")
    print(f"{available_milk} of milk")
    print(f"{available_coffee_beans} of coffee beans")
    print(f"{available_cups} of disposable cups")
    print(f"{available_money} of money")

machine_display()
user_action = input("Write action (buy, fill, take):\n")
if user_action == "buy":
    coffee_type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:\n"))
    print()
    if coffee_type == 1:
        available_water -= 250
        available_coffee_beans -= 16
        available_cups -= 1
        available_money += 4
    elif coffee_type == 2:
        available_water -= 350
        available_milk -= 75
        available_coffee_beans -= 20
        available_cups -= 1
        available_money += 7
    elif coffee_type == 3:
        available_water -= 200
        available_milk -= 100
        available_coffee_beans -= 12
        available_cups -= 1
        available_money += 6
elif user_action == "fill":
    available_water += int(input("Write how many ml do you want to add:\n"))
    available_milk += int(input("Write how many ml of milk do you want to add:\n"))
    available_coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    available_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
elif user_action == "take":
    print(f"I gave you ${available_money}")
    available_money -= available_money

machine_display()