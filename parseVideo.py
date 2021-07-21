from FileCapture import ImageCapture, NextFrame
from PIL import Image
import read_digits
import ntpath

import cv2
import sys
import os
import time

def crop(image_buf, rect):
    x, y, end_x, end_y = rect    
    
    crop_img = image_buf[y:end_y,x:end_x]
    return crop_img
    
if __name__ == '__main__':
        
    if len(sys.argv) < 2:
        print ("parseVideo.py filename")
        print ("note there is no  .mp4")
        sys.exit()
    
    filename = sys.argv[1] + ".mp4"
    try:
        name, ext = os.path.splitext(filename)
        os.mkdir(name)
    except:
        pass
        
    rect = [0,0,1280,720]
    textRect = [238,249,238+71,249+14] # regular layout
    textRect2 = [224,405, 224+68, 405+13] # no pad
    if len(sys.argv) >= 3 and sys.argv[2] == "nopad":
        textRect = textRect2
        
    img = ImageCapture(None,filename)
    lastNumber = -1
    
    oframeCount = 0
    oframeNumbers = []
    
    t = time.time()
    while True:
        canProcess, vidframeNumber, vidframeCount = NextFrame()
        
        if not canProcess:
            break    
        
        img = ImageCapture(None)
        words = crop(img, textRect)                    
        
        
        num = read_digits.extract_digits(words, "cachekey")
        if num != lastNumber:
            lastNumber = num                                  
            oframeCount += 1
            oframeNumbers.append(vidframeNumber)
            # only convert to rgb at last possible stage
            png_compat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(png_compat)
            img.save(name + "/" + "{:05d}".format(oframeCount)+ ".png", compress_level=3)
        
        if vidframeNumber % 1000 == 0:
            print (f"Frames per second: {vidframeNumber/(time.time() - t)}")

    oframeNumbers = (str(i) for i in oframeNumbers)
    with open(name + "/frameNumber.txt", 'w') as f:
        f.writelines("\n".join(oframeNumbers))