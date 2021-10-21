print("Do you use inches and pounds?" )
print("Yes or No ?")
ans = input()
if ans == "Yes":
    h = float(input())
    w = float(input())
    BMI = (w / h**2) * 703
    print("BMI is","%.1f" % BMI)
else:
    h = float(input())
    w = float(input())
    BMI = (w / h**2)
    print("BMI is","%.1f" % BMI)


