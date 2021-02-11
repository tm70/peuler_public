# The number of permutations starting with a specific digit is 9! = 362880
# 2*9! < 1000000 < 3*9!, so the 1 millionth permutation starts with a 2
# 100000 - 2*9! = 274240, so it is the 274240th permutation starting with 2

from itertools import permutations

if __name__ == "__main__":
    digits = [0, 1, 3, 4, 5, 6, 7, 8, 9]
    print(list(permutations(digits))[274239])
