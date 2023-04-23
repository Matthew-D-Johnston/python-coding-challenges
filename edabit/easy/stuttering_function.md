##### Edabit > Python > Easy

---

## Stuttering Function

#### Problem

##### Instructions:

Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis `...` and space after each, and then the word is pronounced with a question mark `?`.

##### Definitions/Rules (explicit and implicit):

* repeat twice: first two letters of word followed by an ellipsis and then a space
* then the word followed by a question mark.

##### Input/Output:

* Input: a word
* Output: the first two letters of the word followed by an ellipsis and a space repeated twice and then the full word followed by a question mark.

##### Mental Model:

Take the word and grab the first two letters. Create a string with the first two letters followed by an ellipsis and a space. Output this string twice followed by the full word and a question mark.

---

#### Examples / Test Cases

```python
stutter("incredible")
// => "in... in... incredible?"
stutter("enthusiastic")
// => "en... en... enthusiastic?"
stutter("outstanding")
// => "ou... ou... outstanding?"
```

---

#### Data Structures

##### Input:

* A string

##### Output:

* A string

---

#### Algorithm

* Obtain first two letters of string.
* 



---

#### Code

```python
def stutter(word):
  return ((word[0:2] + '... ') * 2) + word + '?'
```

