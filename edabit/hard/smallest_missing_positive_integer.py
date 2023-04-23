def min_miss_pos(integers):
    max_integer = len(integers) + 1
    current_integer = 1

    while current_integer <= max_integer:
        if current_integer not in integers:
            return current_integer
        
        current_integer += 1


print(min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2]))
print(min_miss_pos([5, 9, -2, 0, 1, 3, 9, 3, 8, 9]))
print(min_miss_pos([0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9]))
