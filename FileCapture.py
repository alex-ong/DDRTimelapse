import os
import cv2
from PIL import Image
import time
from vidgear.gears import CamGear

class FileMgr():
    def __init__(self):
        self.videoFile = None
        self.imgBuf = None
        self.frameRate = None
        self.frameCount = 0
        self.totalFrames = 1

    def videoCheck(self, fileName):
        if self.videoFile is None:
            self.videoFile = CamGear(fileName).start()                     
            self.frameRate = self.videoFile.stream.get(cv2.CAP_PROP_FPS)            
            self.totalFrames =  int(self.videoFile.stream.get(cv2.CAP_PROP_FRAME_COUNT))
            self.NextFrame()
                
    def ImageCapture(self, rectangle, fileName):
        self.videoCheck(fileName)
        if rectangle is None:
            return self.imgBuf
        return self.imgBuf.crop([rectangle[0],
                                rectangle[1],
                                rectangle[0]+rectangle[2],
                                rectangle[1]+rectangle[3]])        

    def NextFrame(self):        
        if self.videoFile is not None:
            cv2_im = self.videoFile.read()
            if cv2_im is not None:
                #cv2_im = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
                self.imgBuf = cv2_im # bgr
                self.frameCount += 1
                if (self.frameCount % 1000 == 0):
                    print (self.frameCount, '{0:.2f}'.format(self.frameCount*100.0/self.totalFrames)+"% complete")
                return (True, self.frameCount, self.totalFrames)
    
        return (False, self.frameCount, self.totalFrames)

    def TimeStamp(self):
        if self.frameRate is not None:
            return self.frameCount * (1.0/self.frameRate)
        return time.time()


imgCap = FileMgr()

def ImageCapture(rectangle, filename=None):
    """returns BGRA image"""
    global imgCap
    return imgCap.ImageCapture(rectangle,filename)

#returns false if we want to exit the program
def NextFrame():
    global imgCap
    return imgCap.NextFrame()
