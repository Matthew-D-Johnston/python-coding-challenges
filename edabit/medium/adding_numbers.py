def add(str1, str2):
  if str1 == None or str2 == None:
    return "Invalid Operation"
  elif len(str1) == 0 or len(str2) == 0:
    return "Invalid Operation"
  
  return str(int(str1) + int(str2))

print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))