try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator cannot be 0. Please enter a new denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. ValueError will occur when an input that is not an integer is made.
# 2. Zerodivision error will occur when a number is divided by 0, which will happen if the denominator is 0.
# 3. Yes