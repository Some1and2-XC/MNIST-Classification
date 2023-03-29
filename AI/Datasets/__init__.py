#!/usr/bin/env python3

"""

Section for code that has to do with the datasets of the algorithm

Author	: @some1and2
Date	: 3/29/2023

"""

from os import path
import logging

import numpy as np

logger = logging.getLogger("main")

## Setting Package Variables ##
DataSource		= "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz" # URL to where the dataset can be downloaded from
DataDestination	= __path__[0] # Sets the destination of the data
DataFilename	= path.join( DataDestination, "mnist.npz" ) # Sets the path of the outfile to join the Destination folder and filename
DataHash = "731C5AC602752760C8E48FBFFCF8C3B850D9DC2A2AEDCF2CC48468FC17B673D1" # Expected Hash Value for the Dataset

## Setting Package Variables for Filenames ##
ExpectedValues = [ "x_test.npy", "y_test.npy", "x_train.npy", "y_train.npy" ] # Values expected to exist in the "Datasets/" subdirectory

# Sets up a dictionary to return the strings of the desired dataset
ReturnValues = {
	"test"	: [ "x_test.npy", "y_test.npy" ],
	"train"	: [ "x_train.npy", "y_train.npy" ],
}

## Defining Package functions ##
def DataINIT() -> bool:
	"""
	Function for Initializing the Datasets
	Should return numpy arrays of all the data that would be required
		"""

	## Local Function Setting ##
	def DownloadData() -> bool:
		"""
		function for downloading the data
		Returns true if downloading happened successfully
		"""

		from requests import get as curl
		from hashlib import sha256
		from zipfile import ZipFile as unzip
		import io

		# Gets the content of the file as bytes ( generally downloadable so just using a get request should return the bytes of the file )
		DataFile = curl(DataSource).content

		if sha256(DataFile).hexdigest().upper() == DataHash: # Compares the file it downloaded to the expected hash ( set in package variables )

			# Unzips the datafile and writes to the directory
			unzip(
				io.BytesIO(DataFile) # Uses BytesIO to avoid writing the compressed ".npz" file to disk
			).extractall(DataDestination)

			logger.info("Data Written To Files ( DownloadData() )", extra = {"FuncName": DownloadData.__name__})

			return True
		else:
			# Raises Error if the downloaded files hash doesn't match the expected hash
			raise ValueError("Incorrect HASH Value from Source")
			return False

	def VerifyData() -> bool:
		"""
		Function for verifying if all the files that are expected got downloaded
		"""

		from glob import glob

		DirectoryValues = glob(path.join(DataDestination, "*")) # Variable for a list of the files in the destination directory
		DirectoryValues = [ PathToValue.split(path.sep)[-1] for PathToValue in DirectoryValues ] # Only looks for the filename of each file instead of the full path

		for Filename in ExpectedValues:
			# Goes through each value in 'ExpectedValues' defined in DataINIT() to verify if it is in the directory
			# If the file isn't found then returns false
			if Filename not in DirectoryValues:
				return False
		else:
			return True # If all the files are found return true

	if not VerifyData(): # If all the files are not found
		DownloadData() # Download the data

	return True

def DataImport(mode: str = "test") -> tuple:
	"""
	Function for returning the data from file
	Returns numpy array of the data
	"""

	## Imports the files ##
	files = ReturnValues[mode] # Sets "files" to be the file names of the datasets to be imported

	GetFileNames = lambda x: path.join( DataDestination, x ) # Setsup a lambda function for getting the file path for the datasets

	logger.debug("Started Importing Data", extra={"FuncName": DataImport.__name__})

	x = np.load(GetFileNames(files[0])) # Imports the "x" data
	y = np.load(GetFileNames(files[1])) # Imports the "y" data

	del GetFileNames

	## Reshapes "x" ##
	logger.debug("Changing Shape of the x", extra={"FuncName": DataImport.__name__})
	x_shape = x.shape
	x.reshape(x_shape[0], x_shape[1] * x_shape[2]) # Keeps the original length of the array but changes the images to be a single column

	return x, y