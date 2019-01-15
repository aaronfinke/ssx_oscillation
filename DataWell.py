#!/usr/bin/python

class DataWell:

	def __init__(self,path,frames):
		self.path = path
		self.frames = frames
		self.isIndexed = False


	def framesIndexed(self):
		self.isIndexed = True


