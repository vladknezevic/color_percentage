def colorPercentage(img):
    import cv2
    import numpy as np 

    imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    blue = [0, 30]
    green = [31, 87]
    yellow = [88, 100]
    orange = [101, 112]
    red = [113, 137]
    purple = [138, 179]

    colors = [blue, red, green, yellow, orange, purple]
    colorStrings = ["blue", "red", "green", "yellow", "orange", "purple"]

    cp = {}
    ranges = []

    for i in range(len(colors)):
        ranges.append([np.array([colors[i][0], 20, 40]), np.array([colors[i][1], 255, 255])])
        mask = cv2.inRange(imgHSV, ranges[i][0], ranges[i][1])
        percentage = round(np.sum(mask == 255) / (mask.shape[0] * mask.shape[1]) * 100)
        cp[colorStrings[i]] = percentage

    whiteRange = [np.array([0, 0, 240]), np.array([255, 20, 255])]
    blackRange = [np.array([0, 0, 0]), np.array([255, 255, 39])]

    bw = [whiteRange, blackRange]
    bwStrings = ["white", "black"]

    for i in range(len(bw)):

        ranges.append(bw[i])
        mask = cv2.inRange(imgHSV, ranges[i+6][0], ranges[i+6][1])
        percentage = round(np.sum(mask == 255) / (mask.shape[0] * mask.shape[1]) * 100)
        print(bwStrings[i], percentage)
        cp[bwStrings[i]] = percentage

    return cp