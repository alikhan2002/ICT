s = input()
t = s.lower()
res = ""

for i in range(len(s)):
    if i == 0:
        res += s[i].upper()
    else:
        res += t[i]


print(res)
