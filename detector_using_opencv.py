import cv2




from random import randrange #यहाँ पर ये rectangle का random colours put करेगा: randomrange(256)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('RDJ.jpg')
# '''
# # type1: outputs
# cv2.imshow('face Detector tasveer', img)
# cv2.waitKey()
# '''
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# '''
# # type2 : outputs
# cv2.imshow('face Detector tasveer', gray_img)
# cv2.waitKey()
# '''
# #FaceDetectionaTool
# # type3
# face_coordinates = face_cascade.detectMultiScale(gray_img)
# '''
# print(face_coordinates)
# '''
# #DrawReactangleAroundTheFace
# # type4
# '''
# (x,y,w,h)= face_coordinates[0]
# cv2.rectangle(img,(x, y), (x+w, y+h),(0,250,0), 1)
# print(face_coordinates)
# cv2.imshow('face Detector tasveer', img)
# cv2.waitKey()
# '''


# #DrawReactangleAroundTheFaces
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# img = cv2.imread('RDJ1.jpg')
# face_coordinates = face_cascade.detectMultiScale(img)
# for (x,y,w,h) in face_coordinates:
#     cv2.rectangle(img,(x, y), (x+w, y+h),(0,255,0), 1)
# cv2.imshow('face Detector tasveer', img)
# cv2.waitKey()



######################################################################
'''                      USING CAMERA                              '''

#type1:
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# webcam = cv2.VideoCapture(0)
# while True:
#     sucessful_frame_read, frame = webcam.read()
#     grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('face Detector tasveer', grayscaled_img)
#     cv2.waitKey()
# #type2:
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# webcam = cv2.VideoCapture(0)
# while True:
#     sucessful_frame_read, frame = webcam.read()
#     grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('face Detector tasveer', grayscaled_img)
#     cv2.waitKey(1)
#type3:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
while True:
    sucessful_frame_read, frame = webcam.read()
    face_coordinates = face_cascade.detectMultiScale(frame)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x, y), (x+w, y+h),(randrange(256),randrange(256),randrange(256)), 5)
    cv2.imshow('face Detector tasveer', frame)
    key = cv2.waitKey(1)
    if key==27 :  #27 stands for ascii code key of ESC button
        break

webcam.release()