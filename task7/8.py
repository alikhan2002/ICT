a = int(input())
b = int(input())
c = int(input())
x = min(min(a, b), c)
y = max(max(a, b), c)
print("Oldest is", y)
print("Yongest is", x)

