# pattern_drawing.py
# Program to draw a square pattern using a while loop and a nested for loop

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for each row
while row < size:

    # Inner for loop to print asterisks for each column
    for col in range(size):
        print("*", end="")

    # Move to the next line after a row is complete
    print()

    row += 1
