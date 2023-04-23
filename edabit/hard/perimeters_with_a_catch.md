##### Edabit > Python > Hard

---

## Perimeters with a Catch

#### Problem

##### Instructions:

Write a function that takes a number and returns the perimeter of either a circle or a square. The input will be in the form (letter `l`, number `num`) where the letter will be either `"s"` for *square*, or `"c"` for *circle*, and the number will be the side of the square or the radius of the circle.

Use the following formulas:

- Perimeter of a square: 4 * side.
- Perimeter of a circle: 6.28 * radius.

The catch is you can only use **arithmetic** or **comparison operators**, which means:

- No if... else statements.
- No dictionaries.
- No lambdas.
- No formatting methods, etc.

The goal is to write a short, [branch-free](https://en.wikipedia.org/wiki/Branch_(computer_science)#Branch-free_code) piece of code.

_Notes_

- No rounding is needed.
- Hint: The Boolean `True`, used with arithmetic operators, counts as `1`, while `False` counts as `0`. That means *(a>b)+1* will return *1* or *2*, depending on the values of *a* and *b*.

##### Definitions/Rules (explicit and implicit):

* Perimter of square: 4 * side
* Perimeter of a circle: 6.28 * radius
* Only use arithmetic or comparison operators.

##### Input/Output:

* Inputs: a letter and a number
* The letter is either an `'s'`, for square, or `'c'`, for circle.
* The number acts either as the side of a square or the radius of a circle depending on which letter is input.
* Output: a number representing the calculation of the perimeter of a square or a circle.

##### Mental Model:

Take the given letter and use the given letter in a comparison with some arbitrary letter of the alphabet between 's' and 'c'. Then add the result of the comparison to 0 to force the boolean value returned by the comparison to either a 1 or 0. Then use the index to obtain either the formula for the perimter of a square or the perimeter of a circle contained in a 2-element list.

---

#### Examples / Test Cases

```python
perimeter("s", 7)
# => 28

perimeter("c", 4)
# => 25.12

perimeter("c", 9)
# => 56.52
```

---

#### Data Structures

##### Input:

* A string and a number.

##### Output:

* A float.

---

#### Algorithm

* Declare a `perimeters` variable and set it to `[perimeter of a circle, perimeter of a square]`.
* Declare an `index` variable and set it to `(letter > s) + 0`.
* Return the value of `perimeters[index]`.

---

#### Code

```python
def perimeter(letter, number):
    perimeters = [6.28 * number, 4 * number]
    index = (letter > 'm') + 0
    return perimeters[index]
```

