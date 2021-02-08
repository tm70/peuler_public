def alpha_value(str):
    sum = 0
    for i in range(len(str)):
        sum = sum + ord(str[i]) - 64
    return sum

if __name__ == "__main__":
    f = open("p022_names.txt", 'r')
    names = [s[1:-1] for s in f.read().split(',')]
    names = sorted(names)
    
    sum = 0
    for i, name in enumerate(names):
        sum = sum + ((i + 1) * alpha_value(name))
    print(sum)