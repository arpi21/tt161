def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def sequence(n):
    if n <= 0:
        return ('invalid input')
    else:
        for i in range(n):
            print(fibo(i))



sequence(20)

