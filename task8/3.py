l = map(int, input().split())

for i in l:
    if i > 300:
        break
    elif i > 120:
        continue
    elif i % 3 == 0:
        print(i)