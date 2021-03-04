def generate_prime_numbers(start, end):
    for number in range(start, end + 1):
        if number > 1:

            for i in range(2, number):
                if number % i == 0:
                    break

                if i + 1 == number:
                    yield number
