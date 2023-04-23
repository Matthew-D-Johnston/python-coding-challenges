##### Edabit > Python > Hard

---

## The Snake—Area Filling

#### Problem

##### Instructions:

This challenge is based on the classic videogame "Snake".

Assume the game screen is an `n * n` square, and the snake starts the game with length `1` (i.e. just the head) positioned on the top left corner.

For example, if `n = 7` the game looks something like this:

![img](https://edabit-challenges.s3.amazonaws.com/glbiwtu.png)

In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).

Create a function that takes the side `n` of the game screen and returns ***the number of times the snake can eat before it runs out of space*** in the game screen.

_Notes_

The given number will always be a positive integer (there are no exceptions to handle).

##### Definitions/Rules (explicit and implicit):

* The game screen is an `n * n` square.
* The snake starts with a length of 1, taking up a single `1*1` block of the game screen.
* The length of the snake doubles each time it eats food ...
  * The 1st time it eats, it doubles to length 2 (1*2^1)
  * The 2nd time it eats, it doubles to length 4 (1*2^2)
  * The 3rd time it eats, it doubles to length 8 (1*2^3)
  * The nth time it eats, it doubles to length 2^n.
* Total number of squares equals `n * n`.
* The given number, `n`, will always be a positive integer.

##### Input/Output:

* Input: the length of one of the sides of the game screen.
* Output: the number of times the snake can eat before it runs out of space on the game screen.

##### Mental Model:

Take the given length of the side of the game screen and square it to find the total number of squares on the game screen. We need to find the max value of `2^x` so that it is still less than the total number of squares. `x` represents the number of times the snake eats.

---

#### Examples / Test Cases

```python
snakefill(3)
# => 3

snakefill(6)
# => 5

snakefill(24)
# => 9

snakefill(1)
# => 0
```

---

#### Data Structures

##### Input:

* A positive integer.

##### Output:

* An integer.

---

#### Algorithm

* We can obtain the result we're looking for by solving the equation `n^2 = 2^x`.
* We take the natural log of both sides `ln(n^2) = ln(2^x)`.
* Which we can then write as, `ln(n^2) = x*ln(2)`, or `x = ln(n^2) / ln(2)`
* We want to use floored division however, since `x` must be the max integer that solves the equation.

---

#### Code

##### Solution #1

```python
import math

def snakefill(side_length):
    total_game_squares = side_length ** 2
    return math.log(total_game_squares) // math.log(2)
```

This solution did not pass edabit's tests.

##### Solution #2

```python
def snakefill(side_length):
    game_squares_remaining = (side_length ** 2) - 1
    times_snake_eats = 0

    while game_squares_remaining > 0:
        times_snake_eats += 1
        game_squares_remaining -= 2 ** times_snake_eats

    return times_snake_eats
```

This solution passed the tests.