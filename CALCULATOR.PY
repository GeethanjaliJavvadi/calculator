#define  function for addition operation

def addition(x, y):
    return x + y

#define function for subtraction operation

def subtraction(x, y):
    return x - y

#define function for multiplication operation

def multiplication(x, y):
    return x * y

#define function for division opration

def division(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y
        
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#enter the choice to select the operation to be performed

while True:
    choice = input("Enter choice (1/2/3/4): ")

#enter the numbers to perform opration

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Result:", multiplication(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
            
    else:
        print("Invalid input")
        break


        
        