def dis(price, discount):
  return round(price - (price * (discount / 100)), 2)

print(dis(1500, 50))
print(dis(89, 20))
print(dis(100, 75))