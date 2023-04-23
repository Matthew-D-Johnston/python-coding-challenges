def stutter(word):
  return ((word[0:2] + '... ') * 2) + word + '?'

print(stutter('incredible'))
print(stutter('enthusiastic'))
print(stutter('outstanding'))
