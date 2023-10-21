MyVar = input("What is your answer to my 1st question? (yes/no) ")

if myVar == "yes":
    myNextVar = input("What is your answer to my 2nd question? (yes/no) ")
    
    if myNextVar == "yes":
        
        myThirdVar = input("What is your answer to my 3rd question? (yes/no) ")
        
        if myThirdVar == "yes":
            print("Outcome of the 3rd 'yes' condition")
        elif myThirdVar == "no":
            print("Outcome of the 3rd 'no' condition")
        else:
            print("Answer my question! You didn't type yes or no for the 3rd question.")
    
    elif myNextVar == "no":
        
        print("Outcome of the 2nd 'no' condition")
    else:
        print("Answer my question! You didn't type yes or no for the 2nd question.")

elif myVar == "no":
    
    print("Outcome of the 2nd 'no' condition")
    
else:
    print("Answer my question! You didn't type yes or no for the 1st question.")
    #  I filled in the right variable names and consequences, then used  nesting conditions 