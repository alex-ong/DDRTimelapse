from pydub import AudioSegment
import sys
import os

framerate = 1000 / 60.0

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    
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
    result = speed_change(result, 16 / framerate)
    result.export(audio + "_processed" + ".wav",format="wav")
        
