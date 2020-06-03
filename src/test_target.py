#RUNS TEST TARGET
import sys
sys.path.append('.')

import pickle
import numpy as np

import matplotlib.pyplot as plt

import calculate_features as calc



def run_test():
	#LOAD IN TEST DATA
	img_files = ['./data/test/test_earlywar_images.data','./data/test/test_midwar_images.data',
						'./data/test/test_latewar_images.data']

	all_colors = []
	all_grays = []
	avg_edge = 0
	for i in img_files:
	    with open(i, 'rb') as filehandle:
	        # read the data as binary data stream
	        war_images = pickle.load(filehandle)
	    num_color = 0
	    num_grayscale = 0
	    
	    for img in war_images:
	        if len(img.shape)==3:
	                num_color += 1
	                avg_edge += calc.per_row_grayscale_var(img,False,True)
	        if len(img.shape) == 2:
	                num_grayscale += 1
	                avg_edge += calc.per_row_grayscale_var(img,True,True)
	    print(i)
	    #print(len(war_images))
	    #print(num_color)
	    #print(num_grayscale)
	    avg_edge /= len(war_images)
	    with open ("table_scores.txt", 'w') as fh:
	    	fh.write(i + " has avg_edge_score: " + str(avg_edge) + "\n")

	    all_colors.append(num_color)
	    all_grays.append(num_grayscale)
	    del war_images
	
	fig = plt.figure()
	ax = fig.add_subplot(111)

	x = [i-0.2 for i in range(len(all_grays))]
	col = ax.bar(range(len(all_colors)),all_colors,width=0.2, color='r')
	gray = ax.bar(x,all_grays,width=0.2, color='black')
	ax.set_title("Color vs. Grayscale")
	ax.set_ylabel("Frequencies")
	ax.set_xticklabels( ('', 'Pre-War', '', 'Mid-War','', 'Late-War') )
	ax.legend((col[0], gray[0]), ('Color', 'Grayscale'));
	plt.savefig('color_vs_grayscale.png')

	





#SAVE FIGURES
