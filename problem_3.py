def is_prime(number):
    if number < 2:
        return False
    elif number == 2 or number == 3 or number == 5 or number == 7:
        return True
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        return False
    else:
        return True


def largest_prime_factor(number):
    primes = []
    division = number
    multiplier = 1
    current_prime = 2
    go = True

    while(go):
        if is_prime(current_prime) and division % current_prime == 0:
            division = division // current_prime
            primes.append(current_prime)
            multiplier = multiplier * current_prime
        else:
            current_prime += 1

        if multiplier >= number:
            go = False
        elif current_prime == division:
            primes.append(division)
            go = False
    else:
        print(primes)


largest_prime_factor(600851475143)
