import pandas as pd
import numpy as np
import pylab as pl
import PIL
from PIL import Image
import os
import base64
from StringIO import StringIO
from sklearn.decomposition import RandomizedPCA
from sklearn.neighbors import KNeighborsClassifier

#setup a standard image size; this will distort some images but will get everything into the same shape
STANDARD_SIZE = (800, 1000)
def img_to_matrix(filename, verbose=False):
    """
    takes a filename and turns it into a numpy array of RGB pixels
    """
    img = Image.open(filename)
    if verbose==True:
        print "changing size from %s to %s" % (str(img.size), str(STANDARD_SIZE))
    img = img.resize(STANDARD_SIZE)
    img = np.array(img)
    #img = list(img.getdata())
    #img = map(str, img)
    #img = map(list, img)
    #img = np.array(img)
    #img = map(str,img)
    return img

def flatten_image(img):
    """
    takes in an (m, n) numpy array and flattens it 
    into an array of shape (1, m * n)
    """
    s = img.shape[0] * img.shape[1]
    img_wide = img.reshape(1, s)
    return img_wide[0]

img_dir = 'C:\\Users\\ipladmin\\Documents\\codeNIH\\pyProjects\\test\\'
images = [img_dir+ f for f in os.listdir(img_dir)]
labels = ["18" if "ASIF18" in f.split('/')[-1] else "05" for f in images]

data = []
for image in images:
    print "Processing: " + image
    img = img_to_matrix(image)
    img = flatten_image(img)
    data.append(img)

data = np.array(data)
#print data

is_train = np.random.uniform(0, 1, len(data)) <= 0.7
y = np.where(np.array(labels)=="18", 1, 0)

train_x, train_y = data[is_train], y[is_train]
test_x, test_y = data[is_train==False], y[is_train==False]

pca = RandomizedPCA(n_components=2)
X = pca.fit_transform(data)
df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1], "label":np.where(y==1, "18", "05")})
#df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1]})
colors = ["red", "yellow"]
for label, color in zip(df['label'].unique(), colors):
    mask = df['label']==label
    pl.scatter(df[mask]['x'], df[mask]['y'], c=color, label=label)
pl.legend()
pl.show()
print X