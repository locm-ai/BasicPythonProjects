"""

    Just one action is not so interesting, is it? Let's improve the program so it
can do multiple actions, one after another. It should repeatedly ask a user
what they want to do. If the user types "buy", "fill" or "take", then the
program should do exactly the same thing it did in the previous step. However,
if the user wants to switch off the coffee machine, they should type "exit".
The program should terminate on this command. Also, when the user types
"remaining", the program should output all the resources that the coffee
machine has.

    The program that will work endlessly to make coffee for all interested
persons until the shutdown signal is given. Introduce two new options:
"remaining" and "exit".
    There is a chance that you can be out of resources for making coffee. If
the coffee machine doesn't have enough resources to make coffee, the program
should output a message that says it can't make a cup of coffee.
    And the last improvement to the program at this step — if the user types
"buy" to buy a cup of coffee and then changes his mind, they should be able to
type "back" to return into the main cycle.

"""
available_water = 400
available_milk = 540
available_coffee_beans = 120
available_cups = 9
available_money = 550

def machine_display():
    print("\nThe coffee machine has:")
    print(f"{available_water} of water")
    print(f"{available_milk} of milk")
    print(f"{available_coffee_beans} of coffee beans")
    print(f"{available_cups} of disposable cups")
    print(f"{available_money} of money\n")


user_action = input("Write action (buy, fill, take, remaining, exit):\n")
while user_action != exit:
    if user_action == "buy":
        coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:\n")
        if coffee_type == "1":
            available_water -= 250
            available_coffee_beans -= 16
            available_cups -= 1
            available_money += 4
            if available_water < 0:
                available_water += 250
                available_coffee_beans += 16
                available_cups += 1
                available_money -= 4
                print(f"Sorry, not enough water!")
            elif available_milk < 0:
                available_water += 250
                available_coffee_beans += 16
                available_cups += 1
                available_money -= 4
                print(f"Sorry, not enough milk!")
            elif available_coffee_beans < 0:
                available_water += 250
                available_coffee_beans += 16
                available_cups += 1
                available_money -= 4
                print(f"Sorry, not enough coffee beans!")
            elif available_cups < 0:
                available_water += 250
                available_coffee_beans += 16
                available_cups += 1
                available_money -= 4
                print(f"Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
            user_action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        elif coffee_type == "2":
            available_water -= 350
            available_milk -= 75
            available_coffee_beans -= 20
            available_cups -= 1
            available_money += 7
            if available_water < 0:
                available_water += 350
                available_milk += 75
                available_coffee_beans += 20
                available_cups += 1
                available_money -= 7
                print(f"Sorry, not enough water!")
            elif available_milk < 0:
                available_water += 350
                available_milk += 75
                available_coffee_beans += 20
                available_cups += 1
                available_money -= 7
                print(f"Sorry, not enough milk!")
            elif available_coffee_beans < 0:
                available_water += 350
                available_milk += 75
                available_coffee_beans += 20
                available_cups += 1
                available_money -= 7
                print(f"Sorry, not enough coffee beans!")
            elif available_cups < 0:
                available_water += 350
                available_milk += 75
                available_coffee_beans += 20
                available_cups += 1
                available_money -= 7
                print(f"Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
            user_action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        elif coffee_type == "3":
            available_water -= 200
            available_milk -= 100
            available_coffee_beans -= 12
            available_cups -= 1
            available_money += 6
            if available_water < 0:
                available_water += 200
                available_milk += 100
                available_coffee_beans += 12
                available_cups += 1
                available_money -= 6
                print(f"Sorry, not enough water!")
            elif available_milk < 0:
                available_water += 200
                available_milk += 100
                available_coffee_beans += 12
                available_cups += 1
                available_money -= 6
                print(f"Sorry, not enough milk!")
            elif available_coffee_beans < 0:
                available_water += 200
                available_milk += 100
                available_coffee_beans += 12
                available_cups += 1
                available_money -= 6
                print(f"Sorry, not enough coffee beans!")
            elif available_cups < 0:
                available_water += 200
                available_milk += 100
                available_coffee_beans += 12
                available_cups += 1
                available_money -= 6
                print(f"Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
            user_action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        elif coffee_type == "back":
            user_action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    elif user_action == "fill":
        available_water += int(input("Write how many ml do you want to add:\n"))
        available_milk += int(input("Write how many ml of milk do you want to add:\n"))
        available_coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        available_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        user_action = input("Write action (buy, fill, take, remaining, exit):\n")
    elif user_action == "take":
        print(f"I gave you ${available_money}")
        available_money -= available_money
        user_action = input("Write action (buy, fill, take, remaining, exit):\n")
    elif user_action == "remaining":
        machine_display()
        user_action = input("Write action (buy, fill, take, remaining, exit):\n")
    elif user_action == "exit":
        break
