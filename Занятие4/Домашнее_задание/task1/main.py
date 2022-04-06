def task(num: int) -> bool:
    list_ = [int(i) for i in str(num)]
    if len(set(list_)) == 1:
        return True
    else:
        return False
    # TODO какая есть особенность, когда все цифры в числе одинаковые?


if __name__ == "__main__":
    print(task(123))
    print(task(1111111))
