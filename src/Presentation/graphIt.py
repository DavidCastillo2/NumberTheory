import matplotlib.pyplot as plt


def generateDict(arr):
    d = {}
    for i in range(len(arr)):
        d[i] = arr[i]
    return d


def generateCounts(arr):
    arr.sort()
    retVal = {}
    for val in arr:
        try:
            retVal[val] = retVal[val] + 1
        except KeyError:
            retVal[val] = 1
    return retVal


def plot_bar(dic, title="Default", color='red', xText='Index - i', yText='Number Generated', show=True):
    plt.clf()
    fig = plt.figure(figsize=(11, 7), dpi=150)
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.5)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    plt.title(title, fontsize=24, loc="right")
    plt.xlabel(xText, fontsize=20)
    plt.ylabel(yText, fontsize=20)
    plt.bar(x=dic.keys(),
            height=dic.values(),
            color=color)
    if show:
        plt.show()
    return plt
