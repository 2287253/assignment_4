def main():
    print("Temprature in Fahrenheit! :)")
    Fahrenheit= float(input("Eter the temprature in fahrenheit:" ))
    celsius=(Fahrenheit -32) * 5.0/9.0
    print(f"Temprature:{Fahrenheit}f={celsius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()