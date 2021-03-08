## dimensionality reduction

import pandas as pd
import numpy as np

def merge(continous, categorical, timestamp):

	"""
	Merge two dataframes
	
	Arguments:
	dataframe(pandas dataframe): multivariate time series data frame to be encoded
	
	Returns:
	encoded categorical dataframe
	"""
	result = np.concatenate((continous, categorical), axis = 1)
	return result