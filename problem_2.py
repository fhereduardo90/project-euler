def sum_even_numbers():
    prev = 0
    nxt = 1
    sum = 0

    while nxt <= 4000000:
        if nxt % 2 == 0:
            sum += nxt

        nxt = prev + nxt
        prev = nxt - prev
    else:
        return sum


print(sum_even_numbers())
