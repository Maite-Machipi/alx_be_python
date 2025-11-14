# sum_list.py
# Program to calculate the sum of numbers in a list using a for loop

numbers = [1, 5, 3, 9]   # Step 1: create a list of numbers
total = 0                # Step 2: initialize running sum

# Step 3: loop through the list
for num in numbers:
    total += num         # Step 4: add each number to total

# Step 5: print the sum
print(f"The total sum is: {total}")
