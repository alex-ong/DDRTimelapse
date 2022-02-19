ffmpeg -i %1 -map 0 -c copy "%~n1.mp4"
MOVE "%~n1.mp4" "D:/Dev/DDRTimelapse/%~n1.mp4"
