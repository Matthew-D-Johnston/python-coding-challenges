import math

# Solution 1

# def snakefill(side_length):
#     total_game_squares = side_length ** 2
#     return math.log(total_game_squares) // math.log(2)

# print(snakefill(3))
# print(snakefill(6))
# print(snakefill(7))
# print(snakefill(24))
# print(snakefill(1))


# Solution 2

def snakefill(side_length):
    game_squares_remaining = (side_length ** 2) - 1
    times_snake_eats = 0

    while game_squares_remaining > 0:
        times_snake_eats += 1
        game_squares_remaining -= 2 ** times_snake_eats

    return times_snake_eats


print(snakefill(3))
print(snakefill(6))
print(snakefill(7))
print(snakefill(8))
print(snakefill(24))
print(snakefill(1))

