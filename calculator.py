def add(a, b):
    return a+b
def substract(a, b):
    return a-b
def multiply (a, b):
    return a*b
def divide(a, b):
    if b==0:
        return "cannot divide by zero"
    else:
        return a / b 
first_number= int(input("enter first number: "))
second_number= int(input("enter second number: "))
print(add(first_number,second_number))
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Quit")
    choice= input("choose operation")
    if choice =="0":
        print("goodbye!")
        break
    a= int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if choice  =="1":
        print(f"Answer: {add(a, b)}")
    elif choice== "2":
        print(f"Answer: {substract (a, b)}")
    elif choice== "3":
        print(f"Answer: {multiply (a, b)}")
    elif choice== "4":
        print(f"Answer: {divide (a, b)}")