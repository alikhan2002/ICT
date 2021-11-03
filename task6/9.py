s = input()

anton = 0
danik = 0

for i in s:
    if i == 'A':
        anton += 1
    else:
        danik += 1

if danik == anton:
    print("Friendship")
elif anton > danik:
    print("Anton")
else:
    print("Danik")