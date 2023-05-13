def sum_of_vowels(text):
  values = { 'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 0 }
  vowels = ['a', 'e', 'i', 'o', 'u']
  sum = 0

  for char in text:
    lowercase_char = char.lower()

    if lowercase_char in vowels:
      sum += values[lowercase_char]
  
  return sum

print(sum_of_vowels("Let\'s test this function."))
print(sum_of_vowels("Do I get the correct output?"))
print(sum_of_vowels("I love edabit!"))
