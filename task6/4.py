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
