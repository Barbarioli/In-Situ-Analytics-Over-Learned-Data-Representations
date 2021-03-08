## categorical encoding

import pandas as pd
import numpy as np

def cat_encoding(dataframe):

	"""
	Encodes the categorical columns into numbers
	
	Arguments:
	dataframe(pandas dataframe): multivariate time series data frame to be encoded
	
	Returns:
	encoded categorical dataframe
	"""
	dataframe = pd.DataFrame(dataframe)
	copy_df = dataframe.astype('category')
	encoded_df = pd.DataFrame() 

	columns = copy_df.columns
	for col in columns:
		new_col = 'encoded' + '_' + str(col)
		encoded_df[new_col] = copy_df[col].cat.codes

	return encoded_df


