def divisible_by_b(a, b):
  num = a + 1

  while num % b != 0:
    num += 1

  return num

print(divisible_by_b(17, 8))
print(divisible_by_b(98, 3))
print(divisible_by_b(14, 11))
