import math

def babbage(n):
    digits = len(str(n))
    multiplier = int('1' + (digits * '0'))
    square = n
    square_root = math.sqrt(square)

    while square_root / 1 != square_root // 1:
        square += multiplier
        square_root = math.sqrt(square)
    
    if n == 269696:
        if square_root == 99736:
            return "Babbage was correct!"
        else:
            return "Babbage was incorrect!"
    else:
        return square_root


print(babbage(25))
print(babbage(161))
print(babbage(269696))
