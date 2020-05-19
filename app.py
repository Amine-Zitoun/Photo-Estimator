from flask import Flask,request,render_template,url_for,flash,redirect,jsonify
from follow import follow
from InstagramAPI import InstagramAPI
import urllib.request,json
import random
import os
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import json
import numpy as np
from PIL import Image
import cv2
import base64
import io
import pickle
import time



IMG_SIZE = 80
training_data = []
likes = []


instaApi = InstagramAPI(USERNAME, PASSWORD)
instaApi.login()

def get_userID(username):
	instaApi.searchUsername(username) 
	try:
		return instaApi.LastJson["user"]["pk"]
	except Exception:
		print("username doesn't exist") 
		return False



	



def read_json(path):
    with open(path+'.json') as f:
        data = json.load(f)
    return data
def like_process(likes):
    global boi 
    boi = 0
    new_likes = []
    for like in likes:
        boi += like
        model = boi/len(likes)
        if like >= model:
            like = 1
            new_likes.append(like)
        else:
            like = 0
            new_likes.append(like)
    return new_likes



def Model():

	X = pickle.load(open('x.pickle', 'rb'))
	y = pickle.load(open('y.pickle', 'rb'))


	X =X/255.0

	conv_layers = [2]
	dense_layers = [1]
	layer_sizes = [128]

	for dense_layer in dense_layers:
	    for layer_size in layer_sizes:
	        for conv_layer in conv_layers:
	        	model = tf.keras.models.Sequential()
	        	model.add(tf.keras.layers.Conv2D(layer_size, (3,3), input_shape= X.shape[1:]))
	        	model.add(tf.keras.layers.Activation('relu'))
	        	model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
	        	for l in range(conv_layer-1):
	        		model.add(tf.keras.layers.Conv2D(layer_size, (3,3), input_shape= X.shape[1:]))
	        		model.add(tf.keras.layers.Activation('relu'))
	        		model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))

	        	model.add(tf.keras.layers.Flatten())
	        	for _ in range(dense_layer):
	        		model.add(tf.keras.layers.Dense(layer_size))
	        		model.add(tf.keras.layers.Activation('relu'))
	        		model.add(tf.keras.layers.Dropout(0.2))
	        	model.add(tf.keras.layers.Dense(1))
	        	model.add(tf.keras.layers.Activation('sigmoid'))
	        	model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
	        	model.fit(X,y,epochs=10,validation_split=0.1)
	model.save('PP.model')






def process(image):
    image = image.resize((80,80))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image.reshape(-1,80,80,1)
def test():
	model = tf.keras.models.load_model('PP.model')
	return model



def training(username,DATADIR):
    json_path = f'{username}'
    json_file = os.path.join(DATADIR,json_path)
    json = read_json(json_file) # 5

    for i in json:
        likes.append(i['edge_media_preview_like']['count'])
    
    new_likes = like_process(likes) 
    
    new_likes.reverse()
    print(new_likes)
    k = 0
    while (k <= len(os.listdir(DATADIR))-1):
        try:
            print(k)
            class_img = new_likes[k]
            
            

            img_array = cv2.imread(os.path.join(DATADIR,os.listdir(DATADIR)[k]),cv2.IMREAD_GRAYSCALE)
            print(img_array)
            new_arr = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
            training_data.append([new_arr,class_img])
            
        except Exception as e:
            pass
        k += 1


def stock(training_data):
	x= []
	y= []
	import pickle

	for features,labels in training_data:
		x.append(features)
		y.append(labels)
	X = np.array(x).reshape(-1,IMG_SIZE,IMG_SIZE,1)


	pickle_boi = open('x.pickle','wb')
	pickle.dump(X,pickle_boi)
	pickle_boi = open('y.pickle','wb')
	pickle.dump(y,pickle_boi)
	pickle_boi.close()


def get_his_shit(username,me,pwd,DATADIR):
	os.system(f'instagram-scraper {username}  -m 24  -t image --media-metadata -u {me} -p {pwd}')
	training(username,DATADIR)
	stock(training_data)
	




	



	return "fu"





app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')



@app.route('/waiting')
def meanwhile():
	return render_template('meanwhile.html')



@app.route('/data', methods=['GET','POST'])
def data():

	return render_template('data.html')


@app.route('/follow',methods=['GET','POST'])
def follow():
	username = request.form['username']
	DATADIR = f'/home/amine/Desktop/PhtoEstimator/{username}'
	
	id = get_userID(username)
	instaApi.follow(id)
	print(username)

	flash('A Request has been sent to you Please Accept to proceed', 'sucess')
	return render_template('meanwhile.html', message=username)


@app.route('/download', methods=['GET','POST'])
def download():
	username=request.form['username']
	DATADIR = f'/home/amine/Desktop/PhtoEstimator/{username}'
	me = 'amine_zitoun'
	pwd = "zitoun123456"
	get_his_shit(username,me,pwd,DATADIR)
	return render_template('training.html', message=username)


@app.route('/train')
def train():
	
	Model()
	print('done ez')
	return  render_template('testing.html')



@app.route('/predict',methods=['GET','POST'])
def predict():
	
	print('bish')
	model = test()
	message = request.get_json(force=True)
	encoded = message['image']
	decoded = base64.b64decode(encoded)
	image = Image.open(io.BytesIO(decoded))
	processed_image = process(image)
	prediction = model.predict(processed_image).tolist()
			
	response = {
		'prediction': prediction[0][0]
	}
	print(jsonify(response))
	return jsonify(response)
	
	



if __name__ == '__main__':
	app.secret_key='zitoun100%'
	app.run(debug=True,threaded=False)
