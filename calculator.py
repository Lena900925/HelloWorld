while True:
    n1 = input("Enter a number(or a letter to exit): ")
    if n1.isnumeric():
        op = input("Enter an operation: ")
        n2 = input("Enter another number: ")

        if op == "+":
            print("Result: ", int(n1) + int(n2))

        elif op == "-":
            print("Result: ", int(n1) - int(n2))

        elif op == "*":
            print("Result: ", int(n1) * int(n2))

        elif op == "/":
            print("Result: ", int(n1) / int(n2))
        else:
            print("Please enter an operation")
    else:
        exit()