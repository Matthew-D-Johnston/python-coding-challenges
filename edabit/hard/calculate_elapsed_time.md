##### Edabit > Python > Hard

---

## Calculate Elapsed Time

#### Problem

##### Instructions:

Create a function that takes a timestamp for the start time `sa` and stop time `st` in **HH:MM:SS** format and returns the measured amount of **elapsed time** between start and stop times.

_Notes_

- All times will be provided in 24 Hrs format.
- Consider Elapsed time will always be less than 24 Hrs.

##### Definitions/Rules (explicit and implicit):

* Return in format, `"HH:MM:SS"`.
* Uses 24-hour format.
* Elapsed time will always be less than 24 hrs.

##### Input/Output:

* Input: two timestamps as strings.
* Output: a string representing the difference in the two given timestamps.

##### Mental Model:

Take the two timestamps. Create `datetime` objects. Take the difference between the two time objects. Determine the hours, minutes, and seconds that represent the time difference between the two objects. Format the result like so, `"HH:MM:SS"`.

---

#### Examples / Test Cases

```python
elapsed_time("11:00:00", "12:00:00") ➞ "01:00:00"

elapsed_time("13:01:43", "21:41:57") ➞ "08:40:14"

elapsed_time("17:34:43", "17:34:42") ➞ "23:59:59"
```

---

#### Data Structures

##### Input:

* Two strings.

##### Output:

* A string.

---

#### Algorithm

* Import the `datetime` module using `from datetime import datetime`
* Create to `datetime` objects from the given strings using `strptime` and formatted as `"%H:%M:%S"`
* Get the time difference by subtracting the first time from the second. Store in variable called `time_delta`.
* Find the total seconds from the time difference using `total_seconds()`. Make sure to round so there are no decimal places.
* Find the `hours`: `total_seconds // 3600`
* Find the `minutes`: `(total_seconds % 3600) // 60`
* Find the `seconds`: `total_seconds % 60`
* If the `hours` are less than `0` (i.e. negative), then set `hours` equal to `24 + hours`
* Format the output so that there are leading zeros.

---

#### Code

```python
from datetime import datetime

def elapsed_time(time1, time2):
    t1 = datetime.strptime(time1, "%H:%M:%S")
    t2 = datetime.strptime(time2, "%H:%M:%S")

    time_delta = t2 - t1

    total_seconds = round(time_delta.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    if hours < 0:
        hours += 24
    
    return ("%02d" % hours) + ":" + ("%02d" % minutes) + ":" + ("%02d" % seconds)
```

