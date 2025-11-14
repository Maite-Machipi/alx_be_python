# pyramid_art.py
# Program to print a pyramid pattern using nested while loops

rows = 5  # height of the pyramid

# Outer loop controls each row
i = 1
while i <= rows:

    # Print spaces (rows - i)
    spaces = 0
    while spaces < rows - i:
        print(" ", end="")
        spaces += 1

    # Print stars (2*i - 1)
    stars = 0
    while stars < (2 * i - 1):
        print("*", end="")
        stars += 1

    # Move to next line after each row
    print()

    i += 1
