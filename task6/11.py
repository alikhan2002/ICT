m = int(input())

s = input()

z = 0
e = 0
r = 0
o = 0
n = 0
res = ""
for i in s:
    if(i == 'z'):
        z += 1
    if(i == 'e'):
        e += 1
    if(i == 'r'):
        r += 1
    if(i == 'o'):
        o += 1
    if(i == 'n'):
        n += 1
# search ones
for i in range(len(s)):
    if(o > 0 and n > 0 and e > 0 ):
        o -= 1
        n -= 1
        e -= 1
        res += "1 "
# search zeros
for i in range(len(s)):
    if(z > 0 and e > 0 and r > 0 and o > 0):
        z -= 1
        r -= 1
        e -= 1
        o -= 1
        res += "0 "

print(res)
