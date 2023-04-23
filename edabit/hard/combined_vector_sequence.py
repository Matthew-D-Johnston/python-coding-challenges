def has_consecutive_series(v1, v2):
    length_difference = len(v1) - len(v2)

    if length_difference > 0:
        v2 += length_difference * [0]

    if length_difference < 0:
        v1 += (-1 * length_difference) * [0]

    sequence = []
    for index in range(len(v1)):
        sequence.append(v1[index] + v2[index])
    
    for index in range(len(sequence) - 1):
        if sequence[index] != (sequence[index + 1] - 1):
            return False
    
    return True


print(has_consecutive_series([3, 5, 1, -5], [4, 3, 8, 15]))
print(has_consecutive_series([2, 2, 2], [5, 6, 7, 10]))
print(has_consecutive_series([4, 2, 8, 5], [14, 2, 4, 9]))
