##### Edabit > Python > Medium

---

## Sum of Odd and Even Numbers

#### Problem

##### Instructions:

Write a function that takes a list of numbers and returns a list with two elements:

1. The first element should be the sum of all **even** numbers in the list.
2. The second element should be the sum of all **odd** numbers in the list.

_Notes_

Count `0` as an **even** number.

##### Definitions/Rules (explicit and implicit):

* Return an array whose first element is the sum of all even numbers given and the second element is a sum of all the odd numbers given.
* Treat 0 as an even number.

##### Input/Output:

* Input: a list of numbers
* Output: a list of two numbers, the sum of odd numbers and the sum of even numbers.

##### Mental Model:

Take the given list of numbers. Iterate over the list and check to see whether each number is even or odd. If even then add it to a sum of even numbers. If odd, then add it to a sum of odd numbers.

---

#### Examples / Test Cases

```python
sum_odd_and_even([1, 2, 3, 4, 5, 6])
# => [12, 9]

sum_odd_and_even([-1, -2, -3, -4, -5, -6])
# => [-12, -9]

sum_odd_and_even([0, 0])
# => [0, 0]
```

---

#### Data Structures

##### Input:

* A list of numbers

##### Output:

* A list of two numbers

---

#### Algorithm

* Declare an `even_sum` variable and set its initial value to `0`.
* Declare an `odd_sum` variable and set its initial value to `0`.
* Iterate over the given list of numbers.
* If the number is even then add it to the `even_sum` variable.
* Else if it is odd, then add it to the `odd_sum` variable.
* return a list whose first element is the `even_sum` variable and whose second element is the `odd_sum` variable.

---

#### Code:

```python
def sum_odd_and_even(numbers):
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return [even_sum, odd_sum]
```

