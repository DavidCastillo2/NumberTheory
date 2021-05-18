from NumTheoryMath.ChineseRem import *
from NumTheoryMath.ResidueSystem import *
from NumTheoryMath.linComb import *
from NumTheoryMath.ToNewBase import *


# GCD - Used for Inverse Modulo
# print(GCD(12, 23), end="\n\n")


# Chinese Remainder Theorem
vals = easyMake("2 3 3 5 5 8")
ChineseRem(vals, printStuff=True, printLC=True)


# Linear Combination - Linear Congruence - Eculdian Distance
# linComb(45, 63, printStuff=True)


# Residue System
# ResidueSystem("9 17 85", 3, printStuff=True)


# New Base
# convert(47, 2)


