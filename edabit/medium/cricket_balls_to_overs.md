##### Edabit > Python > Medium

---

## Cricket Balls to Overs!

#### Problem

##### Instructions:

In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of `balls` bowled by a bowler and calculates the number of **overs** and **balls** bowled by him/her. Return the value as a float, in the format `overs.balls`.

_Notes_

The number following the decimal point represents the balls remaining after the last over. Therefore, it will only ever have a value of 1-5.

##### Definitions/Rules (explicit and implicit):

* Over: 6 deliveries a bowler bowls from one end.
* The total number of balls is given; the result is in the format `overs.balls` where `overs` is the complete overs possible given the number of balls and `balls` represents the remaining balls leftover after all overs have been accounted for.



##### Input/Output:

* Input: the total number of balls.
* Output: The number of overs and remaining number of balls, formatted as `overs.balls`.

##### Mental Model:

Take the total given number of balls and divide by 6. Find the number of times 6 can be divided into the total before remainder. Find the remaining number of balls. Return the total overs and remaining number of balls in the format `overs.balls`.

---

#### Examples / Test Cases

```python
total_overs(2400)
# => 400

total_overs(164)
# => 27.2

total_overs(945)
# => 157.3

total_overs(5)
# => 0.5
```

---

#### Data Structures

##### Input:

* A number.

##### Output:

* A float.

---

#### Algorithm

* Declare an `overs` variable and set it equal to the floored division of the total balls divided by 6.
* Declare a `remaining_balls` variable and set it equal to the remainder of the total balls divided by 6.
* Return `overs + (remaining_balls / 10)`.

---

#### Code

```python
def total_overs(balls):
    overs = balls // 6
    remaining_balls = balls % 6

    return overs + (remaining_balls / 10)
```

