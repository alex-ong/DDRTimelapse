from pydub import AudioSegment
import sys
import os

framerate = 1000 / 60.0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Usage: parseAudio.py file.mp4")
    framerate = 1000 / 60.0
    
    audio, ext = os.path.splitext(sys.argv[1])
    
    sound = AudioSegment.from_wav(audio + ".wav")
    
    frames = []
    with open(audio + "/" + "frameNumber.txt") as f:
        for line in f:
            frames.append(int(line))
    # len() and slicing are in milliseconds
    result = None
    
    for frame in frames:
        start = int(framerate*frame)
        clip = sound[start:start+16]
        print(len(clip))
        if result is None:
            result = clip
        else:
            result = result + clip

    result.export(audio + "_processed" + ".wav",format="wav")
        
