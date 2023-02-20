import os
from PIL import Image
import cv2

def traverse_dir_files(root_dir, ext=None):    
    paths_list = []
    full_list = []
    for parent, _, fileNames in os.walk(root_dir):
        for name in fileNames:
            if name.startswith('.') :  # 去除隐藏文件
                continue
            if ext:  # 根据后缀名搜索
                if name.endswith(tuple(ext)):
                    paths_list.append(parent)
                    full_list.append(os.path.join(parent, name))
            else:
                paths_list.append(parent)
                full_list.append(os.path.join(parent, name))
    return paths_list,full_list

p_list,f_list = traverse_dir_files('G:/MKT/train code/Flick','.jpg')

print(f_list)
# pathstr = p_list.pop(0)
# im2 = Image.open(filestr)

def get_picture_sharpness(filestr):
	image = cv2.imread(filestr)
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	image_var = str(int(cv2.Laplacian(image_gray, cv2.CV_64F).var()))
	# image_var = str(int(cv2.Laplacian(image_gray, cv2.CV_16U).var()))


	font_face = cv2.FONT_HERSHEY_COMPLEX
	font_scale = 1
	thickness = 1
	baseline = 0

	var_size = cv2.getTextSize(image_var, font_face, font_scale, thickness)
	# 清晰度值的绘制位置
	draw_start_point = (20, var_size[0][1] + 10)
	cv2.putText(image, image_var, draw_start_point, font_face, font_scale, (0,0,255), thickness)

	# cv2.imshow('frame', image)
	cv2.waitKey(0)

	return image_var

# sharpness_list = []
txt = open("G:/MKT/train code/quality.txt", 'w')
for i in range(len(f_list)):
    file_path = f_list.pop(0)
    filestr = file_path.replace('\\', '/')
    print(filestr)
    txt.write(file_path+","+get_picture_sharpness(filestr) + '\n')
txt.close()
