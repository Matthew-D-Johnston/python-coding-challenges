##### Edabit > Python > Medium

---

## FizzBuzz Interview Question

#### Problem

##### Instructions:

Create a function that takes a number as an argument and returns `"Fizz"`, `"Buzz"` or `"FizzBuzz"`.

- If the number is a multiple of 3 the output should be `"Fizz"`.
- If the number given is a multiple of 5, the output should be `"Buzz"`.
- If the number given is a multiple of both 3 and 5, the output should be `"FizzBuzz"`.
- If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
- The output should always be a string even if it is not a multiple of 3 or 5.

**Notes**

- Try to be precise with how you spell things and where you put the capital letters.
- If you get stuck on a challenge, find help in the **Resources** tab.
- If you're really stuck, unlock solutions in the **Solutions** tab.

##### Definitions/Rules (explicit and implicit):

* Number is a multiple of 3: `"Fizz"`
* Number is a multiple of 5: `"Buzz"`
* Number is a multiple of 3 and 5: `"FizzBuzz"`
* Number is not a multiple of either 3 or 5: output number on its own as a string.

##### Input/Output:

* Input: a number
* Output: A string that depends on whether the number is a multiple of 3, 5, both, or neither.

##### Mental Model:

Take the given number. Check to see if it is a multiple of 3 and 5. If so, output `"FizzBuzz"`. If not, check if it is just a multiple of 3. If so, return `"Fizz"`. If not, check to see if it is a multiple of just 5. If so, return `"Buzz"`. If not, then output the number as a string.

---

#### Examples / Test Cases

```python
fizz_buzz(3)
# => "Fizz"
fizz_buzz(5)
# => "Buzz"
fizz_buzz(15)
# => "FizzBuzz"
fizz_buzz(4)
# => "4"
```

---

#### Data Structures

##### Input:

* an integer.

##### Output:

* a string.

---

#### Algorithm

* Take the number and check to see if it is a multiple of both 3 and 5:
  * if yes, output `"FizzBuzz"`
* Else if it is just a multiple of 3:
  * output `"Fizz"`
* Else if it is just a multiple of 5:
  * output `"Buzz"`
* Else
  * output the number as a string.

---

#### Code

```python
def fizz_buzz(num):
  if (num % 3 == 0 and num % 5 == 0):
    return "FizzBuzz"
  elif (num % 3 == 0):
    return "Fizz"
  elif (num % 5 == 0):
    return "Buzz"
  else:
    return str(num)
```

