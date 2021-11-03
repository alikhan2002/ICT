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