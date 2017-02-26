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
# TODO: Number of training examples(done)
import pandas
n_train = train['features'].shape[0]
# TODO: Number of testing examples.(done)
n_test = test['features'].shape[0]
# TODO: What's the shape of an traffic sign image?(done)
image_shape = []
image_shape.append(train['sizes'][0][0])
image_shape.append(train['sizes'][0][1])
# TODO: How many unique classes/labels there are in the dataset.(done)
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
#TODO: Uncoment here for submission
# for i in range(6):
#     index = random.randint(0,n_train)
#     rnd_img.append(X_train[index])
#     plt.subplot(3,2,i+1)
#     plt.title(str((train['labels'][index])),style='italic',
#         bbox={'facecolor':'red', 'alpha':0.5, 'pad':1})
#     plt.imshow(rnd_img[i])
# plt.show()

#Step 2: Design and Test a Model Architecture
### Preprocess the data here. Preprocessing steps could include normalization, converting to grayscale, etc.
### Feel free to use as many code cells as needed.
import cv2
X_train_nrm=[]
for i in range(n_train):
    #make grayscale image
    X_train_nrm.append((cv2.cvtColor(X_train[i],cv2.COLOR_BGR2GRAY)))
    #normilize data
    cv2.normalize(X_train_nrm[i],X_train_nrm[i],0,10,cv2.NORM_MINMAX)


#TODO: Uncomment if you need to see the normilization pictures
# for i in range(6):
#     index = random.randint(0,n_train)
#     rnd_img.append(X_train_nrm[index])
#     plt.subplot(3,2,i+1)
#     plt.title(str((train['labels'][index])),style='italic',
#         bbox={'facecolor':'red', 'alpha':0.5, 'pad':1})
#     plt.imshow(rnd_img[i],cmap='gray')
# plt.show()




