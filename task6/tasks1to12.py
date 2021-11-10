#1
s = input()
s = s.lower()
a = ""
for i in s:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y'):
        s = s.replace(i, "")

for i in s:
    if(i != 'a' or i != 'e' or i != 'i' or i != 'o' or i != 'u' or i != 'y'):
        a += "."
        a += i

print(a)

#2
s = input()

l = list()
res = ""
for i in s:
    if i >= '0' and i <= '9':
        l.append(int(i))

l.sort()
for i in range(len(l)):
    if(i != len(l) - 1):
        res += str(l[i])
        res += '+'
    else:
        res += str(l[i])

print(res)

#3
s = input()
res = ""
if(s[0].isupper() == False):
    res += s[0].upper()
else: res += s[0]
for i in range(1, len(s)):
    res += s[i]
print(res)


#4
s = input()

zeros = 0
ones = 0
res = False
for i in s:
    if(i == '0'):
        zeros += 1
        ones = 0
    if(i == '1'):
        ones += 1
        zeros = 0
    if(ones >= 7 or zeros >= 7):
        res = True
if(res):
    print("YES")
else:
    print("NO")

#5
s = input()

s = set(s)
# s = list(s)
if(len(s)%2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

#6
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


#7
n = int(input())
s = input()
s = s.lower()
s = set(s)
if(len(s) >= 26):
    print("YES")
else:
    print("NO")

#8
s = input()

t = input()

res = ""
for i in range(len(t) - 1, -1, -1):
    res += s[i]

if(res == t):
    print("YES")
else:
    print("NO")

#9
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

#10
s = input()
t = s.lower()
res = ""

for i in range(len(s)):
    if i == 0:
        res += s[i].upper()
    else:
        res += t[i]


print(res)


#11
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

#12
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
    