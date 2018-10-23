import tensorflow as tf
import numpy as np
import facenet
import os
import sys
import math
import pickle
from scipy import misc
import matplotlib.pyplot as plt

with tf.Graph().as_default():
    with tf.Session() as sess:

        # load facenet model into graph 
        images = []        

        for file in os.listdir("./data"):
            if file.endswith(".jpg"):
                images.append(os.path.join("./data",file))

        images_tmp = facenet.load_data(images,False,False,160)

        print(images_tmp.shape)
        plt.imshow(images_tmp[0])
        facenet.load_model('./models/')

        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")

        feed_dict = {images_placeholder:images_tmp, phase_train_placeholder:False} 

        embedding_size = embeddings.get_shape()[1]

        emb_array = np.zeros((1,embedding_size))
        
        emb_array = sess.run(embeddings,feed_dict=feed_dict)

        print(emb_array)
