"""
notation:
x = b mod m
Example:
x = 6 mod 13

input must be in the form:
[ (b,m) ]
aka a list of tuples

TODO Set the print for Linear Combination to AFTER everything is done
"""
from functools import reduce

from NumTheoryMath.linComb import linComb, GCD


def getInitialValues(arr):
    retVal = [1] * len(arr)
    for i in range(len(arr)):
        for x in range(len(retVal)):
            if x != i:
                retVal[x] *= arr[i][1]
    return retVal


def firstPrint(arr):
    for val in arr:
        print("X = %d (mod %d)" % (val[0], val[1]))
    print("Find X!")


def checkDivides(a, b):
    temp = float(a) / float(b)
    if temp == a // b:
        return True
    return False


def fancyPrint(baseVals, multVals):
    for i in range(len(baseVals)):
        print(baseVals[i], end='')
        for x in range(len(multVals[i])):
            if x != len(multVals[i]) - 1:
                print(" * (%d)" % multVals[i][x], end='')
            else:
                if i != len(baseVals) - 1:
                    print(" * (%d)" % multVals[i][x], end="     +     ")
                else:
                    print(" * (%d)" % multVals[i][x])


class ChineseRem:
    def __init__(self, arr, printStuff=False, printLC=False):
        self.firstX = None
        self.finalMod = None
        self.printStuff = printStuff
        self.printLC = printLC
        self.arr = arr
        if printStuff:
            firstPrint(arr)
            print("\n")
        self.x = self.loop()
        return

    def loop(self):
        # Just setting First Equation up using the X's b value
        retVal = getInitialValues(self.arr)
        storedMults = [[x[0]] for x in self.arr]
        storedPrints = []
        if self.printStuff:
            print("Base Values:")
            fancyPrint(retVal, storedMults)
            print()

        for i in range(len(self.arr)):
            if self.printStuff:
                print("Step %d of %d  -------------------------------------------------------------------------------------"
                      % (i + 1, len(self.arr)))
            gcd = GCD(retVal[i], self.arr[i][1])

            if checkDivides(self.arr[i][0], gcd.output):
                if self.printStuff:
                    print("%dx = %d (mod %d)" % (retVal[i], 1, self.arr[i][1]))
                    print("Find Linear Combination of %d and %d" % (retVal[i], self.arr[i][1]))
                    storedPrints.append([retVal[i], self.arr[i][1]])

                x0 = self.getX0(retVal[i], self.arr[i][1], gcd)
                storedMults[i].append(x0)

                if self.printStuff:
                    fancyPrint(retVal, storedMults)
                    print()

            # This means no solutions exist
            else:
                print("GCD(%d,%d) does NOT divide %d" % (retVal[i], self.arr[i][1], self.arr[i][0]))
                raise Exception("GCD(%d,%d) does NOT divide %d" % (retVal[i], self.arr[i][1], self.arr[i][0]))

        # Using our Multiplier
        for i in range(len(retVal)):
            for val in storedMults[i]:
                retVal[i] *= val

        # Final full print of values
        if self.printStuff:
            print("\nFINAL RESULT  " + "-"*84)
            for i in range(len(retVal)):
                if i != len(retVal) - 1:
                    print("%d + " % retVal[i], end="")
                else:
                    print("%d" % retVal[i])

        val = sum(retVal)  # Adding them up
        self.firstX = val
        val = self.bestVal(val)  # Find smallest positive value

        if self.printLC:
            print('\n\nLinear Combination Stuff\n', end='')
            print('*'*150 + "\n")
            for i in range(len(storedPrints)):
                print("Linear Combination %d Of %d [ lc(%d, %d) ]"
                      % (i + 1, len(storedPrints), storedPrints[i][0], storedPrints[i][1]), end='')
                print('-'*100)
                linComb(storedPrints[i][0], storedPrints[i][1], printStuff=self.printStuff)

        return val

    def getX0(self, a, m, gcd=None):
        if gcd is not None:
            lc = linComb(a, m, steps=gcd.steps, printStuff=False)
        else:
            lc = linComb(a, m, printStuff=False)
        return lc.finalSolution[0]

    def bestVal(self, val):
        if self.printStuff:
            print(val)

        # Find Lowest Positive Value
        mod = reduce((lambda x, y: x * y), ([i[1] for i in self.arr]))
        self.finalMod = mod
        times = 0  # Purely for printing
        while True:
            if val > 0:
                if val - mod <= 0:
                    break
                else:
                    times -= 1
                    val -= mod
            else:
                val += mod
                times += 1
        if self.printStuff:
            print("x = %d (mod %d)" % (val, mod))

        return val


def easyMake(args):
    if isinstance(args, str):
        args = [int(x) for x in args.split(' ')]
    if len(args) % 2 != 0:
        error = "Inputs are an Odd length, We only accept an Even number of inputs. You Gave %d inputs" % len(args)
        raise Exception(error)

    retVal = []
    for i in range(0, len(args), 2):
        retVal.append([args[i], args[i + 1]])
    return retVal


if __name__ == "__main__":
    vals = [[0, 2], [3, 12], [4, 13], [5, 17], [6, 19]]
    vals = easyMake([0, 2, 3, 12, 4, 13, 5, 17, 6, 19])
    vals = easyMake("1 999 2 1001 3 1003 4 1004 5 1007")
    cr = ChineseRem(vals, printStuff=True, printLC=True)
    # print(cr.x)  # X value
    # print(cr.firstX)  # First X value that we got before modding
    # print(cr.finalMod)  # Final Modulo
