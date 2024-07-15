# Part K
# Number of rows for the half-pyramid
rows = 5

# Outer loop to handle the number of rows
for i in range(1, rows + 1):
    # Inner loop to handle the number of stars
    for j in range(i):
        print("#", end="")

    # Print a newline after each row
    print()