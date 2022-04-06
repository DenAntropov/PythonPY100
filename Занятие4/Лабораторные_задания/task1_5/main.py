if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    chet = [i % 2 == 0 for i in list_]
    nechet = [i % 2 == 0 for i in list_]         # TODO получить два списка четных и нечетных чисел

    num_chet = len(chet)
    num_nechet = len(nechet)    # TODO найти длины этих списков

    if num_chet > num_nechet:
        print("Чётных больше!")

    elif num_chet < num_nechet:
        print("Нечётных больше!")

    else:
        print("Поровну!")   # TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
