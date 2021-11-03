n = int(input())
s = input()
t = s
x = 0
for i in range(len(s)):
    if s[i] == 'x':
        x += 1
        if(x >= 3):
            t = t.replace('x', '', 1)
    else:
        x = 0
print(len(s) - len(t))
    