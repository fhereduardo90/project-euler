def sum_even_numbers():
    prev = 1
    nxt = 2
    sum = 0

    while nxt <= 4000000:
        sum += nxt

        nxt = (((prev * 2) + (nxt * 3)))
        prev = (nxt - (((nxt - (prev * 2)) // 3) + prev))
    else:
        return sum


print(sum_even_numbers())
