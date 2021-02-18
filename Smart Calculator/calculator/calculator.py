"""
    Now we need to consider the reaction of the calculator when users enter
expressions in the wrong format. The program only knows numbers, a plus sign,
a minus sign, and two commands. It cannot accept all other characters and it
is necessary to warn the user about this.


    The program should print Invalid expression in cases when the given
expression has an invalid format. If a user enters an invalid command, the
program must print Unknown command. All messages must be printed without
quotes. The program must never throw an exception.
    To handle incorrect input, we should remember that the user input that
starts with / is a command, in other situations, it is an expression.
    Let's not forget to write methods to decompose our program. Like before,
/help command should print information about your program. When the command
/exit is entered, the program must print Bye! , and then stop.
"""


def commands(x):
    if x == "/help":
        print("The program calculates the sum of numbers")
    else:
        print("Unknown command")


def calc(x, y, z):
    if "-" in y:
        negatives = len(y) % 2
        if negatives == 1:
            return int(x) - int(z)
        else:
            return int(x) + int(z)
    elif "+" in y:
        return int(x) + int(z)
    elif "/" in y:
        div = len(y) % 2
        if div == 1:
            return int(x) / int(z)
        else:
            return int(x) // int(z)
    elif "%" in y:
        return int(x) % int(z)

def full(y):
    x = y.split()
    if len(x) == 3:
        return calc(x[0], x[1], x[2])
    else:
        offset = (len(x) - 3) // 2
        current = calc(x[0], x[1], x[2])
        for z in range(1, offset+1):
            current = calc(current, x[1+(z * 2)], x[2+(z * 2)])
        return current


def expression(x):
    operators = ["+", "-"]
    try:
        instructions = x.split()
        if len(instructions) >= 3:
            print(full(x))
            # print(eval(x))  Cheap way of having python do the logic
        elif len(instructions) == 2:
            print("Invalid Expression")
        elif len(instructions) == 1:
            if x[0].isalpha() or x[len(x) - 1] in operators:
                print("Invalid Expression")
            elif x[0] in operators:
                print(int(instructions[0]))
            else:
                print(int(instructions[0]))
    except:
        print("Invalid expression")


user_input = input()
while user_input != "/exit":
    if user_input == "":
        pass
    elif user_input[0] == "/":
        commands(user_input)
    else:
        expression(user_input)
    user_input = input()
print('Bye!')