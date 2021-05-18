"""
Takes in:
    A, the number we start with.
    baseB, the base we want to convert A to.
    baseA, OPTIONAL if A is not base 10, you can set its base here.
"""


def convert(a, baseB, baseA=10):
    print("%d base: %d  -> base: %d" % (a, baseA, baseB))
    if baseA != 10:
        a = sendToBase10(a, baseA)
    retVal = []
    while True:
        maxDiv = a // baseB
        if maxDiv == 0:
            print('Operation: %d / %d = %d remainder %d\t->\tEND MET!' % (a, baseB, maxDiv, a))
            retVal.append(a)
            break
        else:
            rem = a - baseB * maxDiv
            print('Operation: %d / %d = %d remainder %d' % (a, baseB, maxDiv, rem))
            a = maxDiv
            retVal.append(rem)

    retVal = arrToInt(retVal)
    print("Result: " + str(retVal) + "\n")


# backend method
def arrToInt(a):
    retVal = 0
    for i in range(len(a)):
        if i == 0:
            retVal += a[i]
        else:
            retVal += a[i] * pow(10, i)
    return retVal


# backend method
def getDigitsReversed(num):
    digits = []
    while True:
        maxDiv = num // 10
        if maxDiv == 0:
            digits.append(num)
            break
        else:
            rem = num - maxDiv * 10
            num = maxDiv
            digits.append(rem)
    return digits


# can call, A is input baseA is obviously A's base
def sendToBase10(a, baseA):
    digits = getDigitsReversed(a)
    retVal = 0
    print(str(a) + " To base 10:")
    for i in range(len(digits)):
        retVal += digits[i] * pow(baseA, i)
        if i == len(digits) - 1:
            print("(%d * %d^%d) = %d" % (digits[i], baseA, i, retVal), end='\n')
        else:
            print("(%d * %d^%d) + " % (digits[i], baseA, i), end='')
    return retVal


if __name__ == "__main__":
    # convert(1999, 7)

    # print(sendToBase10(100100010101, 2))

    convert(47, 2)


