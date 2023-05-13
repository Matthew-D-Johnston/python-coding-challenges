##### Edabit > Python > Medium

---

## Sum of v0w3ls

#### Problem

##### Instructions:

Create a function that takes a string and returns the **sum of vowels**, where some vowels are considered numbers.

| Vowel | Number |
| :---- | ------ |
| A     | 4      |
| E     | 3      |
| I     | 1      |
| O     | 0      |
| U     | 0      |

##### Definitions/Rules (implicit and explicit):

* "sum of vowels": all the vowels (e.g. a, e, i, o, and u) are associated with corresponding number values; to sum the vowels we need to sum the corresponding number values.
* All of the vowels will be contained in the given input string.
* Vowels are case insensitive (e.g. A = 4 and a = 4).

##### Input/Output:

* Input: a string of text.
* Output: the sum of the vowels that occurred in the input string.

##### Mental Model:

Iterate through each character of the string. Check to see if that character is a vowel and if so, then find its corresponding number value. Sum up the corresponding values for each of the vowels and return the total sum after iterating through the entire string.

---

#### Examples / Test Cases

```
sum_of_vowels("Let\'s test this function.") ➞ 8

sum_of_vowels("Do I get the correct output?") ➞ 10

sum_of_vowels("I love edabit!") ➞ 12
```

---

#### Data Structures

##### Input:

* A string

##### Output:

* An integer

---

#### Algorithm

* Create a dictionary with vowels as keys and the corresponding number values as values.
* Create a list of vowels containing each of the values.
* Initialize a `sum` variable and set its inital value to `0`.
* Iterate over each character in the given string.
* convert the character to a lowercase character.
* Check to see if the char is present in a list of vowels; if it is, take that char to obtain the corresponding value from the values dictionary.
* Add the corresponding value to the `sum` variable.
* After iterating over each character, return the `sum` variable.



---

#### Code

```python
def sum_of_vowels(text):
  values = { 'a': 4, 'e': 3, 'i': 1, 'o': 0, 'u': 0 }
  vowels = ['a', 'e', 'i', 'o', 'u']
  sum = 0

  for char in text:
    lowercase_char = char.lower()

    if lowercase_char in vowels:
      sum += values[lowercase_char]
  
  return sum
```



