 
num1 = input("Enter the first number: ")


num2 = input("Enter the second number: ")



# num1.isdigit and 2 checks if the numbers are valid 


if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    
    operation = input("Enter the operation you want to use (mul, div, or mod): ")

    
    if operation == "mul":
        result = num1 * num2
        print("Result:", result)
    elif operation == "div":
        if num2 == 0:
            print("Dividing  by zero is no good .")
        else:
            result = num1 / num2
            print("Result:", result)
    elif operation == "mod":
        if num2 == 0:
            print("Modulo by zero is no good .")
        else:
            result = num1 % num2
            print("Result:", result)
    else:
        print(" *** invalid operation *** ")
