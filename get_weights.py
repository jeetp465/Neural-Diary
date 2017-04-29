#!/usr/bin/env python

import caffe
import cv2
import numpy
import sys

class Weights:
	def read_image( self, path ):
		img_file = cv2.imread(path)
		img_file.resize(3, 224, 224)
		img_file.resize(1, 3, 224, 224)
		return img_file

	def __init__(self):
		global net
		caffe.set_mode_gpu()
		caffe.set_device(0)
		self.net = caffe.Net('/data/gpuuser2/caffe/models/vgg_16/VGG_ILSVRC_16_layers_deploy.prototxt', '/data/gpuuser2/caffe/models/vgg_16/VGG_ILSVRC_16_layers.caffemodel', caffe.TEST)

	def comp_image( self, path1, path2 ):
		data1 = self.net.forward_all(data=self.read_image(path1))
		data2 = self.net.forward_all(data=self.read_image(path2))
		a = numpy.ndarray.flatten(data1['fc8'])
		b = numpy.ndarray.flatten(data2['fc8'])
		n = numpy.linalg.norm(a-b, 5)
		return n
