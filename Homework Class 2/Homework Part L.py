# Part L
# Creating an X shape using nested for loop (width and length is 7)
size = 7
for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()  # Newline after each row