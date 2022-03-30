def get_list_number_divisors(number):
    number_divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            number_divisors.append(divisor)
    return number_divisors


if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 16))
