# sum of all multiples of i, up to and including j
def sum_of_multiples(i, j):
    n = j // i
    return n/2 * (2*i + (n-1)*i)

if __name__ == "__main__":
    x = sum_of_multiples(3,999) + sum_of_multiples(5,999) - sum_of_multiples(15,999)
    print(x)
    
    #check
    y = 0
    for i in range(1000):
        if (i%3 == 0 or i%5 == 0):
            y = y + i
    print(y)