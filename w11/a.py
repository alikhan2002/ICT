s = input()
res = True
len = int(len(s))
for i in range(int(len / 2)):
    if s[i] != s[len - i - 1]:
        res = False
        break

if res:
    print("String is a palindrome!")
else:
    print("String is not a palindrome!")

