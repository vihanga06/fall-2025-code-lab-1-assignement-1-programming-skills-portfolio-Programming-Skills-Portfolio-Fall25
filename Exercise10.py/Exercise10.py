def is_even(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    user_input = int(input("Enter a number: "))
    print(is_even(user_input))

if __name__ == "__main__":
    main()