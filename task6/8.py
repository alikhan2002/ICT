s = input()

t = input()

res = ""
for i in range(len(t) - 1, -1, -1):
    res += s[i]

if(res == t):
    print("YES")
else:
    print("NO")