def sum_odd_and_even(numbers):
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return [even_sum, odd_sum]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
