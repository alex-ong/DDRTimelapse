ffmpeg -i %1.mp4 -vn -b:a 320k %1.wav
call python parseVideo.py %1 nopad
call python parseAudio.py %1
ffmpeg -i %1_processed.wav -r 60 -i %1/%%05d.png %1_processed.mp4