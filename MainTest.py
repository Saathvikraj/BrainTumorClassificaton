import cv2
from keras.models import load_model
from PIL import Image
import numpy as np
model=load_model('BrainTumor10EpochsCategorical.h5')
image=cv2.imread('C:\\Users\\Saathvik\\Brain tumor\\datasets\\yes\\y0.jpg')
img=Image.fromarray(image)
img=img.resize((64,64))
img=np.array(img)
input_img=np.expand_dims(img,axis=0)
result=model.predict_step(input_img)
print(result)