##### Edabit > Python > Hard

---

## Find Domain Name From DNS Pointer (PTR) Records Using IP Address

#### Problem

##### Instructions:

Write a function that takes an IP address and returns the domain name using PTR DNS records.

_Notes_

- You may want to import `socket`.
- Don't cheat and just print the domain name, you need to make a real DNS request.
- Return as a string.

##### Definitions/Rules (explicit and implicit):

* Make a real DNS request.
* Retrieve the domain name given an IP address.

##### Input/Output:

* Input: an IP address.
* Output: domain name.

##### Mental Model:

Take the given IP address and return the domain name associated with that IP address.

---

#### Examples / Test Cases

```python
get_domain("8.8.8.8")
# => "dns.google"

get_domain("8.8.4.4")
# => "dns.google"
```

---

#### Data Structures

##### Input:

* A string.

##### Output:

* A string.

---

#### Algorithm

* import `socket`
* Use the `socket.gethostbyaddr(ip_address)` function to obtain an array whose first element is the domain name.

---

#### Code

```python
import socket

def get_domain(ip_address):
    return socket.gethostbyaddr(ip_address)[0]
```

