#Step 0: Load The Data
# Load pickled data
import pickle
# TODO: Fill this in based on where you saved the training and testing data
training_file = './Resources/traffic-signs-data/test.p'
validation_file ='./Resources/traffic-signs-data/train.p'
testing_file = './Resources/traffic-signs-data/valid.p'
with open(training_file, mode='rb') as f:
    train = pickle.load(f)
with open(validation_file, mode='rb') as f:
    valid = pickle.load(f)
with open(testing_file, mode='rb') as f:
    test = pickle.load(f)
X_train, y_train = train['features'], train['labels']
X_valid, y_valid = valid['features'], valid['labels']
X_test, y_test = test['features'], test['labels']

#Step 1: Dataset Summary & Exploration
### Replace each question mark with the appropriate value.
### Use python, pandas or numpy methods rather than hard coding the results
# TODO: Number of training examples
import pandas
n_train = train['features'].shape[0]
# TODO: Number of testing examples.
n_test = test['features'].shape[0]
# TODO: What's the shape of an traffic sign image?
image_shape = []
image_shape.append(train['sizes'][0][0])
image_shape.append(train['sizes'][0][1])
# TODO: How many unique classes/labels there are in the dataset.
n_classes = len(set(train['labels']))
print("Number of training examples =", n_train)
print("Number of testing examples =", n_test)
print("Image data shape =", image_shape)
print("Number of classes =", n_classes)

#Include an exploratory visualization of the dataset
### Data exploration visualization code goes here.
### Feel free to use as many code cells as needed.
import matplotlib.pyplot as plt
# Visualizations will be shown in the notebook.
#%matplotlib inline
import random
rnd_img = []
for i in range(6):
    index = random.randint(0,n_train)
    rnd_img.append(X_train[index])
    plt.subplot(3,2,i+1)
    plt.title(str((train['labels'][index])),style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':1})
    plt.imshow(rnd_img[i])

plt.show()



