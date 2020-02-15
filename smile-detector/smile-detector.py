import cv2

print(cv2.__version__)

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml') 
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml') 

def has_smile (gray, frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    tem_sorriso=False
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), ((x+w), (y+h)), (255,0,0),2)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x +w]
        smiles=smile_cascade.detectMultiScale(roi_gray,1.8,20)        
        for(sx,sy,sw,sh) in smiles:                    
          if sx>=0:
            tem_sorriso=True
          cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

    return tem_sorriso

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

path_image_sem_sorriso='stage/IMG_4067.JPG'
path_image_com_sorriso='stage/foto.jpg'

print ('Imagem sem sorriso')
img_1 = cv2.imread(path_image_sem_sorriso)
gray=cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)


if has_smile(gray,img_1):
  print (' Encontrei um sorriso')
  canvas = detect(gray,img_1)
  cv2.namedWindow('Foto1', cv2.WINDOW_GUI_EXPANDED)
  cv2.imshow('Foto1', canvas)
else:
  print (' Nada de sorriso por aqui')  


print ('Imagem com sorriso')
img_2 = cv2.imread(path_image_com_sorriso)
gray=cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)

if has_smile(gray,img_1):
  print (' Encontrei um sorriso')
  canvas = detect(gray,img_2)
  cv2.namedWindow('Foto2', cv2.WINDOW_GUI_EXPANDED)
  cv2.imshow('Foto2', canvas)
else:
  print (' Nada de sorriso por aqui')  


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
