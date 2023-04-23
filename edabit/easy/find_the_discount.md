##### Edabit > Python > Easy

---

## Find the Discount

#### Problem

##### Instructions:

Create a function that takes two arguments: the original `price` and the `discount` percentage as integers and returns the final price after the discount.

##### Definitions/Rules (explicit and implicit):

* two arguments: `price` and `discount`
* `price` is as is
* `discount` is a percentage and must be converted to decimal in order to calculate the price after discount.
* The `discount` must be multiplied by the `price` for the discount deduction.
* Answer should be rounded to two decimal places.

##### Input/Output:

* Inputs: the `price` and the `discount` as a percentage.
* Output: the final price after the discount has been deducted.

##### Mental Model:

Convert the `discount` to a decimal. Then find the discount deduction and subtract from the initial price.

---

#### Examples / Test Cases

```python
dis(1500, 50)
# => 750

dis(89, 20)
# => 71.2

dis(100, 75)
# 25
```

---

#### Data Structures

##### Inputs:

* `price`: a number
* `discount`: a number

##### Outputs:

* final price: a number rounded to two decimal places

---

#### Algorithm

* Take the `discount` and convert it to a percentage by dividing by 100.
* Multiply that conversion by the price and subtract from the initial price.
* Return that result.

---

#### Code

```python
def dis(price, discount):
  return round(price - (price * (discount / 100)), 2)
```

