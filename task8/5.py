n = int(input())
l = [None] * n
l[0] = 0
l[1] = 1

for i in range(2, n, 1):
    l[i] = l[i - 1] + l[i - 2]

for i in l:
    print(i, end = " ")