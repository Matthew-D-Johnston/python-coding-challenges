def number_length(num):
  string_num = str(num)

  count = 0

  for char in string_num:
    count += 1

  return count

print(number_length(10))
print(number_length(5000))
print(number_length(0))