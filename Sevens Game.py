def skip_sevens():
    for number in range(101):  # 101 because range is exclusive of the stop value
        if '7' in str(number) or number % 7 == 0:
            continue  # Skip the number if it contains '7' or is divisible by 7
        print(number)

# Run the game
skip_sevens()