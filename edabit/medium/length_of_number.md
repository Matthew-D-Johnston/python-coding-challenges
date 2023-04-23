##### Edabit > Python > Medium

---

## Length of Number

#### Problem

##### Instructions:

Create a function that takes a number `num` and returns its length.  

**Notes:**

**The use of the len() function is prohibited.**

##### Definitions/Rules (explicit and implicit):

* Length of a number: the number of digits in the number
* Use of the `len()` function is prohibited.

##### Input/Output:

* Input: a number.
* Output: the length of the number.

##### Mental Model:

Take a given number and count the total number of digits that comprise the number.

---

#### Examples / Test Cases

```python
number_length(10)
# => 2
number_length(5000)
# => 4
number_length(0)
# => 1
```

---

#### Data Structures

##### Input:

* A number.

##### Output:

* A number.

---

#### Algorithm

* Convert the given number into a string.
* Declare a `count` variable and set its value to `0`.
* Initiate a `for` loop that will iterate over each character of the string.
* On each iteration increment the `count` variable by `1`.
* Return the `count` variable after the loop is finished.

---

#### Code

```python
def number_length(num):
  string_num = str(num)

  count = 0

  for char in string_num:
    count += 1

  return count
```

