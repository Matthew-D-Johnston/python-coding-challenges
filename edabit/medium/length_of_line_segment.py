import math

def line_length(dot1, dot2):
  x1, y1 = dot1[0], dot1[1]
  x2, y2 = dot2[0], dot2[1]

  return round(math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)), 2)

print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [0, 0]))
print(line_length([0, 0], [1, 1]))
