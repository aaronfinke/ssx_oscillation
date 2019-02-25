#!/usr/bin/python

class DataWell:

	def __init__(self,path,firstframe,numframes):
		self.path = path
		self.firstframe = frames
		self.lastframe = frames + numframes - 1

		self.isIndexed = False


	def framesIndexed(self):
		self.isIndexed = True
