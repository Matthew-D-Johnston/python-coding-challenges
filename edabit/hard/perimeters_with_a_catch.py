def perimeter(letter, number):
    perimeters = [6.28 * number, 4 * number]
    index = (letter > 'm') + 0
    return perimeters[index]

print(perimeter('s', 7))
print(perimeter('c', 4))
print(perimeter('c', 9))

