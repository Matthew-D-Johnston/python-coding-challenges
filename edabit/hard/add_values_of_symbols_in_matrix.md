##### Edabit > Python > Hard

---

## Add the Values of the Symbols in a Matrix

#### Problem

##### Instructions:

Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

- `#` = 5
- `O` = 3
- `X` = 1
- `!` = -1
- `!!` = -3
- `!!!` = -5

A list of lists containing 2 `#`s, a `O`, and a `!!!` would equal (0 + 5 + 5 + 3 - 5) 8.

If the final score is negative, return `0` (e.g. 3 `#`s, 3 `!!`s, 2 `!!!`s and a `X` would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return `0`.

_Notes_

Strings in the lists will only be `#`, `O`, `X`, `!`, `!!` and `!!!`.

##### Definitions/Rules (explicit and implicit):

* Symbols are contained in nested arrays.
* If the final score is negative, return `0`.

##### Input/Output:

* Input: A matrix containing symbols.
* Output: the final score after adding up the scores associated with each symbol.

##### Mental Model:

Create a dictionary of the symbols and associated values. Declare a score variable and set it to 0. Iterate over each row (i.e. list) of the matrix (i.e. outer list). Then iterate over each element of each row. Use the dictionary to look up the value of the given symbol. Add the value to the score. After all iterations have completed, check to see if the final score is negative. If so, return 0. Otherwise, simply return the final score.

---

#### Examples / Test Cases

```python
check_score([
  ["#", "!"],
  ["!!", "X"]
]) ➞ 2

check_score([
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
]) ➞ 0

check_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]) ➞ 12
```

---

#### Data Structures

##### Input:

* A list of nested lists, which contain strings.

##### Output:

* An integer.

---

#### Algorithm

* Declare a `symbol_values` variable and assign it to a dictionary of the symbols and their associated values.
* Declare a `score` variable and set it equal to `0`.
* Initiate a `for` loop to loop over the nested lists of the primary list.
* Initiate another `for` loop to loop over the symbols in each of the nested lists.
* Use the `symbol_values` dictionary to look up the value of each symbol.
* Add that symbol to the `score` variable.
* After all the loops have completed, check to see if `score < 0`.
* If it is, then return `0`.
* Otherwise, return `score`.

---

#### Code

```python
def check_score(matrix):
    symbol_values = {
      '#': 5,
      'O': 3,
      'X': 1,
      '!': -1,
      '!!': -3,
      '!!!': -5
    }
    score = 0

    for row in matrix:
        for symbol in row:
            score += symbol_values[symbol]
    
    if score < 0:
        return 0
    else:
        return score
```

