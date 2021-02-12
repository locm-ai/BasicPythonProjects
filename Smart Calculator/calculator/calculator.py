"""
    Finally, we got to the next operation: subtraction. It means that from
now on the program must receive the addition + and subtraction - operators as
an input to distinguish operations from each other. It must support both unary
and binary minus operators. Moreover, If the user has entered several same
operators following each other, the program still should work (like Java or
Python REPL). Also, as you remember from school math, two adjacent minus signs
turn into a plus. The smart calculator ought to have such a feature.

    The program must calculate expressions like these: 4 + 6 - 8, 2 - 3 - 4,
and so on.
    Modify the result of the /help command to explain these operations.
    Decompose your program using functions to make it easy to understand and
edit later.
    The program should not stop until the user enters the /exit command.
    If you encounter an empty line, do not output anything.
"""
user_input = input()
while user_input != "/exit":
    if user_input == "":
        pass
    elif user_input == "/help":
        print("The program calculates the sum of numbers")
    else:
        instructions = user_input.split()
        if len(user_input) > 1:
            print(eval(user_input))
        elif len(user_input) == 1:
            print(user_input[0])
    user_input = input()
print("Bye!")