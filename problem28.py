def spiral_diag_sum(n):
    if not  (n%2):
        return None
    sum = 1
    end = 1
    rings = (n-1) // 2
    for i in range(1,rings + 1):
        # in the next ring, the corners are e+2r, e+4r, e+6r, e+8r
        # where e is the number at the end of the previous ring
        # and r is the ring number (starting from 0 at the ring of only 1)
        sum = sum + (4*end) + 2*i*10
        # each ring other than the first has 8r numbers in it
        end = end + (i * 8)
    return sum

if __name__ == "__main__":
    print(spiral_diag_sum(1001))