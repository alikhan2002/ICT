start = int(input())
end = int(input())

for i in range(start, end + 1, 1):
    flag = True
    j = 2
    if i > 1:
        while(j * j <= i):
            if i % j == 0:
                flag = False
                break
            j += 1
    if flag and i > 1:
        print(i)
