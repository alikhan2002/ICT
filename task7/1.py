from typing import final


print("Choose size of pizza")
size = input("S\nM\nL\n")

final_bill = 0
if size == 'S':
    final_bill += 15
elif size == 'M':
    final_bill += 20
elif size == 'L':
    final_bill += 25

add = input("add_pepperoni?\nY\nN\n")

if add == 'Y' and size == 'S':
    final_bill += 2
elif add == 'Y' and (size == 'M' or size == 'L'):
    final_bill += 3

cheese = input("Do you wanna extra cheese?\nY\nN\n")

if cheese == 'Y':
    final_bill += 1

print("Your final bill is:", final_bill)