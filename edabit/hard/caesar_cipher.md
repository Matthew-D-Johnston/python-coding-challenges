##### Edabit > Python > Hard

---

## Caesar Cipher

#### Problem

##### Instructions:

Create a function that takes two arguments (`text`, `key`) and returns a new encrypted text using the `key`. For example, if the input is `"a"` and the key is `1`, it should move that letter 1 step in alphabetic order so the output would be `"b"`.

_Notes_

The input is only letters and spaces; no special characters.

##### Definitions/Rules (explicit and implicit):

* Input is only letters and spaces.
* If the key steps past the end of the alphabet, it should wrap around to the beginning of the alphabet and cycle through it again.

##### Input/Output:

* Inputs: a text message and a key value representing the number of spaces to step.
* Output: an encoded message.

##### Mental Model:

Take the given text and key. Find the remainder of the key when dividing by 26. Use that as the key. Iterate over each character of the text. For each character, find the character code. If the character code is between 65 and 90, create a logic branch for uppercase letters. if it is between 97 and 122, create another logic branch for lowercase letters. If it is 32, then simply leave as 32. Add the key to the character code. If the sum extends past the upper limit of each branch (i.e. 90 or 122), subtract 26 from the key-character code summation. Use that character code to derive the encoded character. Append the character code to an `encoded_text` string.

---

#### Examples / Test Cases

```python
caesar_cipher("hello", 5) ➞ "mjqqt"

caesar_cipher("hello world", 1) ➞ "ifmmp xpsme"

caesar_cipher("a", 2) ➞ "c"
```

---

#### Data Structures

##### Input:

* A string.
* An integer.

##### Output:

* A string.

---

#### Algorithm

* Reassign the `key` to `key % 26`.
* Declare an `encoded_text` variable. 
* Iterate over each character of the `text` string.
* Declare a `char_code` variable and set it equal to the character code of the current character.
* Declare an `encoded_char_code` and set it equal to the `char_code + key`
* If the character code is between 65 and 90:
  * If `encoded_char_code` is greater than 90, reassign it to `encoded_char_code - 26`
  * Use `encoded_char_code` to find a character and append that character to the `encoded_text` string.
* Else if the character code is between 97 and 122:
  * If `encoded_char_code` is greater than 122, reassign it to `encoded_char_code - 26`
  * Use `encoded_char_code` to find a character and append that character to the `encoded_text`.
* Else:
  * append a space to `encoded_text` string.
* retrun `encoded_text`

---

#### Code

```python
def caesar_cipher(text, key):
    key %= 26
    encoded_text = ''

    for char in text:
        char_code = ord(char)
        encoded_char_code = char_code + key

        if char_code >= 65 and char_code <= 90:
            if encoded_char_code > 90:
                encoded_char_code -= 26
            
            encoded_text += chr(encoded_char_code)
        elif char_code >= 97 and char_code <= 122:
            if encoded_char_code > 122:
                encoded_char_code -= 26
            
            encoded_text += chr(encoded_char_code)
        else:
            encoded_text += ' '
        
    return encoded_text
```

