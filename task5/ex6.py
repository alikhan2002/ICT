tax = 0.1
tip = 0.18
cost = float(input())

tax = tax * cost
tip = tip * cost

tot = tax + tip + cost

print("tax:", "%.2f" % tax)
print("tip:", "%.2f" % tip)
print("total:", "%.2f" % tot)