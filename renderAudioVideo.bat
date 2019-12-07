ffmpeg -i test.mp4 -vn -b:a 320k test.wav
call parseVideo.py
call parseAudio.py
ffmpeg -i audio.wav -r 60 -i output/%%05d.png final.mp4