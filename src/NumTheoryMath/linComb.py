class linComb:
    def __init__(self, a, b, printStuff=False, steps=None):
        if steps is None:
            g = GCD(a, b)
            steps = g.steps
            if printStuff:
                print("GCD(%d, %d):" %(a, b))
                print(g, end="\n\n")
                # print(" GCD = %d\n" %g.output)
        self.steps = steps
        self.a = a
        self.b = b
        self.s = steps
        self.solved = {}  # Dict with tuples as values
        self.finalSolution = None  # Tuple of just the final multiples of A and B
        self.aMult = 1
        self.bMult = -1
        self.printStuff = printStuff
        self.loop()
        return

    def loop(self):
        for i in range(0, len(self.s)):
            step = self.s[i]
            step.toInt()
            aMult = 1
            bMult = step.mult * -1
            a = 0
            b = 0
            aTemp = -1
            bTemp = -1
            expanded = False

            if step.remain == 0:
                break

            # We begin
            if self.printStuff:
                print("Step %d of %d" % (i+1, len(self.s)-1))
                print("%d = (%d)*%d + (%d)*%d" % (step.remain, aMult, step.a, bMult, step.b))

            # Dealing with step.A
            try:
                aTemp, bTemp = self.solved[str(step.a)]
                if self.printStuff:
                    print("%d = (%d)*%d + (%d)*%d + (%d)*%d" % (step.remain, aTemp, self.a, bTemp, self.b, bMult, step.b))
                a = aTemp * aMult
                b = bTemp * aMult
                expanded = True
            except KeyError:
                if step.a == self.a:
                    a = aMult
                else:
                    b = aMult

            # Dealing with step.B
            try:
                aCopy = aTemp
                bCopy = bTemp
                aTemp, bTemp = self.solved[str(step.b)]

                # Just for printing Expanded form - with bMult on the outside
                if self.printStuff:
                    if expanded:
                        print("%d = (%d)*%d + (%d)*%d + " % (step.remain, aCopy, self.a, bCopy, self.b), end='')
                    else:
                        print("%d = (%d)*%d + " % (step.remain, aMult, step.a), end='')
                    print("(%d)[ (%d)*%d + (%d)*%d ]" % (bMult, aTemp, self.a, bTemp, self.b))

                    # Just for Printing Expanded form - bMult FACTORED into other multiples
                    if expanded:
                        print("%d = (%d)*%d + (%d)*%d + " % (step.remain, aCopy, self.a, bCopy, self.b), end='')
                    else:
                        print("%d = (%d)*%d + " % (step.remain, aMult, step.a), end='')

                aTemp = aTemp * bMult
                bTemp = bTemp * bMult
                if self.printStuff:
                    print("(%d)*%d + (%d)*%d" % (aTemp, self.a, bTemp, self.b))

                a += aTemp
                b += bTemp
            except KeyError:
                if step.b == self.b:
                    b = bMult
                else:
                    a = bMult

            self.solved[str(step.remain)] = a, b
            self.finalSolution = (a, b)

            if self.printStuff:
                print("%d = (%d)*%d + (%d)*%d\n" % (step.remain, a, self.a, b, self.b))  # Final result


class linCombStep:
    def __init__(self, step):
        self.step = step
        self.aMult = 1
        self.bMult = step.mult


class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.steps = []
        self.output = self.gcd()
        return

    def gcd(self):

        val = self.a  # 78
        f = self.b  # 66
        retVal = 1

        while True:
            if f == 0:
                return retVal
            else:
                retVal = f
                r = val // f
                remainder = val - (f * r)
                stepString = "%d %d %d %d" % (val, f, r, remainder)
                s = Step(stepString)
                self.steps.append(s)
                val = f
                f = remainder

    def __repr__(self):
        retVal = ''
        for s in self.steps:
            retVal += str(s) + "\n"
        retVal += "GCD(%d, %d) = %d" % (self.a, self.b, self.output)
        return retVal


class Step:
    def __init__(self, string):
        numbers = string.split(' ')
        self.remain = numbers[3]
        self.a = numbers[0]
        self.b = numbers[1]
        self.mult = numbers[2]

    def toInt(self):
        self.remain = int(self.remain)
        self.a = int(self.a)
        self.b = int(self.b)
        self.mult = int(self.mult)

    def __repr__(self):
        return self.a + ' / ' + self.b + ' = ' + self.mult + " Remainder " + self.remain


if __name__ == "__main__":
    a = 12
    b = 5
    g = GCD(a, b)
    # print(g, end='')
    # print(g.output, end="\n\n")

    # lc = linComb(a, b, printStuff=True, steps=g.steps)
    lc = linComb(a, b, printStuff=True)











