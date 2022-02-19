import sys
import os
import shutil
import ntpath
import subprocess


full_path = sys.argv[1]
orig_file_name = ntpath.basename(full_path)
folder_path = ntpath.dirname(full_path)
file_name, ext = os.path.splitext(orig_file_name)

#convert from date time to just date
file_name = file_name.split()[0] 

print (orig_file_name, file_name + ext)
shutil.move(orig_file_name, file_name+ext)

subprocess.call(["mkv_to_mp4.bat", file_name+ext])
os.system(f'start cmd /K "cd /d D:/dev/DDRTimelapse & Drag-file-here.bat {file_name+ext}"')