if __name__ == "__main__":
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))

    cond_1 = A % 2 == 1
    cond_2 = B % 2 == 1

    if cond_1 and cond_2:
        print("Числа A и B нечетные")

    else:
        print("Одно из чисел четное!")
