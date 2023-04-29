def square_areas_difference(radius):
  square_one_area = 2 * radius * radius
  square_two_area = (2 * radius) * (2 * radius)

  return square_two_area - square_one_area

print(square_areas_difference(5))
print(square_areas_difference(6))
print(square_areas_difference(7))