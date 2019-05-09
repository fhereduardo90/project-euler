# def is_palindrome(number):
#     reversed_number = 0
#     n = number

#     while(n != 0):
#         difference = n % 10
#         reversed_number = (reversed_number * 10) + difference
#         n //= 10

#     return number == reversed_number


def is_palindrome(number):
    reversed_number = str(number)[::-1]
    return number == int(reversed_number)


def largest_palindrome_product():
    palindrome = 0
    serie_a = 999
    serie_b = 999
    result = 0

    while(True):
        result = serie_a * serie_b

        if result == 0:
            break

        if is_palindrome(result):
            palindrome = result
            break
        else:
            if serie_a - serie_b == 100:
                serie_a -= 1
                serie_b = serie_a
            else:
                serie_b -= 1

    print(serie_a, serie_b, palindrome)


largest_palindrome_product()
