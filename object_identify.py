from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
import sys
import time
import cv2
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os 
from PyQt5 import QtCore

class _identify():
    def __init__(self):
        self.file_name = "rgb.jpg"
        self.model_file = "tf_files/retrained_graph.pb"
        self.label_file = "tf_files/retrained_labels.txt"
        self.input_height = 224
        self.input_width = 224
        self.input_mean = 128
        self.input_std = 128
        self.input_layer = "input"
        self.output_layer = "final_result"
        self.result = ""
        parser = argparse.ArgumentParser()
        parser.add_argument("--image", help="image to be processed")
        parser.add_argument("--graph", help="graph/model to be executed")
        parser.add_argument("--labels", help="name of file containing labels")
        parser.add_argument("--input_height", type=int, help="input height")
        parser.add_argument("--input_width", type=int, help="input width")
        parser.add_argument("--input_mean", type=int, help="input mean")
        parser.add_argument("--input_std", type=int, help="input std")
        parser.add_argument("--input_layer", help="name of input layer")
        parser.add_argument("--output_layer", help="name of output layer")
        self.args = parser.parse_args()

        if  self.args.graph:
           self.model_file =  self.args.graph
        if  self.args.labels:
           self.label_file =  self.args.labels
        if  self.args.input_height:
           self.input_height = self.args.input_height
        if  self.args.input_width:
           self.input_width = self.args.input_width
        if  self.args.input_mean:
            self.input_mean =  self.args.input_mean
        if  self.args.input_std:
           self.input_std =  self.args.input_std
        if  self.args.input_layer:
           self.input_layer =  self.args.input_layer
        if self. args.output_layer:
           self.output_layer =  self.args.output_layer
        self.graph = self.load_graph(self.model_file)       
         

    def load_graph(self,model_file):
        graph = tf.Graph()
        graph_def = tf.GraphDef()

        with open(model_file,"rb") as f:
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            tf.import_graph_def(graph_def)
        return graph
    
    def read_tensor_from_image_file(self,file_name, input_height=299, input_width=299,
				input_mean=0, input_std=255):
        input_name = "file_reader"
        output_name = "normalized"
        file_reader = tf.read_file(file_name, input_name)
        if file_name.endswith(".png"):
            image_reader = tf.image.decode_png(file_reader, channels = 3,
                                            name='png_reader')
        elif file_name.endswith(".gif"):
            image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                        name='gif_reader'))
        elif file_name.endswith(".bmp"):
            image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
        else:
            image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                                name='jpeg_reader')
        float_caster = tf.cast(image_reader, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0);
        resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
        normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
        sess = tf.Session()
        result = sess.run(normalized)
        return result
    def load_labels(self,label_file):
        label = []
        proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
        for l in proto_as_ascii_lines:
            label.append(l.rstrip())
        return label
    
    def run(self):
        self.cap = cv2.VideoCapture(0)
        time.sleep(2)
        ret,frame = self.cap .read()
        #frame=cv2.resize(frame,(900,600))
        cv2.imwrite('rgb.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY, 90])
        self.cap .release()        
        cv2.destroyAllWindows()
        if  self.args.image:
           self.file_name =  self.args.image
       
        t =self. read_tensor_from_image_file(self.file_name,
                                        input_height=self.input_height,
                                        input_width=self.input_width,
                                        input_mean=self.input_mean,
                                        input_std=self.input_std)
        input_name = "import/" + self.input_layer
        output_name = "import/" +self. output_layer
        input_operation =  self.graph.get_operation_by_name(input_name)
        output_operation =  self.graph.get_operation_by_name(output_name)
        with tf.Session(graph =  self.graph) as sess:
            results = sess.run(output_operation.outputs[0],
                {input_operation.outputs[0]:t})
        results = np.squeeze(results)       
        top_k = results.argsort()[-5:][::-1]
        labels =self. load_labels(self.label_file)
        title = ''
        template = "{}(score={:0.5f})"
        for i in top_k:
            print(template.format(labels[i],results[i]))
            title += template.format(labels[i],results[i]) + '\n'
        fl = title[0]
        if fl=='c':
            title='Clear'
            self.result = "清澈"
        if fl=='s':
            title='SmallTurbid'
            self.result = "微混濁"
        if fl=='b':
            title='Turbid'
            self.result = "混濁"

        #title += 'Test image: '+file_name
        # plt.title(title,fontsize=30)
        # img = mpimg.imread( self.file_name)
        # imgplot = plt.imshow(img)
        # plt.show()

    def getResult(self):
        return self.result