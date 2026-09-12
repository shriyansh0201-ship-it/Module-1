name = input("Enter your name: ")
club = input("Enter your club name: ")

member_number = 101
fee = 250.50
active = True

# Convert numbers and Boolean to text
member_number = str(member_number)
fee = str(fee)
active = str(active)

# Create badge code using slicing
badge_code = name[:3] + club[:3]

# Create and print badge
badge = "School Club Member Badge\n"
badge = badge + "Name: " + name + "\n"
badge = badge + "Club: " + club + "\n"
badge = badge + "Member Number: " + member_number + "\n"
badge = badge + "Fee: ₹" + fee + "\n"
badge = badge + "Active: " + active + "\n"
badge = badge + "Badge Code: " + badge_code.upper()

print(badge)