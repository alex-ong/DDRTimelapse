set myvar=%1
echo %myvar%
set myvar=%~n1
echo %myvar%
call renderAudioVideoNoPad.bat %myvar%