q = int(input())
price = q * 100
if price > 1000:
    print(0.9 * price)
else:
    print(price)