import numpy as np 
import argparse

def label_to_onehot(label):
    one_hot_labels = np.zeros([label.shape[0], int(np.max(label)+1)])
    one_hot_labels[np.arange(label.shape[0]), label.astype(int)] = 1
    return one_hot_labels

def onehot_to_label(onehot):
    return np.argmax(onehot, axis=1)

def normalize_fn(data, means, stds):
    """This function takes the data, the means,
    and the standard deviatons(precomputed). It 
    returns the normalized data.
    
    Inputs:
        data : shape (NxD)
        means: shape (1XD)
        stds : shape (1xD)
        
    Outputs:
        data_normed: shape (NxD)
    """
    data_normed = np.arange(data.shape[0]*data.shape[1]).reshape(data.shape)
    for i in range(data.shape[1]):
        data_normed[:,i] = (data[:,i] - means[0,i])/stds[0,i]
    
    return data_normed

