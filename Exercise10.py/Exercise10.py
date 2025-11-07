def is_even(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    number = int(input("Enter a number: "))
    print(is_even(number))

if __name__ == "__main__":
    main()