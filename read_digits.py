# Code from:
# https://github.com/Brett824/NESTetrisCapture/blob/master/read_digits.py

import numpy as np
import imutils
import cv2
from imutils import contours


DIGITS = {}
DIGITS_BOOL = {}
REGION_CACHE = {}
BASE_RES = (50, 50)

filenames = ["0","1","2","3","4","5","6","7","8","9"]
def get_template_digits():
    for filename in filenames:
        ref = cv2.imread("images/%s.png" % filename)
        ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
        ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY)[1]
        refCnts = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        c = imutils.grab_contours(refCnts)[0]
        (x, y, w, h) = cv2.boundingRect(c)
        roi = ref[y:y + h, x:x + w]
        roi = cv2.resize(roi, BASE_RES)
        roi = imutils.resize(roi, height=BASE_RES[1])
        DIGITS[filename] = roi
        DIGITS_BOOL[filename] = roi != 0
    return DIGITS


def extract_digit(img, template=True):
    # either do correlation based template matching, take the highest scoring digit
    # or simply XOR two thresholded binary images, and take the most similar
    # template matching is significantly slower but more reliable - not good for production
    img = cv2.resize(img, BASE_RES)
    scores = []
    score = 0
    if not DIGITS:
        raise Exception("Tried reading digits without initializing templates")
    diffs = {}
    img_bool = img != 0 if not template else None
    for (digit, digitROI) in DIGITS.items():        
        if not template:
            diffs[digit] = np.count_nonzero(img_bool ^ DIGITS_BOOL[digit])
        else:
            result = cv2.matchTemplate(img, digitROI,
                                       cv2.TM_CCOEFF_NORMED)
            (_, score, _, _) = cv2.minMaxLoc(result)
            scores.append(score)
    if diffs:
        digit = min(diffs, key=diffs.get)
        if digit == "null":
            digit = 0
        return str(digit)
    if not score:
        return ''
        
    index = np.argmax(scores)
    if (scores[index] < 0.3):
        return "0"
    else:
        return str(index)
    


def extract_digits(img, cachekey, template=False, length=None, thresh=80):
    """
    expects image as an np array that is in BGR.
    """
    result = ""    
    
    ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, ref = cv2.threshold(ref, thresh, 255, cv2.THRESH_BINARY)    
    
    if not REGION_CACHE.get(cachekey):    
        good_rects = []
        tileWidth = int(len(img[0]) / 5)
        tileHeight = int(len(img))
        for i in range(5):
            good_rects.append([tileWidth*i,0,tileWidth,tileHeight])
        
        REGION_CACHE[cachekey] = good_rects
            
    rects = REGION_CACHE[cachekey]
    
    for x, y, w, h in rects:        
        orig_roi = ref[y:y + h, x:x + w]        
        result += extract_digit(orig_roi, template=template)
        first = False

    return result

get_template_digits()
