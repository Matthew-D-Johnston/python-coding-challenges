##### Edabit > Python > Hard

---

## Hole Number Sequence

#### Problem

##### Instructions:

What do the digits 0, 4, 6, 8, and 9 have in common? Well, they are whole numbers... and they are also *hole* numbers (not actually a thing until now). Hole numbers are numbers with holes in their shapes (8 is special in that it contains two holes).

14 is a hole number with one hole. 88 is a hole number with four holes.

Your task is to create a function with argument `N` that returns the sum of the holes for the integers *n* in the range of range *0 < n <= N*.

To illustrate, `sum_of_holes(14)` returns `7`, because there are 7 holes in 4, 6, 8, 9, 10 and 14.

_Notes_

- All test cases are positive real integers.
- Don't forget that 8 has two holes.

##### Definitions/Rules (explicit and implicit):

* Hole numbers: 0, 4, 6, 8, and 9
* 8 has two holes.
* Range of *N*: 0 < n <= N

##### Input/Output:

* Input: a positive real integer.
* Output: the count of the number of holes in the numbers that make up the range from 1 to the given number, inclusive.

##### Mental Model:

Take the given number. Iterate over the range of integers from 1 until the given number. Find all digits that match either 0, 4, 6, or 9. Store the matches in a single holes variable. Find all the 8s in the number and store those in a separate eights list. After going through all numbers in the range, count the length of the single holes list. Add it to double the length of the eights list.

---

#### Examples / Test Cases

```python
sum_of_holes(4)
# => 1

sum_of_holes(6)
# => 2

sum_of_holes(8)
#=> 4

sum_of_holes(6259)
# => 12345
```

---

#### Data Structures

##### Input:

* An integer.

##### Output:

* An integer.

---

#### Algorithm

* `import re` (import the regex module)
* Declare a `single_holes` variable and set it equal to an empty list.
* Declare an `eights` variable and set it equal to an empty list.
* Declare a `single_hole_pattern` variable and set it equal to `re.compile('[0469]')`
* Declare an `eight_pattern` variable and set it equal to `re.compile('8')`
* Initiate a `for` loop that iterates from `1` to the `number`; `for num in range(number)`
* For each `num`, declare a `single_hole_matches` variable and set it equal to `single_hole_pattern.findall(num)`.
* Then concatenate the `single_hole_matches` list to the `single_holes` list.
* Do the same thing with an `eights_mathces` list and the `eights` list.
* After the loop finishes, find the length of both lists.
* Multiply the length of the `eights` list by 2 and then add it to the length of the `single_holes` list.

---

#### Code

```python
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
```

