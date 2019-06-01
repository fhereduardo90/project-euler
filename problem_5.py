import functools


def smallest_number(interval, number):
    if interval == 0:
        return True

    if not (number % interval):
        if smallest_number(interval - 1, number):
            return True
        else:
            return False
    else:
        return False


interval = 20
number = interval

while not smallest_number(interval, number):
    number += interval

print(number)
