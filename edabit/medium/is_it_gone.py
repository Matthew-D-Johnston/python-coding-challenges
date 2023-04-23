def find_it(items, name):
  if name in items.keys():
    return name.capitalize() + ' is gone...'
  else:
    return name.capitalize() + ' is here!'

# Example 1
items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
}
name = 'timmy'
print(find_it(items, name))

# Example 2
items = {
  "tv": 30,
  "stereo": 50,
}
name = 'timmy'
print(find_it(items, name))

# Example 3
items = {}
name = 'timmy'
print(find_it(items, name))
