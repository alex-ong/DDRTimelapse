from pydub import AudioSegment

framerate = 1000 / 60.0

sound = AudioSegment.from_wav("test.wav")
print(len(sound))
frames = []
with open("frameNumber.txt") as f:
    for line in f:
        frames.append(int(line))
# len() and slicing are in milliseconds
result = None
print (len(frames))
for frame in frames:
    start = int(framerate*frame)
    clip = sound[start:start+16]
    print(len(clip))
    if result is None:
        result = clip
    else:
        result = result + clip

result.export("audio.wav",format="wav")
    
