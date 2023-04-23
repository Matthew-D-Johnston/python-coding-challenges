##### Edabit > Python > Hard

---

## Basic Arithmetic Operations on a String Number

#### Problem

##### Instructions:

Create a function to perform basic arithmetic operations that includes **addition**, **subtraction**, **multiplication** and **division** on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have `1` followed by a space, operator followed by another space and `2`. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

`eval()` is not allowed. In case of division, whenever the second number equals "0" return `-1`.

For example:

```
"15 // 0"  ➞ -1
```

_Notes_

- All the inputs are only integers.
- The operators are `*` `-` `+` and `//`.
- Hint: Think about the single space that appears before and after the arithmetic operator.

##### Definitions/Rules (explicit and implicit):

* Two numbers and one valid operator are given in the instructions.
* `eval()` is not allowed.
* For division, if the second operator equals `0`, return `-1`.
* All number inputs will be integers.

##### Input/Output:

* Input: instructions that include two numbers and one valid operator.
* Output: a number.

##### Mental Model:

Take the given instructions and split them into the two separate numbers and the operator. Then determine which operation needs to be performed given the specific operator. Perform the operation and return the result.

---

#### Examples / Test Cases

```python
arithmetic_operation("12 + 12")
# => 24 // 12 + 12 = 24

arithmetic_operation("12 - 12")
# => 24 // 12 - 12 = 0

arithmetic_operation("12 * 12")
# => 144 // 12 * 12 = 144

arithmetic_operation("12 // 0")
# => -1 // 12 / 0 = -1
```

---

#### Data Structures

##### Input:

* A string.

##### Output:

* A number.

---

#### Algorithm

* Split the instructions into a list with each number and the operator.
* Assign each of the list elements to a variable name.
* Make sure to convert the string numbers to actual integers.
* Use a `match/case` statement to determine which operation to perform be evaluting the operator variable.
* Perform the operation.
* For division, if the second number is a `0`, return `-1`.

---

#### Code

Solution 1

```python
def arithmetic_operation(instructions):
    instruction_list = instructions.split(' ')
    first_num = int(instruction_list[0])
    second_num = int(instruction_list[2])
    operator = instruction_list[1]

    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num
        case '//':
            if second_num == 0:
                return -1
            else:
                return first_num // second_num
```

This code worked with my test cases, but Edabit spit out this error:

```
ERROR:   File "<string>", line 14
    match operator:
                 ^
SyntaxError: invalid syntax
```

Solution 2

```python
def arithmetic_operation(instructions):
    instruction_list = instructions.split(' ')
    first_num = int(instruction_list[0])
    second_num = int(instruction_list[2])
    operator = instruction_list[1]
    
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num
    elif operator == '//':
        if second_num == 0:
            return -1
        else:
            return first_num // second_num
```

This solution worked in Edabit, however.