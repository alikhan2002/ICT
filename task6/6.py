upper = 0
lower = 0
s = input()

for i in s:
    if i.islower():
        lower += 1
    else:
        upper += 1

if lower >= upper:
    s = s.lower()
else:
    s = s.upper()

print(s)