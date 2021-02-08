if __name__ == "__main__":
    f = open('p013_numbers.txt', 'r')
    numbers = [int(s) for s in f.read().split('\n')]
    
    # sum of 100 50 digit numbers is ~10^52
    # we care about 10 significant figures so reduce magnitude by 52-10 = 42
    sum = 0
    for n in numbers:
        sum = sum + (n/(10**42))
    
    print(sum)