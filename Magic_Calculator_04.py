
def addition(x,y):
    return (x + y)

def subtraction(x,y):
    return (x - y)

def multiplication(x,y):
    return (x * y)

def division(x,y):
    return (x / y)

def magic_calculator():
    for _ in range(3):
        x = int(input("Put your first number: "))
        operator = input("Put the operator that you want: ")
        y = int(input("Put your second number: "))

        #for i range (5)
        if operator == "+":
            results = addition(x,y)
        elif operator == "-":
            results = subtraction(x,y)
        elif operator == "*":
            results = multiplication(x,y)
        elif operator == "/":
            results = division(x,y)
        else:
            print("Error put operator/number again")
            continue
        print(f"{x} {operator} {y} = {results}")
        return results

    
print("Results:", magic_calculator())


