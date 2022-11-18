import cv2
import numpy as np
import time

class Cam:
    """properties
        cap, ret, frame, before, after
    """
    
    def __init__(self):
        self.CAM_WIDTH = 720
        self.CAM_HEIGHT = 1280
        
        self.cap = cv2.VideoCapture(0)#, cv2.CAP_V4L2)

        if not self.cap.isOpened():
            print("cam is not opened")
            exit()

        # set dimensions
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.CAM_WIDTH)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.CAM_HEIGHT)

    def capture(self):
        
        self.ret, self.frame = self.cap.read()
        
        if self.ret == False:
            print("ret is False")
            exit()
        
        # take an after picture
        cv2.imwrite('../../after.jpg', self.frame)
        
        # if you want a photo to test, use this code.
        
        # print("write")
        # cv2.imwrite('../../before.jpg', self.frame)
        # print("finish")
        
        # cv2.imshow('frame', self.frame)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # exit()


        self.before = cv2.imread('../../before.jpg')
        self.after = self.frame

        # RGB to YCbCr
        self.before = cv2.cvtColor(self.before, cv2.COLOR_BGR2YCR_CB)
        self.after = cv2.cvtColor(self.after, cv2.COLOR_BGR2YCR_CB)

    def processing(self):
        
        coordinates = {}

        # total = 0
        
        # if self.after == None:
            # print("Didn't take a picture")
          
        # subtract the images
        subtracted = cv2.subtract(self.before, self.after)
    
        blur = cv2.GaussianBlur(subtracted, ksize=(3,3), sigmaX=0)

        self.ret, thresh1 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY)

        edged = cv2.Canny(blur, 0, 255)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        contours_image = cv2.drawContours(subtracted, contours, -1, (0,255,0), 3)

        cv2.imwrite('../../ccontour.jpg', contours_image)

        contours_xy = np.array(contours)

        contour_center = []
        for i in range(len(contours)):
            contours_mean = np.mean(contours[i], axis = 0)
            contour_center.append(contours_mean)

        for i in range(len(contour_center)):
            temp = contour_center[i][0]
            temp = temp.tolist()
            x = int(temp[0])
            y = int(temp[1])
            # print(temp)
            # print(temp[0])
            #contours_image[y, x] = [255,0,0]
            contours_image[y, x] = [128,128,5]
            
            coordinates[f"{i}"] = f"({x}, {y})"

        return coordinates

    def getImage(self):
        
        self.ret, self.frame = self.cap.read()
        
        if self.ret == False:
            print("ret is False")
            exit()

        return self.frame
 

