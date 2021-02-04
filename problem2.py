def even_fib(i):
    if (i == 0):
        return 2
    if (i == 1):
        return 8
    return 4*even_fib(i-1) + even_fib(i-2)

# should memoise for an easy increase in time efficiency
if __name__ == '__main__':
    x = 0
    i = 0
    while True:
        f = even_fib(i)
        if (f < 4000000):
            x = x + f
            i = i + 1
        else:
            break
    
    print(x)