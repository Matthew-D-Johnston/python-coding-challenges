def list_of_multiples(num, length):
  multiple = 1
  multiples = []

  while multiple <= length:
    multiples.append(num * multiple)
    multiple += 1
  
  return multiples

print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))
