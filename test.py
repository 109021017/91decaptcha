import cv2
from os import walk
import os.path
import decaptcha

files = []
for (_, _, filenames) in walk('testimgs/'):
    files.extend(filenames)

accurateNum = 0
for f in files:
    path = os.path.join('testimgs/', f)
    img = cv2.imread(path, 0)
    prediction = decaptcha.decaptcha(img)
    if prediction == f[:4]:
        accurateNum += 1
print("accuracy: %d/%d" % (accurateNum, len(files)))
