def task(num) -> bool:  # TODO добавить аннотацию типов
    list_ = [int(i) for i in str(abs(num))]
    if 10 <= sum(list_) <= 99:
        return True
    else:
        return False


if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
