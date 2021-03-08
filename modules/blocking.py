#blocking

import pandas as pd
import numpy as np

def blocking(numpy_data, block_size = 128, compressed = 'no'):

	"""
	Merge two dataframes
	
	Arguments:
	dataframe(pandas dataframe): multivariate time series data frame to be encoded
	
	Returns:
	encoded categorical dataframe
	"""
	blocks = []
	#blocks = np.array(l)
	size = len(numpy_data)
	for i in range(0,size, block_size):
		if i == 0:
			continue
		else:
			block = numpy_data[i-block_size:i]
			blocks.append(numpy_data)

	return blocks




