#!/usr/bin/env python3

"""

File for storing the model class of the AI

Author	: @some1and2
Date	: 3/29/2023

"""

from os import path
from .. import Datasets

## Sets up Logger ##
logger = logging.getLogger("main")

## Setting Package Variables ##
ModeDestination	= __path__[0] # Sets the destination of the data

class Model:
	def __init__(self):
		"""
		Function for initializing the model
		"""


		self.title = FindTitle() # Sets the title of the model to be a random

	def Train(self):
		"""
		Function for training the model
		"""

	def Eval(self):
		"""
		Function for evaluating the output of the model
		"""

	def Save(self, FileName):
		"""
		Function for saving the settings of the model
		"""

def FindTitle(OutLength: int = 4) -> str:
	"""
	Function for finding a new title for a model
	the purpose of this function is to avoid duplicate names of models (even if this is unlikely)
	Outlength is the expected length of the title
	"""

	from glob import glob

	DirectoryValues = glob(path.join( ModelDestination, "*" )) # Gets all the file in the directory
	DirectoryValues = [ file.split(path.sep)[-1] for file in DirectoryValues ] # Removes the absolute path so that only the filename is left
	title = None

	def GetRandomChars(OutLength: int = 4) -> str:
		"""
		Function for getting a list of random Characters
		"""

		from random import randint
		
		GetCharacter = lambda : chr(randint(ord("A"), ord("Z")))
		return "".join( GetCharacter() for i in range(OutLength) ) # Gets a string of random characters between A and Z


	def IsInDirectory() -> bool:
		"""
		Function for seeing if a title is in a directory
		Inherits [title, DirectoryValues]
		"""

		for file in DirectoryValues:
			if file.startswith(title):
				# If the file is found, return false
				return False
		else:
			return True # If the title is okay, return true

	while IsInDirectory():
		title = GetRandomChars(OutLength)

	return title
