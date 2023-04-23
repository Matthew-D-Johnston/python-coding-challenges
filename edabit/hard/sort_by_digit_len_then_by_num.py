def digit_sort(integers):
    return sorted(integers, key=lambda int: (-len(str(int)), int))

print(digit_sort([77, 23, 5, 7, 101]))
print(digit_sort([1, 5, 9, 2, 789, 563, 444]))
print(digit_sort([53219, 3772, 564, 32, 1]))

