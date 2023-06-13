def normalize(txt):
  if txt == txt.upper():
    lowercased = txt.lower()
    capitalized = lowercased.capitalize()
    return capitalized + '!'
  
  return txt

print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
print(normalize("Let us stay calm, no need to panic."))