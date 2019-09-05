import urllib.request
import cv2
import numpy as np
from dbMgr import insert_db,login_db,select_img
import face_recog
import socket

# while true 문으로  0.5초마다 마지막줄 사진 받아아와서 gen() 함수 마냥 while true문 돌려봐
print(socket.gethostbyname(socket.getfqdn()))


#cv2.imshow('tmp',result)
#cv2.waitKey(0)
#print (img)

