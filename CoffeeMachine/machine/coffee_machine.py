"""
    Let's redesign our program and write a class that represents the coffee
machine. The class should have a method that takes a string as input. Every
time the user inputs a string to the console, the program invokes this method
with one argument: the line that user input to the console. This system
simulates pretty accurately how real-world electronic devices work. External
components (like buttons on the coffee machine or tapping on the screen)
generate events that pass into the single interface of the program.
    The class should not use system input at all; it will only handle the
input that comes to it via this method and its string argument.
    The first problem that comes to mind: how to write that method in a way
that it represents all that coffee machine can do? If the user inputs a single
number, how can the method determine what that number is: a variant of coffee
chosen by the user or the number of the disposable cups that a special worker
added into the coffee machine?
    The right solution to this problem is to store the current state of the
machine. The coffee machine has several states it can be in. For example, the
state could be "choosing an action" or "choosing a type of coffee". Every time
the user inputs something and a program passes that line to the method, the
program determines how to interpret this line using the information about the
current state. After processing this line, the state of the coffee machine can
be changed or can stay the same.

This portion involves a lot of refactoring into a Object Oriented rendition of the "Coffee Machine"
"""


class CoffeeMachine:
    def __init__(self):  # Values for when object is initialized
        self.water = 400
        self.milk = 540
        self.coffee_bean = 120
        self.cups = 9
        self.money = 550
        self.state = "select"

    def __str__(self):  # Output to user for remaining resources
        return f'''
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_bean} of coffee beans
{self.cups} of disposable cups
${self.money} of money'''

    def user_choice(self, action):
        if action == "buy":
            print("What do you want to buy?\n1 - espresso\n2 - latte\n3 - cappuccino\nback - to main menu:\n")
            self.state = "buy"
        elif action == "fill":
            print("What would you like to fill?\nwater\nmilk\ncoffee beans\ncups\n")
            self.state = "fill"
        elif action == "take":
            print(f"I gave you {self.money}")
            self.money = 0
            self.state = "select"
            self.main_menu()
        elif action == "remaining":
            print(self)
            self.state = "select"
            self.main_menu()

    def order_coffee(self, coffee_type):
        self.state = "select"
        if coffee_type == "1":
            self.brew_coffee(water=250, bean=16, price=4)
        elif coffee_type == "2":
            self.brew_coffee(water=350, milk=75, bean=20, price=7)
        elif coffee_type == "3":
            self.brew_coffee(water=200, milk=100, bean=12, price=6)
        self.main_menu()

    def resource_check(self, req_water, req_milk, req_bean, req_cup=1):
        lack = None
        if self.water < req_water:
            lack = "water"
        elif self.milk < req_milk:
            lack = "milk"
        elif self.coffee_bean < req_bean:
            lack = "coffee beans"
        elif self.cups < req_cup:
            lack = "cups"
        else:
            self.water -= req_water
            self.milk -= req_milk
            self.coffee_bean -= req_bean
            self.cups -= req_cup
        return lack

    def brew_coffee(self, water=0, milk=0, bean=0, price=0):
        resource_check = self.resource_check(water, milk, bean)
        if resource_check is None:
            self.money += price
            print("I have enough resources, making you a coffee!")
        else:
            print(f"Sorry, not enough {resource_check}!")

    def refill(self, water_refill=0, milk_refill=0, bean_refill=0, cup_refill=0):
        self.water += water_refill
        self.milk += milk_refill
        self.coffee_bean += bean_refill
        self.cups += cup_refill
        self.state = "select"
        self.main_menu()

    def fill(self, resource):
        if resource == "water":
            print("Write how many ml of water that you want to add:\n")
            self.state = "water"
        elif resource == "milk":
            print("Write how many ml of milk that you want to add:\n")
            self.state = "milk"
        elif resource == "coffee beans":
            print("Write how many grams of coffee beans you want to add:\n")
            self.state = "coffee"
        elif resource == "cups":
            print("Write how many disposable cups of coffee you want to add:\n")
            self.state = "cups"

    def main_menu(self, pick=None):
        if self.state == "action":
            self.user_choice(pick)
        elif self.state == "buy":
            self.order_coffee(pick)
        elif self.state == "fill":
            self.fill(pick)
        elif self.state == "water":
            self.refill(water_refill=int(pick))
        elif self.state == "milk":
            self.refill(milk_refill=int(pick))
        elif self.state == "coffee":
            self.refill(bean_refill=int(pick))
        elif self.state == "cups":
            self.refill(cup_refill=int(pick))
        else:
            print("\nWrite action (buy, fill, take, remaining, exit):")
            self.state = "action"


cafesuada = CoffeeMachine()
user_input = ""

while user_input != cafesuada:  # Loop user input with exit condition
    cafesuada.main_menu(user_input)
    user_input = input()
