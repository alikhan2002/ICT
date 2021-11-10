n = int(input())

if(n < 0 or n > 100):
    print("Please, type correct mark")
elif n < 25:
    print("F")
elif n >= 25 and n < 45:
    print("E")
elif n >= 45 and n < 50:
    print("D")
elif n >= 50 and n < 60:
    print("C")
elif n >= 60 and n <= 80:
    print("B")
elif n > 80:
    print("A")
