import math
import random

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

WIDTH = 400
HEIGHT = 400
RADIUS = WIDTH
dist = []
l = 10000000

def calcPI():
	inCircle = 0
	total    = 0
	for i in range(l):
		total += 1
		x = random.randint(-WIDTH , WIDTH )
		y = random.randint(-HEIGHT, HEIGHT)
		if x * x + y * y <= RADIUS*RADIUS:
			inCircle += 1
		pi = 4*(inCircle/total)
		d = abs(math.pi-pi)
		dist.append(d)
		if i % (l/10) == 0:
			print(i)
	#Return last value of PI to create the name of the pdf
	return pi 
		

def plot(pi):
	# Start plotting a 1000 to better visualiaze the data
	plt.plot(dist[1000:])
	plt.ylabel('Accuracy')
	# Saving to PDF using the last value of PI 
	pp = PdfPages('{}.pdf'.format(pi))
	plt.savefig(pp, format='pdf')
	pp.close()




def main():
	pi = calcPI()
	plot(pi)

if __name__ == '__main__':
	main()
