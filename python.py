from decimal import Decimal, getcontext

getcontext().prec = 400
while True:
    print("Choose operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    choice = int(input("Enter choice(1/2/3/4/5): "))

    if choice in (1, 2, 3, 4, 5):
        pass
    else:
        print("Invalid input")
        exit()
    num1 = Decimal(input("Enter first number: "))
    num2 = Decimal(input("Enter second number: "))

    if choice == 1:
        print( num1 + num2)
    elif choice == 2:
        print( num1 - num2)
    elif choice == 3:
        print( num1 * num2)
    elif choice == 4:
        print( num1 / num2)
    elif choice == 5:
        print( num1 ** num2)
    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if again == 'no':
        print("Thanks for using the calculator! Goodbye.")
        break 