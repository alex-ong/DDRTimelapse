ffmpeg -i "%1" -map 0 -c copy "%~n1.mp4"
COPY "%~n1.mp4" "C:/Drive_D/Dev/DDRTimelapse/%~n1.mp4"
pause