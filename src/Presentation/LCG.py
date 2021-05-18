from Presentation.graphIt import generateDict, plot_bar


class LCG:
    def __init__(self, a, Xn, C, M):
        self.modulus = M
        self.start = Xn
        self.a = a
        self.seed = Xn
        self.c = C
        self.generator = self.lcg()

    def setSeed(self, val):
        self.seed = val

    def reset(self):
        self.seed = self.start

    def lcg(self):
        """Linear congruential generator."""
        while True:
            self.seed = (self.a * self.seed + self.c) % self.modulus
            yield self.seed

    def show(self, s, showPrint=True):
        retVal = []
        if showPrint :
            print("A=%d    Xn=%d    C=%d    M=%d" % (self.a, self.seed, self.c, self.modulus))
        for i in range(s):
            s = "(%d * %d + %d) mod %d\n" % (self.a, self.seed, self.c, self.modulus)
            val = next(self.generator)
            if showPrint:
                print("%d = " % val, end=s)
            retVal.append(val)
        if showPrint:
            print("Final values = ", end='')
            print(retVal, end="\n\n")
        return retVal

    def modIt(self, nums, mod, printIt=True):
        vals = self.show(nums, False)
        for i in range(len(vals)):
            vals[i] = vals[i] % mod
        if printIt:
            print(vals)
        return vals


if __name__ == "__main__":
    # a, Xn, C, M
    # 1, 0, 0, 1

    # NextNum = (a * Xn + C) % M

    lcg = LCG(2, 1, 4, 20)
    vals = lcg.show(5)

    lcg = LCG(a=22695477, Xn=1, C=1, M=pow(2, 32))
    vals = lcg.show(5)


