"""
Simple linear regression example in TensorFlow
This program tries to predict the number of thefts from
the number of fire in the city of Chicago
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = '/home/arrayslayer/tf-stanford-tutorials/data/fire_theft.xls'

# Phase 1: Assemble the graph
# Step 1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override='utf-8')
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)],dtype=np.float32)
n_samples = sheet.nrows - 1
# Step 2: create placeholders for input X (number of fire) and label Y (number of theft)

X = tf.placeholder(tf.float32,shape=None,name="Input_X")
Y = tf.placeholder(tf.float32,shape=None,name="Input_Y")

# Step 3: create weight and bias, initialized to 0
# name your variables w and b

w = tf.Variable(0.0, name = "Weight")
b = tf.Variable(0.0, name = "Bias")

# Step 4: predict Y (number of theft) from the number of fire
# name your variable Y_predicted
Y_predicted = tf.Variable(0,name="Y_predicted")
Y_predicted = X*w +b
# Step 5: use the square error as the loss function

loss = tf.square(tf.subtract(Y,Y_predicted),name="loss")

# name your variable loss

# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.AdamOptimizer(learning_rate=0.025).minimize(loss)

# Phase 2: Train our model
with tf.Session() as sess:
	# Step 7: initialize the necessary variables, in this case, w and b
	# TO - DO
    #init = tf.global_variables_initializer()
    #sess.run(init)
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./my_graph/linear',sess.graph)
	# Step 8: train the model
    for i in range(500):
        total_loss = 0
        for x,y in data:
			# Session runs optimizer to minimize loss and fetch the value of loss
			# TO DO: write sess.run()
            _,l,Y_pred=sess.run([optimizer,loss,Y_predicted],feed_dict={X:x,Y:y})
            total_loss+=l
        print("Epoch {0}:{1}".format(i,(total_loss/n_samples)))
    writer.close()


# plot the results
#X, Y = data.T[0], data.T[1]
#plt.plot(X, Y, 'bo', label='Real data')
#plt.plot(X, X * w + b, 'r', label='Predicted data')
#plt.legend()
#plt.show()
