##### Edabit > Python > Medium

---

## Geometry 1: Length of Line Segment

#### Problem

##### Instructions:

Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.

**Notes**

- The order of the given numbers is X, Y.
- This challenge is easier than it looks.
- Round your result to two decimal places.

##### Definitions/Rules (explicit and implicit):

* Return length of line segment.
* Line segment is defined by two points in the x-y coordinate plane.
* Round the result to two decimal points.

##### Input/Output:

* Input: two points defined by x and y coordinates.
* Output: the length of the line defined by the two points.

##### Mental Model:

Take the two points and use the Pythagorean theorem to calculate the length of the line defined by the two points.

---

#### Examples / Test Cases

```python
line_length([15, 7], [22, 11])
# => 8.06
line_length([0, 0], [0, 0])
# => 0
line_length([0, 0], [1, 1])
# => 1.41
```

---

#### Data Structures

##### Input:

* Two arrays containing two numbers each.

##### Output:

* A number rounded to two decimal places.

---

#### Algorithm

* Extract the x and y coordinates of each point.
* Find the absolute value of the difference between the x and y coordinates, respectively.
* Square the absolute values.
* Add the squared values.
* Take the square root and return the result rounded to two decimal places.

---

#### Code

```python
import math

def line_length(dot1, dot2):
  x1, y1 = dot1[0], dot1[1]
  x2, y2 = dot2[0], dot2[1]

  return round(math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)), 2)
```

