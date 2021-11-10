held = int(input())
att = int(input())
percentage = (att/held)*100
print("Percentage of class attended:", "%.2f"%percentage, end = "%\n")
if(percentage > 75):
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")