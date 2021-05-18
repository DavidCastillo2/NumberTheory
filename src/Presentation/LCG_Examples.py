from Presentation.LCG import LCG
from Presentation.graphIt import *

# NextNum = (a * Xn + C) % M


def makeExamples():
    bigNum = 1000
    generateGraphs = True

    # RANDU - Not random numbers!
    lcg = LCG(M=pow(2, 31), Xn=1, a=65539, C=0)
    vals = lcg.show(10000, False)
    d = generateDict(vals)
    if generateGraphs:
        g = plot_bar(d, "RANDU", show=False)
        g.savefig("Pics/RANDU - Really bad LCG.png")
        g.close()

    newVals = []
    for v in vals:
        if v % 2 == 0:
            newVals.append(v)
    d = generateDict(newVals)
    if generateGraphs:
        g = plot_bar(d, "RANDU - Only Even numbers", show=False)
        g.savefig("Pics/RANDU - Only Even numbers.png")
        g.close()

    lcg.reset()
    vals = lcg.modIt(100, 10, False)
    d = generateCounts(vals)
    if generateGraphs:
        g = plot_bar(d, "RANDU - Mod 10", show=False)
        g.savefig("Pics/RANDU - Mod 10.png")
        g.close()

    lcg.reset()
    vals = lcg.modIt(bigNum, 100, False)
    d = generateCounts(vals)
    if generateGraphs:
        g = plot_bar(d, "RANDU - Mod 100", 'red', 'Number Generated', 'Number Of Appearances', show=False)
        g.savefig("Pics/RANDU - Mod 100.png")
        g.close()




    # Really bad LCG() method
    lcg = LCG(2, 1, 4, 20)
    vals = lcg.show(100, False)
    d = generateDict(vals)
    if generateGraphs:
        g = plot_bar(d, "Really bad LCG", show=False)
        g.savefig("Pics/Reall bad LCG.png")
        g.close()

    # Really bad LCG() method
    lcg = LCG(2, 2, 4, 20)
    vals = lcg.show(100, False)
    d = generateDict(vals)
    if True:
        g = plot_bar(d, "Really bad LCG", color="blue", show=False)
        g.savefig("Pics/Really bad LCG - New Start.png")
        g.close()




    # The LCG vars used by Borland C/C++
    lcg = LCG(a=22695477, Xn=1, C=1, M=pow(2, 32))
    vals = lcg.show(10000, False)
    d = generateDict(vals)
    if generateGraphs:
        g = plot_bar(d, "Borland's C/C++ LCG method", 'purple', show=False)
        g.savefig("Pics/Borland's C_C++ LCG method.png")
        g.close()

    # Sorted Borland list
    vals.sort()
    d = generateDict(vals)
    if generateGraphs:
        g = plot_bar(d, "SORTED Borland's C/C++ LCG method", 'purple', show=False)
        g.savefig("Pics/SORTED Borland's C_C++ LCG method.png")
        g.close()

    # Unique count for each number generated - Theres are no repeats since Mod M is Massive
    lcg.reset()
    vals = lcg.show(bigNum, False)
    d = generateCounts(vals)
    if generateGraphs:
        g = plot_bar(d, "Borland - Unique Numbers", 'purple', 'Number Generated', 'Number Of Appearances', show=False)
        g.savefig("Pics/Borland - Unique Numbers.png")
        g.close()

    # Mod everything by 100 and see how many numbers are repeated
    lcg.reset()
    vals = lcg.modIt(bigNum, 100, False)
    d = generateCounts(vals)
    if generateGraphs:
        g = plot_bar(d, "Borland C/C++ Mod 100", 'purple', 'Number Generated', 'Number Of Appearances', show=False)
        g.savefig("Pics/Borland C_C++ Mod 100.png")
        g.close()




    # random0 - Referenced by many Author's regarding engineering
    lcg = LCG(a=8121, Xn=1, C=28411, M=134456)
    vals = lcg.modIt(bigNum, 100, False)
    d = generateCounts(vals)
    if generateGraphs:
        g = plot_bar(d, "random0 Mod 100", 'green', 'Number Generated', 'Number Of Appearances', show=False)
        g.savefig("Pics/random0 Mod 100.png")
        g.close()

    # random0 - Unique Count
    lcg = LCG(a=8121, Xn=1, C=28411, M=134456)
    vals = lcg.show(bigNum, False)
    d = generateCounts(vals)
    if generateGraphs:
        g = plot_bar(d, "random0 - Unique Numbers", 'green', show=False)
        g.savefig("Pics/random0 - Unique Numbers.png")
        g.close()



