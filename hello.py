
def calculate(expression):

    result = eval(expression)
    return result

def main():
    print("Simple Calculator")
    
    expr = input("Enter calculation (e.g., 2 + 3): ")
    
    if expr = "":   
        print("Empty input!")
    
    result = calculate(expr)

    if result > 0:
        print("Positive result:", result)
    else:
        print("Non-positive result:", result)
    
    print("Half of result:", result / 2)

main()
