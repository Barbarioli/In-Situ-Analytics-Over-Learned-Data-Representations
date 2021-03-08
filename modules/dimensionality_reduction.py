## dimensionality reduction

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def reduction(numpy_array, type = 'PCA', size = 2):

	"""
	Encodes the categorical columns into numbers
	
	Arguments:
	dataframe(pandas dataframe): multivariate time series data frame to be encoded
	
	Returns:
	encoded categorical dataframe
	"""

	num_components = size

	if type == 'PCA':
		pca = PCA(num_components)
		X_pca = pca.fit_transform(numpy_array)
		print('Explained variance: ' + str(pca.explained_variance_ratio_))

	return X_pca
	