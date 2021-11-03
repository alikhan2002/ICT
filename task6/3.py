s = input()
res = ""
if(s[0].isupper() == False):
    res += s[0].upper()
else: res += s[0]
for i in range(1, len(s)):
    res += s[i]
print(res)