#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'model_vgg_plant.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
    test_image = load_img(tomato_plant, target_size = (224, 224)) # load image 
    print("@@ Got Image for prediction")
  
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
    result = model.predict(test_image) # predict diseased palnt or not
    print('@@ Raw result = ', result)
  
    pred = np.argmax(result, axis=1)
    print(pred)
                            
                                                                                                                                             
    if pred==0:
        return "AppleScab", 'AppleScab.html'
       
    elif pred==1:
        return "Disease2", 'Disease2.html'
        
    elif pred==2:
        return "CedarAppleRust", 'CedarAppleRust.html'
        
    elif pred==3:
        return "healthy", 'healthy.html'   # apple healthy
       
    elif pred==4:
        return "healthy", 'healthy.html'    # bluberry healthy
        
    elif pred==5:
        return "healthy", 'healthy.html'    # cherry healthy
        
    elif pred==6:
        return "Powdery_Mildew", 'Powdery_Mildew.html'
        
    elif pred==7:
        return "Corn_GreySpot", 'Corn_GreySpot.html'  
    
    elif pred==8:
        return "Corn_GreySpot", 'Corn_GreySpot.html'   # corn common rust
    
    elif pred==9:
        return "healthy", 'healthy.html'   # corn common rust
    
    elif pred==10:
        return "NorthernleaffBlight", 'NorthernleaffBlightt.html'  # corn
    
    elif pred==11:
        return "Grape_Rot",'Grape_Rot.html'  #grape rot
    
    elif pred==12:
        return "Grape_Rot", 'Grape_Rot.html'# grape esca

    
    elif pred==13:
        return "Grape___healthy", 'Grape___healthy.html'
    
    elif pred==14:
        return "Grape_Leafblight", 'Grape_Leafblight.html'
    
    elif pred==15:
        return "Orange_CitrusGreen", 'Orange_CitrusGreen.html'
    
    elif pred==16:
        return "Peach_LeafSpot", 'Peach_LeafSpot.html'
    
    elif pred==17:
        return "healthy", 'healthy.html'     # peaches
    
    elif pred==18:
        return "Pepper,_bell___Bacterial_spot", 'Pepper,_bell___Bacterial_spot.html'
    
    elif pred==19:
        return "Pepper,_bell___healthy", 'Pepper,_bell___healthy.html'
    
    elif pred==20:
        return "Potato_Blight", 'Potato_Blight.html'
    
    elif pred==21:
        return "Potato___healthy", 'Potato___healthy.html'
    
    elif pred==22:
        return "Potato_LateBlight", 'Potato_LateBlight.html'
    
    elif pred==23:
        return "healthy", 'healthy.html'  # raspberry
    
    elif pred==24:
        return "healthy", 'healthy.html'   # soyabean
    
    elif pred==25:
        return "squash powdery mildew ", 'squash powdery mildew .html'
    
    elif pred==26:
        return "healthy", 'healthy.html'    # strawberry
    
    elif pred==27:
        return "Strawberry Leaf Scorch", 'Strawberry Leaf Scorch.html'
    
    elif pred==28:
        return "TomatoBacterialSpot", 'TomatoBacterialSpot.html'
    
    elif pred==29:
        return "TomatoEarlyBlight", 'TomatoEarlyBlight.html'
    
    elif pred==30:
        return "healthy", 'healthy.html'  # tomato
    
    elif pred==31:
        return " TomatoLateBlight", 'TomatoLateBlight.html'
    
    elif pred==31:
        return "TomatoLeafMold" , 'TomatoLeafMold.html'
    
    elif pred==32:
        return "SeptoriaLeafSpot", 'SeptoriaLeafSpot.html'
    
    elif pred==33:
        return "TomatoSpiderBite", 'TomatoSpiderBite.html'
    
    elif pred==34:
        return "TomatoTargetSpot", 'TomatoTargetSpot.html'
    
    elif pred==35:
        return "TomatoMosiacVirus", 'TomatoMosiacVirus.html'
    
    elif pred==36:
        return "TomatoYellowLeafCurlVirus", 'TomatoYellowLeafCurlVirus.html'
    

     
# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('main.html')
    
#get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=3000) 


# In[ ]:



