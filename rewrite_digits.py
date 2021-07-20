"""
rewrites the "total" for each frame
"""
from FileCapture import ImageCapture, NextFrame
from PIL import Image
import read_digits
import write_digits
import ntpath

import sys
import os

def crop(img, rect):
    return img.crop(rect)    

OUT_WIDTH, OUT_HEIGHT = (104, 16)    
if __name__ == '__main__':
        
    if len(sys.argv) < 3:
        print ("parseVideo.py filename offset")
        print ("note there is no  .mp4")
        sys.exit()
    
    folder = sys.argv[1]
    offset = int(sys.argv[2])
           
    #reading rect
    text_rect = [238,249,238+71,249+14] # 0 -> 10000    
    # writing rect, the 7 digit total.
    write_rect = [206,212, 206+OUT_WIDTH,212+OUT_HEIGHT] # where we write to
    num_chars = 7 #note first digit is MILLIONS
    
    for item in os.listdir(folder):
        if not item.endswith('.png'):
            continue
        full_path = os.path.join(folder,item)
        img = Image.open(full_path)
        words = crop(img, text_rect)
        words.resize((500,100))
        num = read_digits.extract_digits(words, "cachekey")
        num = int(num)
        
        num += offset
        paste_img =  write_digits.write_digits(num, num_chars)
        paste_img = paste_img.resize((OUT_WIDTH,OUT_HEIGHT))
        img.paste(paste_img, write_rect[:2])
        img.save(full_path)
        print (item)
        
