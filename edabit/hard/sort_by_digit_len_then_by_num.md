##### Edabit > Python > Hard

---

## Sort by Digit Length, then By Number Itself

#### Problem

##### Instructions:

Write a function that sorts a list of integers by their digit length in **descending order**, then settles ties by sorting numbers with the same digit length in **ascending order**.

##### Definitions/Rules (explicit and implicit):

* Sort list of integers.
* Sort first by digit length in descending order.
* Then sort by number value in ascending order.

##### Input/Output:

* Input: a list of integers.
* Output: the sorted list of integers.

##### Mental Model:

Take the given list of integers and use a sort function to sort by the digit length in descending order and then settles ties by sorting by the value of the integer in ascending order.

---

#### Examples / Test Cases

```python
digit_sort([77, 23, 5, 7, 101])
➞ [101, 23, 77, 5, 7]

digit_sort([1, 5, 9, 2, 789, 563, 444])
➞ [444, 563, 789, 1, 2, 5, 9]

digit_sort([53219, 3772, 564, 32, 1])
➞ [53219, 3772, 564, 32, 1]
```

---

#### Data Structures

##### Input:

* A list of integers.

##### Output:

* A list of integers.

---

#### Algorithm

* Use the `sorted` function.
* Use a lambda function to specify to sort first by digit length in descending order and then by integer value in ascending order.

---

#### Code

```python
def digit_sort(integers):
    return sorted(integers, key=lambda int: (-len(str(int)), int))
```

