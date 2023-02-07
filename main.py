import cv2
import os
path='Images'
buffer=[]
for file in os.listdir(path):
    file_name, ext=os.path.splitext(file)
    if ext in ['.png', '.jpg', '.webp', '.jfif', '.jpeg', '.gif', '.tiff']:
        buffer.append(f'{path}//{file_name}{ext}')
frame=cv2.imread(buffer[0])
width,height,channel=frame.shape
size=(width,height)
out=cv2.VideoWriter('result.mkv', cv2.VideoWriter_fourcc(*'mp4v'), 0.8, size)
for i in range(0, len(buffer)-1):
    frame=cv2.imread(buffer[i])
    out.write(frame)
out.release()
