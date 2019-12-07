from FileCapture import ImageCapture, NextFrame
from PIL import Image
import read_digits

import sys
def crop(img, rect):
    return img.crop(rect)    

    
if __name__ == '__main__':
    
    filename = "test3.mp4"
    rect = [0,0,1280,720]
    textRect = [238,249,238+71,249+14]
    img = ImageCapture(rect,filename)
    lastNumber = -1
    
    oframeCount = 0
    oframeNumbers = []
    
    while True:
        canProcess, vidframeNumber,vidframeCount = NextFrame()
        
        if not canProcess:
            break    
        
        img = ImageCapture(rect)
        words = crop(img,textRect)                    
        words = words.resize((500,100))
        num = read_digits.extract_digits(words, "cachekey")
        if num != lastNumber:
            lastNumber = num                                  
            oframeCount += 1
            oframeNumbers.append(oframeCount)
            img.save("output/" + "{:05d}".format(oframeCount)+ ".png")
    print("done!")
    with open("output/frameNumber.txt", 'w') as f:
        f.writelines("\n".join(soframeNumbers))