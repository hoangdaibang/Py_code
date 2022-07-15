import cv2
import dlib


#load detector 
detector = dlib.get_frontal_face_detector()

#load predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#read the image
cap = cv2.VideoCapture(0)






if __name__ == "__main__":
    main()
