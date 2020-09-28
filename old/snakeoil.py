amount = 16
price = 17
shipping = 0
total = 0
if amount < 10:
    price += 20 # shipping 20
    total = price * amount
elif amount >= 10 and amount <= 100:
    shipping += 500
    total = (price * amount) + shipping
else:
    total = price * amount
    total *= 0.97

print(total)