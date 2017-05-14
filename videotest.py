import YOLO_small_tf
from os import listdir
from os.path import isfile, join

yolo = YOLO_small_tf.YOLO_TF()

images_dir_name = 'test/video/'
# filename = 'test/football.jpg'

onlyfiles = [f for f in listdir(images_dir_name) if isfile(join(images_dir_name, f))]

print (onlyfiles)
for file in onlyfiles:
    # filename = images_dir_name + '2.jpg'
    filename = images_dir_name + file
    #Yolo settings
    yolo.disp_console = True
    # yolo.disp_console = False
    yolo.imshow = False
    yolo.tofile_img = 'test/output/' + file
    yolo.tofile_txt = 'test/output/' + file.replace(' ', '')[:-4] + '.txt'
    yolo.filewrite_img = True
    yolo.filewrite_txt = True

    yolo.detect_from_file(filename)

# yolo.detect_from_cvmat(cvmat)
