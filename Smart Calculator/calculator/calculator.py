"""
    It is time to improve the previous version of the calculator. What if we
have many pairs of numbers, the sum of which we need to find? It will be very
inconvenient to run the program every time. So then let's add a loop to
continuously calculate the sum of two numbers. We will also be sure to have a
safeword to break the loop. Also, It would be nice to think through situations
where users enter only one number or do not enter numbers at all.

Current Version
    Write a program that reads two numbers in a loop and prints the sum in the
standard output.
    If a user enters only a single number, the program should print the same
number. If a user enters an empty line, the program should ignore it.
    When the command /exit is entered, the program must print "Bye!" (without
quotes), and then stop.
"""
user_input = input()
while user_input != "/exit":
    if user_input == "":
        user_input = input()
    numbers = [int(x) for x in user_input.split(' ')]
    if len(numbers) > 1:
        print(numbers[0] + numbers[1])
        user_input = input()
    elif len(numbers) == 1:
        print(int(user_input))
        user_input = input()

print("Bye!")