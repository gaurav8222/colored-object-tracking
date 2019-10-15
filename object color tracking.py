
# coding: utf-8

# In[ ]:


#OBJECT TRACKING WITH COLOR
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret, frame=cap.read()
else:
    ret=False
    
    
while ret:
    ret, frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low=np.array([100,50,50])
    high=np.array([140,255,255])
    
    image_mask=cv2.inRange(hsv,low,high)
    
    output=cv2.bitwise_and(frame,frame,mask=image_mask)
    
  
    cv2.imshow('image_mask',image_mask)
    cv2.imshow("ORIGINAL IMAGE FEED",frame)
    cv2.imshow("TRACKING IMAGE IS",output)
    if cv2.waitKey(1)==27:
        break
        

cv2.destroyAllWindows()        
cap.release()

