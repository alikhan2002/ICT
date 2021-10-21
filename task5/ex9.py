money = float(input())

percent = 0.04
money = percent * money + money
print("first year:","%.2f" % money)
money = percent * money + money
print("second year:","%.2f" % money)
money = percent * money + money
print("third year:","%.2f" % money)