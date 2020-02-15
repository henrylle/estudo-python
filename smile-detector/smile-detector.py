import cv2

print(cv2.__version__)

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml') 

def detect (gray, frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), ((x+w), (y+h)), (255,0,0),2)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x +w]
        smiles=smile_cascade.detectMultiScale(roi_gray,1.8,20)
        
        for(sx,sy,sw,sh) in smiles:
          cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

    return frame

path_image='stage/foto.jpg'

img = cv2.imread(path_image)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canvas = detect(gray,img)

cv2.namedWindow('Foto', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Foto', canvas)

#Salvar imagem
#cv2.imwrite('foto_marcada.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# video_capture = cv2.VideoCapture(0)
# while True:
#   # Captures video_capture frame by frame
#   _, frame = video_capture.read()

#   # Capture image in monochrome
#   gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#   # Call the detect function
#   canvas = detect(gray,frame)

#   #Displays the result on camera feed
#   cv2.imshow('Video', canvas)

#   # The control breaks once q key is pressed
#   if cv2.waitKey(1) & 0xff == ord('q'):
#     break

# # Release the capture once all the processing is done.
# video_capture.release()
# cv2.destroyAllWindows()
