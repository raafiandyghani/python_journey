    x = int(input("Put your first number: "))
        operator = input("Put the operator that you want: ")
        y = int(input("Put your second number: "))

        #for i range (5)
        if operator == "+":
            results = addition(x,y)
        elif operator == "-":
            results = subtraction(x,y)
        if operator == "*":
            results = multiplication(x,y)
        elif operator == "/":
            results = division(x,y)
        else:
            print("Error put operator/number again")
            continue
        return results