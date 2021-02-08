"""
    Our task is to make a smart calculator. What do you usually expect from a
calculator? Of course, it is bound to support 4 basic operations:
multiplication, division, addition, and subtraction. But we don't need to stop
there and add the ability to calculate expressions containing parenthesis and
the ability to remember the previous result. This will be a console
application, which we will improve gradually, from simple to complex.

    So, the first version of the calculator will only support the addition
operation for two numbers. In this version, we will not receive the plus
symbol (+) as an input, initially we will accept this as an unwritten rule
(because only one operation is supported).

Current Version
Write a program that reads two integer numbers from the same line and prints
their sum in the standard output. Numbers can be positive, negative, or zero.
"""

user_input = input()
numbers = user_input.split(' ')
print(int(numbers[0]) + int(numbers[1]))