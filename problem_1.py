import math


def sum_multiples(number):
    t_3 = 3 * (math.floor(number/3) * (math.floor(number/3)+1))/2
    t_5 = 5 * (math.floor(number/5) * (math.floor(number/5)+1))/2
    t_15 = 15 * (math.floor(number/15) * (math.floor(number/15)+1))/2

    return (t_3 + t_5) - t_15


print(sum_multiples(1000))
