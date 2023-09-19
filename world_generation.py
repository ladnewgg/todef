#Importations
import numpy as np
from matplotlib import image
from matplotlib import pyplot
basicmap = image.imread('noiseTexture.png')

#CONSTS
SHAPE = basicmap.shape[0]
PROP = 4
RESULT_SHAPE = int(SHAPE/PROP)



def keep_only_alpha(image):
	tmp = np.zeros((SHAPE,SHAPE))
	for i in range(SHAPE):
		for j in range(SHAPE):
			tmp[i][j] = image[i][j][0]
	return tmp


def convert_to_matrix(image):
	result = np.zeros((RESULT_SHAPE, RESULT_SHAPE))
	for i in range(0, SHAPE, PROP):
		for j in range(0, SHAPE, PROP):
			mean = 0
			for k in range(PROP):
				for l in range(PROP):
					mean += image[i+k][j+l]
			
			mean = mean/(PROP*PROP)
			mean = 0 if (mean < 0.2) else 1
			result[int(i/PROP)][int(j/PROP)] = mean
	return result




def main():
	basicmap = keep_only_alpha(basicmap)
	result = convert_to_matrix(basicmap)
	pyplot.imshow(result)
	pyplot.show()

main()