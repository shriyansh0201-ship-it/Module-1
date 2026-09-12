team1 = 20
team2 = 25
team3 = 30

# Total
total = team1 + team2 + team3
print("Total points:", total)

# Average
average = total / 3
print("Average points:", average)

# Reward stars
stars = 14
boxes = stars // 4
leftover = stars % 4

print("Full boxes:", boxes)
print("Leftover stars:", leftover)

# Compare scores
last_week = 65

print("This week is greater:", total > last_week)
print("This week is equal:", total == last_week)
print("This week is less:", total < last_week)

# Assignment operators
total += 5
print("After +5:", total)

total -= 2
print("After -2:", total)