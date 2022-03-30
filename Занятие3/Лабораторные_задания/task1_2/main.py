def factorial(n):
    fact = 1
    if n > 0:
        for i in range(1, n + 1):
            fact *= i
        return fact
    else:
        print("Error")



if __name__ == "__main__":
    print(factorial(4))
