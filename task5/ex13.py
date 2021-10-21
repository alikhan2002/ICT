penny = 1
nickels = 5
dimes = 10
quarters = 25
loonies = 100
toonies = 200
#one cent = one penny
cent = int(input())

if cent < 5:
    print("penny:", cent)
elif cent >= 5 and cent < 10:
    print("nickels:", 1, "penny:", cent - 5)

