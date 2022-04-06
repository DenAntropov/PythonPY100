def is_palindrome_number(num: int) -> bool:
    if num < 0:
        raise NameError("Число отрицательное!")     # TODO проверить что число больше или равно нулю

    if str(num) == str(num)[::-1]:
        return True
    else:
        return False    # TODO проверить является ли число палиндром


if __name__ == "__main__":
    print(is_palindrome_number(1234))
    print(is_palindrome_number(1234321))
