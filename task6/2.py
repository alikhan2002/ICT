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