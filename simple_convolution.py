from PIL import Image
import numpy as np

im = np.asarray(Image.open("example.jpg").convert("L"))

kernel = np.array([[-1, 0, 1],
				   [-2, 0, 2],
				   [-1, 0, 1]])

def convolve(img, kernel):
	output = [0] * (len(img)-1)
	for i in range(len(img)-1):
		output[i] = [0] * (len(img[0])-1)
		for j in range(len(img[0])-1):
			output[i][j] += img[i-1][j-1] * kernel[0][0] + img[i-1][j] * kernel[0][1] + img[i-1][j+1] * kernel[0][2] + img[i][j-1] * kernel[1][0] + img[i][j] * kernel[1][1] + img[i][j+1] * kernel[1][2] + img[i+1][j-1] * kernel[2][0] + img[i+1][j] * kernel[2][1] + img[i+1][j+1] * kernel[2][2]
	outputnp = np.array(output)
	print(outputnp)
	data = Image.fromarray(outputnp)
	data.convert("RGB").save("edges.jpg")

convolve(im, kernel)
