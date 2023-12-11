def is_prime(num):  # function to checks if a given number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def validate_start(number):  # function to validates the starting number
    if number < 0:
        print("Enter a non-negative number.")
        return False
    elif number == 0:
        print("Program terminated.")
        exit()
    else:
        return True


def validate_end(start, end):  # function to validates the ending number
    if end <= start:
        print(f"Enter a number greater than {start}.")
        return False
    else:
        return True


def display_primes(start, end):  # function to display prime numbers within a range
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()  # new line at the end


def main():  # main program
    print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
    print("Created by: Per Virgil B. Wabe")
    print("\nProblem: Create a Python program that displays all prime numbers within a range:")
    print("\n RULES TO CONSIDER:")
    print(
        "[1] If number [start] is a negative number. The program will prompt a message: 'Enter a non-negative number' ")
    print(
        "[2] If number [end] is less than number [start]. The program will prompt a message 'Enter a number greater than number [start]'")
    print("[3] If the user enter the number '0', the program will terminate. ")

    while True:
        valid_start = False
        while not valid_start:
            start = int(input("\nEnter a number [start]: "))
            valid_start = validate_start(start)

        valid_end = False
        while not valid_end:
            end = int(input(f"Enter a number greater than {start}: "))
            valid_end = validate_end(start, end)

        display_primes(start, end)


if __name__ == "__main__":
    main()
