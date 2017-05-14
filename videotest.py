import YOLO_small_tf
yolo = YOLO_small_tf.YOLO_TF()

images_dir_name = '/var/www/DataScience/Personal/Projects/VideoTask/YOLO_tensorflow/test/video/'
# filename = 'test/football.jpg'
filename = images_dir_name + '2.jpg'

#Yolo settings
yolo.disp_console = True
# yolo.disp_console = False
yolo.imshow = False
yolo.tofile_img = 'test/output/football1.jpg'
yolo.tofile_txt = 'test/output/football1.txt'
yolo.filewrite_img = True
yolo.filewrite_txt = True

yolo.detect_from_file(filename)
# yolo.detect_from_cvmat(cvmat)
