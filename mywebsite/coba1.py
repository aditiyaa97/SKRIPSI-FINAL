import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('Proposal_Aditiya.jpeg')

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()