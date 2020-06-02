#!/usr/bin/env python
# coding: utf-8

# # Changing Color of an Image

# In[61]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[76]:



# Load the image and convert to HSV colourspace
img = cv2.imread('A.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img)
plt.axis('off')


# In[77]:


NEW_COLOR = (255,0,0) #rbg for red (this is where synesthesia color would go)

# Define lower and uppper limits of what we call "black/gray"
black_lo=np.array([0,0,0]) #pure black lower limit
gray_hi=np.array([128,128,128]) #grey upper limit 

# Mask image to only select black/grey tones
mask = cv2.inRange(hsv,black_lo,gray_hi)

# Change image to new color where we found black before 
img[mask > 0]= NEW_COLOR

cv2.imwrite("result.png",img)
plt.imshow(img)
plt.axis('off')


# ### Another Image

# In[78]:


#FOR HANDWRITING IMAGE 
NEW_COLOR = (0,0,255) #rbg for blue (this is where synesthesia color would go)

# Load the aerial image and convert to HSV colourspace
img = cv2.imread('handwriting.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img)
plt.axis('off')


# In[79]:


# Define lower and uppper limits of what we call "black/grey"
black_lo=np.array([0,0,0]) #pure black lower limit
grey_hi=np.array([128,128,128]) #grey upper limit 

# Mask image to only select black/grey tones
mask=cv2.inRange(hsv,black_lo,grey_hi)

# Change image to red where we found black/grey tones
img[mask > 0]= NEW_COLOR

cv2.imwrite("result.png",img)
plt.imshow(img)
plt.axis('off')


# In[ ]:




