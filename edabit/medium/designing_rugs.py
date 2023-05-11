def make_rug(m, n, s = '#'):
  rug = []
  row = 1

  while row <= m:
    rug.append(s * n)
    row += 1
  
  return rug


print(make_rug(3, 5, '#'))
print(make_rug(3, 5, '$'))
print(make_rug(2, 2, 'A'))
print(make_rug(4, 3))