import streamlit as st
import numpy as np # linear algebra
import pandas as pd
import numpy as np
import pandas as pd
from pathlib import Path
import os.path
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from PIL import Image


model = tf.keras.models.load_model('final.h5')
Labels = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 
'sweetpotato', 'tomato', 'turnip', 'watermelon']

def output(img):
    pil_image = Image.open(img)
    new_size = (224,224)
    img = pil_image.resize(new_size)
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = Labels[y]
    return res,answer[0][y]

st.header('Capture and Search')
uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'png', 'jpeg'])
# st.write(type(uploaded_image))
if uploaded_image is not None:
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    a,b = output(uploaded_image)
    if(b > 0.75):
        
        st.write("A match was found for the given image in our database")
        st.markdown(f"Image matches <b>{a}</b>", unsafe_allow_html=True)     
        st.write("Confidence: ",b)  
    else:
        st.write("Image does not match with any item in our database")