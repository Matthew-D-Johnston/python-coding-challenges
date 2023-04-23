##### Edabit > Python > Hard

---

## Smallest Square Ending

#### Problem

##### Instructions:

In a letter to Lord Bowden in 1837, Charles Babbage asked, "What is the smallest positive integer whose square ends in 269,696?". He thought the answer was 99,736 whose square is 9,947,269,696. Was he right?

Write a function that takes a positive integer `n` and returns the smallest number whose square ends with `n`. One small twist, if `n == 269696` return `"Babbage was correct!"` if the smallest number whose square ends with 269,696 is 99,736, otherwise return `"Babbage was incorrect!"`.

_Notes_

- `n` will always be a positive integer `n > 0`.
- Make sure your solution is efficient enough to pass the tests within a 12 second time limit.

##### Definitions/Rules (explicit and implicit):

* Return smallest number whose square ends with `n`.
* However, if `n` is equal to `269696`, return `"Babbage was correct!"` if the smallest number whose square ends with 269,696 is 99,736. Otherwise, return `"Babbage was incorrect!"`.

##### Input/Output:

* Input: a positive integer, `n`.
* Output: the smallest number whose square ends in `n`.

##### Mental Model:

Take the given integer `n`. Take its square root. If the square root is a positive integer, return that integer. Otherwise, take the number of digits in `n` and multiply that by a stringed `0`. Then append those zeros to a `1` and convert to an integer. Add that integer to `n` and take the square again. Keep taking the square until the square is an integer. Once the square is a positive integer, return that integer unless `n` is equal to `269696`. If that is the case, check if the positive integer is `99736`. If so, return `"Babbage was correct!"`. Otherwise, return `"Babbage was incorrect!"`.

---

#### Examples / Test Cases

```python
babbage(25) ➞ 5

babbage(161) ➞ 119
# 119 * 119 == 14,161
# Ends with 161

babbage(269696) ➞ "Babbage was {?}!"
# Replace {?} with the word "correct" or "incorrect".
```

---

#### Data Structures

##### Input:

* A positive integer.

##### Output:

* A positive integer or a string.

---

#### Algorithm

* Take the given integer `n`.
* Convert `n` to a string and find its length. Store in variable named `digits`.
* Declare a `multiplier` variable and set it equal to the conversion of `"1" + (digits * "0")` into an integer.
* Declare a variable named `square` and set it equal to `n`.
* Declare a variable called `square_root` and set it to the square root of `n`.
* Initiate a `while` loop with the following condition, `square_root / 1 != square_root // 1`
  * Within the loop, set `square` equal to `square + multiplier`.
  * Set `square_root` equal to the square_root of `square`.
* Once the loop completes, check to see if `n == 269696`
* If so,
  * check to see if `square_root == 99736`
  * if so,
    * return `"Babbage was correct!"`
  * if not,
    * return `"Babbage was incorrect!"`
* If not,
  * return `square_root`.

---

#### Code

```python
import math

def babbage(n):
    digits = len(str(n))
    multiplier = int('1' + (digits * '0'))
    square = n
    square_root = math.sqrt(square)

    while square_root / 1 != square_root // 1:
        square += multiplier
        square_root = math.sqrt(square)
    
    if n == 269696:
        if square_root == 99736:
            return "Babbage was correct!"
        else:
            return "Babbage was incorrect!"
    else:
        return square_root
```

