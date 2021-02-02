"""
Now let's consider a case when you need a lot of coffee. Maybe you're hosting
a party with a lot of guests! In these circumstances, it's better to make
preparations in advance.
So, we will ask a user to enter the desired amount of coffee, in cups. Given
this, you can adjust the program by calculating how much water, coffee, and
milk are necessary to make the specified amount of coffee.
Of course, all this coffee is not needed right now, so at this stage, the
coffee machine doesn't actually make any coffee yet.

Let's break the task into several steps:
    First, read the numbers of coffee drinks from the input.
    Figure out how much of each ingredient the machine will need. Note that
one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml
of milk, and 15 g of coffee beans.
    Output the required ingredient amounts back to the user.
"""

number_of_cups_of_coffee = int(input("Write how many cups of coffee you will need:\n"))
print(f"For {number_of_cups_of_coffee} you will need:")
water = 200
milk = 50
coffee_beans = 15
print(f"{water * number_of_cups_of_coffee} ml of water")
print(f"{milk * number_of_cups_of_coffee} ml of milk")
print(f"{coffee_beans * number_of_cups_of_coffee} g of coffee beans")