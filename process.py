from FileCapture import ImageCapture, NextFrame
from PIL import Image
import sys
def crop(img, rect):
    return img.crop(rect)    
items = ["0","1","2","3","4","5","6","7","8","9","null"]

images = {}
for i in items:
    images[i] = Image.open("images/"+i+".png")
    
if __name__ == '__main__':
    frameCount = 0
    filename = "test.mp4"
    rect = [0,0,1280,720]
    textRect = [238,249,238+71,249+14]
    img = ImageCapture(rect,filename)
    while True:
        canProcess, frameNumber,vidframeCount = NextFrame()
        if (frameNumber % 1000 == 0):
            print(frameNumber,vidframeCount)
        if not canProcess:
            break    
        if frameNumber >= 40000:
            img = ImageCapture(rect)
            words = crop(img,textRect)
            words.show()
            sys.exit()