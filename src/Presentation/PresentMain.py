from functools import partial
import random

from Presentation.GifLand import makeGif
from Presentation.LCG import LCG
from Presentation.graphIt import *
from Presentation.LCG_Examples import makeExamples

# NextNum = (a * Xn + C) % M

if False:
    # makeExamples()

    # Borland
    lcg = LCG(a=22695477, Xn=1, C=1, M=pow(2, 32))
    command = partial(lcg.modIt, mod=100, printIt=False)

    makeGif(lcg, 30, 10000, "Borland Mod 100", command,
            ["index - i", "Number Generated"], color="purple")


    lcg = LCG(a=22695477, Xn=1, C=1, M=pow(2, 32))
    command = partial(lcg.modIt, mod=100, printIt=False)

    makeGif(lcg, 60, 10000, "Sorted Borland Mod 100", command,
            ["Number Generated", "Number Of Occurrences"], sortIt=True, color="purple")


    # Random 0
    lcg = LCG(a=8121, Xn=1, C=28411, M=134456)
    command = partial(lcg.modIt, mod=100, printIt=False)

    makeGif(lcg, 60, 10000, "Sorted Random0", command,
            ["Number Generated", "Number of Occurrences"], sortIt=True, color="pink")

    makeGif(lcg, 60, 10000, "Sorted Random0 - 2", command,
            ["Number Generated", "Number of Occurrences"], sortIt=True, color="pink")

    makeGif(lcg, 60, 10000, "Sorted Random0 - 3", command,
            ["Number Generated", "Number of Occurrences"], sortIt=True, color="pink")



    # Python
    def pythonRandom(nums):
        retVal = []
        for i in range(nums):
            retVal.append(random.randint(0, 99))
        return retVal


    lcg = LCG(a=22695477, Xn=1, C=1, M=pow(2, 32))
    command = partial(pythonRandom)

    makeGif(lcg, 60, 10000, "Sorted Python Mod 100", command,
            ["Number Generated", "Number Of Occurrences"], sortIt=True, color="green")

