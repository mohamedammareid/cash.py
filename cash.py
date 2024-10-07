from cs50 import get_float

# Get a valid input from the user
while True:
    change_owed = get_float("Change owed: ")
    if change_owed >= 0:
        break

# Convert dollars to cents
change_owed_cents = round(change_owed * 100)

num_coins = 0

# Calculate the minimum number of coins
while change_owed_cents > 0:
    if change_owed_cents >= 25:
        change_owed_cents -= 25
        num_coins += 1
    elif change_owed_cents >= 10:
        change_owed_cents -= 10
        num_coins += 1
    elif change_owed_cents >= 5:
        change_owed_cents -= 5
        num_coins += 1
    else:
        change_owed_cents -= 1
        num_coins += 1

# Output the result
print(num_coins)
