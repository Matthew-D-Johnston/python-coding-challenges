##### Edabit > Python > Hard

---

## Combined Vector Sequence

#### Problem

##### Instructions:

The goal is to test if a **consecutive sequence** is formed. A consecutive sequence is defined as sequence of incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8). The twist is that you have to consider the combination of vectors as shown.

```
[3 5 1 -5 ]  =>  [3+4  5+3  1+8  15-5]  =  [7 8 9 10]  =>  true
[4 3 8 15]
```

Also important is that the vectors can be of different sizes, where excess numbers in the longer one will be paired with 0s from the other one.

```
[2 2 2  ]  =>  [2+5  2+6  2+7  10+0]  = [ 7 8 9 10]  =>  true
[5 6 7 10]
```

_Notes_

- Each array has at least two elements.
- Try the [harder version](https://edabit.com/challenge/xo6qTjB8GMDcvzu59).

##### Definitions/Rules (explicit and implicit):

* Consecutive sequence: a sequence of numbers whereby each successive number is one higher than the previous.
* The sequence is a combination of two vectors.
* The vectors may be of different lengths.
* But each vector array has at least two elements.

##### Input/Output:

* Inputs: two vectors of numbers.
* Output: `true` if a consecutive sequence is formed from the two vectors; `false` otherwise.

##### Mental Model:

Take the two vectors. See if one is larger than the other. Add any zeros to the smaller vector to make it the same length as the longer vector. Once they are the same size, add the corresponding elements of the two vectors so that they are combined in a single array. Check to see if the array contains a consecutive sequence of numbers. Iterate over the array and return `false` if the next number is different than one plus the current number. If `false` is not returned after the iteration is complete, then return `true`.

---

#### Examples / Test Cases

```python
has_consecutive_series([3, 5, 1, -5], [4, 3, 8, 15])
# => true
has_consecutive_series([2, 2, 2], [5, 6, 7, 10])
# => true
has_consecutive_series([4, 2, 8, 5], [14, 2, 4, 9])
# => false
```

---

#### Data Structures

##### Input:

* Two lists of numbers.

##### Output:

* A boolean.

##### Intermediate Data Structures:

* Will mostly be working with lists and numbers.

---

#### Algorithm

* Take the difference between the length of the two vectors and store in a variable called `length_difference`.
* If the difference is positive (i.e. greater than 0), that means the first vector is larger than the second vector and we need to add zeros equal to the difference to the second array.
* If the difference is negative (i.e. less than 0), then the second vector is larger than the first and we need to add zeros equal to the absolute value of the difference to the second array.
* Then we need to declare a `sequence` variable and set it equal to an empty list.
* Then initiate a `for` loop that loops over a range starting from `0` and through to the length of either vector.
* Inside the loop, use the current loop iteration variable as the index for the two lists and add the corresponding number at those indexes and push the result to the `sequence` list.
* Once the loop is finished, use a `for` loop to iterate over a range from `0` to the length minus one of the `sequence` list.
* On each iteration, check to see if the current number of the list is equal to one greater than that current number. If not, return `false`
* If the loop completes without ever returning `false` then return `true`.

---

#### Code

```python
def has_consecutive_series(v1, v2):
    length_difference = len(v1) - len(v2)

    if length_difference > 0:
        v2 += length_difference * [0]

    if length_difference < 0:
        v1 += (-1 * length_difference) * [0]

    sequence = []
    for index in range(len(v1)):
        sequence.append(v1[index] + v2[index])
    
    for index in range(len(sequence) - 1):
        if sequence[index] != (sequence[index + 1] - 1):
            return False
    
    return True
```

