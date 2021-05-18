import os

import imageio as imageio

from Presentation.LCG import LCG
from Presentation.graphIt import generateDict, plot_bar, generateCounts


def makeGif(lcg, numFrames, totalSamples, fileName, function, texts, sortIt=False, color="blue"):
    i = 1
    filenames = []
    frames = 0
    data = []
    while i < totalSamples:
        vals = function(totalSamples//numFrames)
        data.extend(vals)

        if sortIt:
            data.sort()
            d = generateCounts(data)
        else:
            d = generateDict(data)

        g = plot_bar(d, fileName, color, texts[0], texts[1], show=False)
        g.savefig("PicToGif/" + fileName + "_" + str(i) + ".png")
        g.close()
        filenames.append("PicToGif/" + fileName + "_" + str(i) + ".png")

        frames += 1
        print("%d Complete" % frames)
        i += (totalSamples//numFrames)


    # Create Gif
    with imageio.get_writer("PicsToGifOutput/" + fileName + ".gif", mode="I") as writer:
        for filename in filenames[1:]:
            image = imageio.imread(filename)
            writer.append_data(image)

            if filename == filenames[len(filenames)-1]:
                for i in range(30):
                    image = imageio.imread(filename)
                    writer.append_data(image)

    # Remove files
    for filename in set(filenames):
        os.remove(filename)

    print("\n\nCreated Gif!")



if __name__ == "__main__":
    print("NO CALL FROM MAIN ONLY")
