import numpy as np
import cv2
import glob
import warnings
import os


cap = cv2.VideoCapture(0)
fourcc= cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        result.write(frame)
        cv2.imshow('output',frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break

if not os.path.exists('extracted images'):
    os.makedirs('extracted images')

def extracting2_frames(video_path):

    vid = cv2.VideoCapture(video_path)
    currentframe = 0
    frames_array = []

    while (True):
        success, frame = vid.read()
        cv2.imshow("Output",frame)
        cv2.imwrite('./extracted images/frame' + str(currentframe) + '.jpg',frame)
        currentframe +=1

        for images in  glob.glob("C:/Users/Lakshmi M/Desktop/sample folder/extracted images/*"):
            image_name = images.split("\\")[-1]
            img = cv2.imread(images)
            height, width, layers = img.shape
            size = (width,height)
            blur_images = cv2.blur(img,(10,10))
            frames_array.append(blur_images)

        fourcc = cv2.VideoWriter_fourcc(*'X264')
        blur = cv2.VideoWriter('blur_video.mp4', fourcc, 15.0, size)
        for i in range(len(frames_array)):
            blur.write(frames_array[i])

        if cv2.waitKey(1) & 0xFF == ord('r'):
            break
        

extracting2_frames('C:/Users/Lakshmi M/Desktop/sample folder/output.avi')
cap.release()
result.release()
cv2.destroyAllWindows()












































# import warnings
# import cv2
# import os
# import glob
# import numpy as np

# cap = cv2.VideoCapture(0)    
# fourcc = cv2.VideoWriter_fourcc(*'XVID')  
# out = cv2.VideoWriter('something.avi',fourcc, 20.0, (640,480))  

# while(cap.isOpened()):  
#     ret, frame = cap.read()  
#     if (ret==True):  
#         # frame = cv2.flip(frame,1)  
#         out.write(frame)  
#         cv2.imshow('frame',frame)  
#         if cv2.waitKey(1) & 0xFF == ord('q'):  
#             break 
#     else:
#         break


# cap.release()      
# cv2.destroyAllWindows()  




