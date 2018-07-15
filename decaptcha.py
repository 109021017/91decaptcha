import cv2
import numpy as np
import os.path


def remove_background(img):
    img[img == 110] = 255
    img[img == 180] = 255
    img[img == 220] = 255


def decaptcha(img):
    remove_background(img)
    prediction = ''
    for i in range(0, 4):
        min_diff = 10000
        min_diff_num = 0
        for n in range(0, 10):
            num_img = nums[n]
            roi = img[:, (i + 1) * 11: (i + 1) * 11 + num_img.shape[1]]
            diff = cv2.absdiff(num_img, roi)
            avg_diff = np.average(diff)
            if avg_diff < min_diff:
                min_diff = avg_diff
                min_diff_num = n
        prediction += str(min_diff_num)
    return prediction


nums = []
for i in range(0, 10):
    numFile = os.path.join('nums/', str(i)+'.png')
    numImg = cv2.imread(numFile, 0)
    nums.append(numImg)
