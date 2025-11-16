pattern_size = int(input("Enter the size of the pattern: "))
row = 0

# Outer while loop for rows
while row < pattern_size:
    # Inner for loop for columns
    for col in range(pattern_size):
        print("*", end="")  # print asterisk on the same line
    print()  # move to next line after each row
    row += 1  # go to next row