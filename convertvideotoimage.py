import subprocess
from subprocess import call
import os

images_dir_name = '/var/www/DataScience/Personal/Projects/VideoTask/YOLO_tensorflow/test/video'
video_dir_name = '/var/www/DataScience/Personal/Projects/VideoTask/YOLO_tensorflow/test/'


os.chdir(images_dir_name)

for i in range(1,20):
    file_name = images_dir_name+"/"+str(i)+".jpg"
    subprocess.check_output(["ffmpeg","-ss",str(i),"-i",video_dir_name+"19_Second_Football.mp4","-qscale:v","2","-vframes","1",file_name])


