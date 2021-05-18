def ResidueSystem(arr, mod, printStuff=False):
    # Just make it easier to input values
    if isinstance(arr, str):
        arr = [int(x) for x in arr.split(' ')]

    # Actually do the stuff
    finalBool = True
    baseArr = [x for x in range(0, mod)]  # All numbers less than our Mod
    if printStuff:
        print("Base Array: ")
        print(baseArr)
    newArr = []  # Stores our added values from arr
    for val in arr:
        num = val % mod
        if not baseArr.__contains__(num):
            print("%d mod %d = %d\t\t %d is not in our Base List." %(val, mod, num, num))
            finalBool = False

        # New value that exists inside of BaseArray
        if not newArr.__contains__(num):
            newArr.append(num)
            if printStuff:
                print("%d mod %d = %d\t\t %d Has been added to List as %d." %(val, mod, num, val, num))
        else:
            # Already had this value, so it is not part of the list
            if printStuff:
                print("%d mod %d = %d\t\t %d is a duplicate, so this is not a complete residue system." % (val, mod, num, num))
            finalBool = False

    # Final compare just for clean printing
    print()
    for baseVal in baseArr:
        if not newArr.__contains__(baseVal):
            if printStuff:
                print("%d from our BaseArray is not in our NewArray." % baseVal)
            finalBool = False
    if printStuff and finalBool:
        print("NewArray has all values in BaseArray, This is a Complete Residue Set.")
    if printStuff and not finalBool:
        print("NewArray does NOT contain all values in BaseArray, this is NOT a complete residue set.")
    return finalBool


if __name__ == "__main__":
    ResidueSystem("1 2 3 4 5 6 7 2", 8, printStuff=True)




