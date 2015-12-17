"""
This script plots some exploratory analysis plots for the raw and filtered data:
    - Moisaic of the mean voxels values for each brain slices

Run with:
    python eda.py 
    from this directory
"""
from __future__ import print_function, division
import sys, os, pdb
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
sys.path.append(os.path.join(os.path.dirname(__file__), "./"))
from plot_mosaic import *
from mask_filtered_data import *

# Locate the paths
project_path = '../../../'
data_path = project_path+'data/ds005/' 
path_dict = {'data_filtered':{ 
			      'type' : 'filtered',
			      'feat' : '.feat/',
			      'bold_img_name' : 'filtered_func_data_mni.nii.gz',
			      'run_path' : 'model/model001/'
			     },
             'data_original':{
		       	      'type' : '',
			      'feat': '',
                              'bold_img_name' : 'bold.nii.gz',
                              'run_path' : 'BOLD/'
			     }}
			
#subject_list = [str(i) for i in range(1,17)]
#run_list = [str(i) for i in range(1,4)]

# Run only for subject 1 and 5 - run 1
run_list = [str(i) for i in range(1,2)]
subject_list = ['1']

# set gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

# Create the needed directories if they do not exist
dirs = [project_path+'fig/',\
        project_path+'fig/BOLD']
for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)

# Template to plot the unmasked filetered data
template_path = project_path+'data/mni_icbm152_t1_tal_nlin_asym_09c_2mm.nii'

# Progress bar
l = len(subject_list)*len(run_list)
sys.stdout.write("Starting EDA analysis\n")
sys.stdout.write("EDA: ")
sys.stdout.flush()

# Loop through the data type - raw or filtered
for dat in path_dict:
    d_path = path_dict[dat]
    # Set the data name and paths
    images_paths = [('ds005' + '_sub' + s.zfill(3) + '_t1r' + r, \
                     data_path + 'sub%s/'%(s.zfill(3)) + d_path['run_path'] \
                     + 'task001_run%s%s/%s' %(r.zfill(3),d_path['feat'],\
    		     d_path['bold_img_name'])) \
                     for r in run_list \
                     for s in subject_list]
    for image_path in images_paths:
        name = image_path[0]
	data_int = nib.load(image_path[1]).get_data()
	data = data_int.astype(float)
        mean_data = np.mean(data, axis=-1)
        # Plot
        if d_path['type']=='filtered':
            Transpose=False
	    template_data = nib.load(template_path).get_data()
	    plt.imshow(\
	        plot_mosaic(template_data, transpose=Transpose), \
	        cmap='gray', alpha=1)
	else:
	    in_brain_mask = mean_data > 375
            Transpose=True
            plt.contour(\
	        plot_mosaic(in_brain_mask, transpose=Transpose), \
		            cmap='gray' , alpha=1)
        plt.imshow(\
	plot_mosaic(mean_data, transpose=Transpose), cmap='gray', alpha=1)
        plt.colorbar()
        plt.title('Voxels mean values' + '\n' +  (d_path['type'] + str(name)))
        plt.savefig(project_path+'fig/BOLD/%s_mean_voxels.png'\
                    %(d_path['type'] + str(name)))
        #plt.show()
        plt.clf()
	plt.close()
        sys.stdout.write("\n\b=")
        sys.stdout.flush()

sys.stdout.write("======================================\n")
sys.stdout.write("EDA analysis done\n")
sys.stdout.write("Mosaic plots in project_epsilon/fig/BOLD/ \n")
sys.stdout.write("Histogram plots in project_epsilon/fig/histograms/ \n\n")
