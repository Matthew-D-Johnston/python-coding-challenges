import re

def sum_of_holes(number):
    single_holes = []
    eights = []

    single_hole_pattern = re.compile('[0469]')
    eight_pattern = re.compile('8')

    for num in range(1, number + 1):
        single_hole_matches = single_hole_pattern.findall(str(num))
        eight_matches = eight_pattern.findall(str(num))

        single_holes += single_hole_matches
        eights += eight_matches

    return len(single_holes) + (2 * len(eights))

print(sum_of_holes(4))
print(sum_of_holes(6))
print(sum_of_holes(8))
print(sum_of_holes(11))
print(sum_of_holes(6259))
