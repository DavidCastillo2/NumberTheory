def gcd(a, b):

    val = a  # 78
    f = b  # 66
    retVal = 1

    while True:
        if f == 0:
            return retVal
        else:
            retVal = f
            r = val // f
            remainder = val - (f*r)
            print("%d / %d = %d remainder %d" % (val, f, r, remainder))
            val = f
            f = remainder


if __name__ == "__main__":
    # 50 = 32 MOD 18
    A = 50388
    B = 2

    print("Output: %d" % gcd(A, B), end="\n\n")






