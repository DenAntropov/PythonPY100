def input_numbers():
    list_numbers = []

    input_num = int(input("Введите новое число: "))
    while input_num >= 0:
        if 3 <= input_num <= 13:
            list_numbers.append(input_num)
        input_num = int(input("Введите новое число: "))

    return list_numbers

if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)

