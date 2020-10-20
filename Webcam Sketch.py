#!/usr/bin/env python
# coding: utf-8

# # Webcam Sketch

# In[15]:


import cv2
import numpy as np


# In[24]:


def sketch(image):
    image2=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
    #removing blur so that the pixels averge out and clear images are obtained
    image2=cv2.GaussianBlur(image2,(7,7),0)
    
    image2=cv2.Canny(image2,30,70)
    ret,image2=cv2.threshold(image2,20,255,cv2.THRESH_BINARY_INV)
    return image2


# In[25]:


cap=cv2.VideoCapture(0) #capturing frame from webcam
while True:
    ret,frame=cap.read() #reading the frame
    cv2.imshow("My Sketch",sketch(frame)) 
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:




