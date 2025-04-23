import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    """
    Generates N_NUMBERS random numbers between MIN_VALUE and MAX_VALUE,
    prints them, and calculates their sum.
    """
    # Generate list of random numbers
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Print the numbers
    print("Generated numbers:", numbers)
    
    # Calculate and print the sum
    total = sum(numbers)
    print("Sum of numbers:", total)

if __name__ == '__main__':
    main()