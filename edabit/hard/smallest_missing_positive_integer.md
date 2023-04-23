##### Edabit > Python > Hard

---

## Smallest Missing Positive Integer

#### Problem

##### Instructions:

Given a list of integers, return the smallest *positive* integer *not present in the list*.

Here is a representative example. Consider the list:

```
[-2, 6, 4, 5, 7, -1, 7, 1, 3, 6, 6, -2, 9, 10, 2, 2]
```

After reordering, the list becomes:

```
[-2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7, 9, 10]
```

... from which we see that the smallest missing positive integer is `8`.

_Notes_

For the sake of clarity, recall that `0` is not considered to be a positive number.

##### Definitions/Rules (explicit and implicit):

* Return smallest positive integer not present in the list.
* 0 is not considered a positive number.
* List is comprised of both positive and negative integers.

##### Input/Output:

* Input: A list of integers.
* Output: the smallest missing positive integer.

##### Mental Model:

Take the given list of integers. Find out how many integers are in the list. Loop over the total number of integers and check to see if each one, starting at 1, is included in the list. If it is not, then return that number.

---

#### Examples / Test Cases

```python
min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2]) ➞ 8
# After sorting, list becomes [-2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 9, 10]
# So the smallest missing positive integer is 8

min_miss_pos([5, 9, -2, 0, 1, 3, 9, 3, 8, 9]) ➞ 2
# After sorting, list becomes [-2, 0, 1, 3, 3, 5, 8, 9, 9, 9]
# So the smallest missing positive integer is 2

min_miss_pos([0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9]) ➞ 1
# After sorting, list becomes [-1, 0, 2, 3, 4, 4, 4, 5, 6, 7, 9, 9, 10, 10]
# So the smallest missing positive integer is 1
```

---

#### Data Structures

##### Input:

* A list of integers.

##### Output:

* An integer.

---

#### Algorithm

* Take the given list and find its length.
* Initiate a while loop to iterate over the integers from `1` to the `length` of the list.
* For each integer, check to see if it is included in the list.
* If it is not included, return that integer.

---

#### Code

```python
def min_miss_pos(integers):
    max_integer = len(integers) + 1
    current_integer = 1

    while current_integer <= max_integer:
        if current_integer not in integers:
            return current_integer
        
        current_integer += 1
```

