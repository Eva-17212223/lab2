from src.utils import add, subtract, multiply, divide



def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter your choice (1-4): ")

        if choice not in ('1', '2', '3', '4'):
            print(
                "Invalid choice. Please enter a number "
                "between 1 and 4."
            )
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    operation = "Division"
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
                    continue

            print(f"{operation} result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue

        again = input(
            "Do you want to perform another calculation? (y/n): "
        ).lower()
        if again != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
