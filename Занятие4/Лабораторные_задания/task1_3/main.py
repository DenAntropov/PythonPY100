def count_even_numbers(list_numbers: list) -> int:
    return len([k for k in list_numbers if k % 2 == 0])  # TODO найти количество четных чисел в списке list_numbers


if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
