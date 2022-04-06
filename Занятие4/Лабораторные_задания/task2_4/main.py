def digit_sum(num: int) -> bool:
    if len(str(num)) != 4:
        raise NameError("Число не четырехзначное!")
    list_ = [int(i) for i in str(num)]

    if sum(list_) % 7 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(digit_sum(1234))
    print(digit_sum(7777))
