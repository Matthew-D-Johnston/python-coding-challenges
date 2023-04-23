##### Edabit > Python > Medium

---

## Burglary Series (03): Is It Gone?

#### Problem

##### Instructions:

Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

Given a **dictionary** of the stolen items and a **string in lowercase** representing the name of the pet (e.g. "rambo"), return:

- `"Rambo is gone..."` if the name *is* on the list.
- `"Rambo is here!"` if the name is *not* on the list.

*Note that the first letter of the name in the return statement is capitalized.*

##### Definitions/Rules (explicit and implicit):

* Stolen items: an object containing the stolen items as keys.
* The name of the pet is a string in lowercase.
* But the string returned should contain the capitalized name of the pet.

##### Input/Output:

* Input 1: an object containing the stolen items as keys.
* Input 2: the name of the pet.
* Output: a string value that indicates whether or not the pet is gone or not.

##### Mental Model:

Extract the item names (i.e. keys) from the given list of stolen objects (i.e. the object). Check to see if the name of the pet is included in the list of keys. If it is, capitalize the pet name and return `"{Name} is gone..."`. If it is not, return `"{Name} is here!"`.

---

#### Examples / Test Cases

```python
items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
}
name = 'timmy'
find_it(items, name)
# => "Timmy is gone..."

items = {
  "tv": 30,
  "stereo": 50,
}
name = 'timmy'
find_it(items, name)
# => "Timmy is here!"

items = {}
name = 'timmy'
find_it(items, name)
# => "Timmy is here!"
```

---

#### Data Structures

##### Input:

* A dictionary with key-value pairs.
* A string.

##### Output:

* A string.

---

#### Algorithm

* Check to see if the name is included in a list of the dictionary's keys.
* If it is, return the capitalized name plus `' is gone ...'`.
* If not, return the capitalized name plus `' is here!'`.

---

#### Code

```python
def find_it(items, name):
  if name in items.keys():
    return name.capitalize() + ' is gone...'
  else:
    return name.capitalize() + ' is here!'
```

