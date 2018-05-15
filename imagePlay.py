from PIL import Image
import numpy as np
fname="C:/Users/simra/Pictures/123.png"
img=np.asarray(Image.open(fname), dtype=np.float32)
for i in img:
	for j in i:
		j[3]=150
		if(np.max(j[0:3])<170):
			j[0:3]=0
		else:
			j[0:3]=255
print(img)
def save_as_img(ar, fname):
    Image.fromarray(ar.round().astype(np.uint8)).save(fname)

save_as_img(img,"edited123.png")    				