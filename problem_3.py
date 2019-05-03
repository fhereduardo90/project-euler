def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def largest_prime_factor(number):
    prime_factors = []
    result = 1

    for i in range(number):
        if is_prime(i) and number % i == 0:
            prime_factors.append(i)
            result = result * i

            if result == number:
                break

    print(prime_factors)


largest_prime_factor(600851475143)
