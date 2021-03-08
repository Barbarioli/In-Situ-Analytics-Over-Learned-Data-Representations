## Separation module

## Insert pandas dataframe
import pandas as pd
import numpy as np

def separator(dataframe, multiple_timestamps = True):

	"""
	Separates the dataframe into categorical and continous dataframes
	
	Arguments:
	dataframe(pandas dataframe): multivariate time series data frame to be compressed/reduced
	multiple_timestamps(Boolean): True if each separate unit will contain the timestamps 
	
	Returns:
	Two differente dataframes, one with continuous time series and the second with categorical
	"""

	#Separating types
	continous = dataframe.select_dtypes(include='number')
	categorical = dataframe.select_dtypes(include='object')
	timestamps = dataframe['date_time']
	categorical.drop(['date_time'], axis = 1)

	#creating numpy arrays
	np_continous = continous.to_numpy()
	np_categorical = categorical.to_numpy()
	np_timestamps = timestamps.to_numpy()

	return np_continous, np_categorical, np_timestamps




