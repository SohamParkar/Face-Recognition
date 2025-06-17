import cv2
#Load the Haar cascade for face detection
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  
#Start capturing video from the default webcam
b = cv2.VideoCapture(0)  

while True:
    #Read a frame from the webcam
    c_box, d_face = b.read()  
    #Convert the frame to grayscale
    e = cv2.cvtColor(d_face, cv2.COLOR_BGR2GRAY)  
    #Detect faces in the frame
    f = a.detectMultiScale(e, 1.3, 6)  

    #Loop through detected faces
    for (x1, y1, w1, h1) in f: 
        #Draw a green rectangle around each face
        cv2.rectangle(d_face, (x1, y1), (x1+w1, y1+h1), (0,255,0), 5)  


    #Display the frame with rectangles
    cv2.imshow("img", d_face)  
    #Wait for 40 milliseconds for a key press
    h = cv2.waitKey(40) & 0xff  
    if h == 40:  
        break

#Release the webcam
b.release()  
#Close all OpenCV windows
cv2.destroyAllWindows()  
