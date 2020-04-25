
import tqdm # To get a progress bar.
import os
from ImageProcessing.TemplateMatching.Templates.templates import Templates


import scipy
if scipy.__version__ > "1.2.1":
    from imageio import imsave
else:
    from scipy.misc import imsave

def saveAllTemplateImages():

    for ind, x in tqdm.tqdm(enumerate(Templates)):
    	if not os.path.exists(f"./im_template_{x}.png"):
	        imsave(f"./im_template_{x}.png", x.value[0])

    # Template images saved to the template directory.

def getImageDirectory():
    return os.path.split(os.path.relpath(__file__))[0]


# Save all the image files in the appropriate directory.
imageSaveDir = getImageDirectory()
currDir = os.getcwd()
os.chdir(imageSaveDir)
saveAllTemplateImages()
os.chdir(currDir)