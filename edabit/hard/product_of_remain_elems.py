from functools import reduce

def can_partition(integers):
    for integer in integers:
        integers_copy = integers.copy()
        integers_copy.remove(integer)
        product = reduce(lambda x, y: x * y, integers_copy)

        if integer == product:
            return True
    
    return False

print(can_partition([2, 8, 4, 1]))
print(can_partition([-1, -10, 1, -2, 20]))
print(can_partition([-1, -20, 5, -1, -2, 2]))
