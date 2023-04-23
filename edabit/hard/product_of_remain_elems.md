##### Edabit > Python > Hard

---

## Product of Remaining Elements

#### Problem

##### Instructions:

Write a function that returns `True` if you can partition a list into **one element and the rest**, such that this element is equal to the **product** of all other elements **excluding itself**.

_Notes_

- The list may contain duplicates.
- Multiple solutions can exist, any solution is sufficient to return `True`.

##### Definitions/Rules (explicit and implicit):

* Partitionable: any single element is equal to the product of the remaining elements.

##### Input/Output:

* Input: a list of integers.
* Output: `True` if the list can be partitioned; otherwise `False`.

##### Mental Model:

Take the given list. Iterate over each element in the list. For each element, create a copy of the list. Then remove that number from the copied list. Find the product of the remaining elements in the list. If the product is equal to the current element, return `True`. If after iterating through the list, `True` was not returned, return `False`.

---

#### Examples / Test Cases

```python
can_partition([2, 8, 4, 1]) ➞ True
# 8 = 2 x 4 x 1

can_partition([-1, -10, 1, -2, 20]) ➞ False

can_partition([-1, -20, 5, -1, -2, 2]) ➞ True
```

---

#### Data Structures

##### Input:

* A list of integers.

##### Output:

* A boolean value.

---

#### Algorithm

* Initiate a `for` loop to loop over each integer in the list.
  * Inside the loop, declare a `list_copy` variable and assign it to a copy of the list.
  * Remove the current integer from the `list_copy`.
  * Multiply the remaining integers within the `list_copy`.
  * Check if the product is equal to the current integer.
  * If so, return `True`
* If the loop completes and `True` was never returned, then return `False`.



---

#### Code

```python
from functools import reduce

def can_partition(integers):
    for integer in integers:
        integers_copy = integers.copy()
        integers_copy.remove(integer)
        product = reduce(lambda x, y: x * y, integers_copy)

        if integer == product:
            return True
    
    return False
```

