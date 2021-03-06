import tensorflow as tf
import numpy as np
import sys

def dropconnect_wrapper(w, keep_prob = 1.0):
    '''
        input : 
                w : any tensor
                keep_prob : float default to be 1.0 
        
        selector : same shape of w, to be 1 with probability with keep_prob otherwise 0

        return :
            keep the value of w with probability keep_prob    
    '''

    selector = tf.sign(keep_prob - tf.random_uniform(get_size(w)
                                                    , minval = 0
                                                    , maxval=1
                                                    , dtype = tf.float32))

    selector = (selector + 1)/2

    return selector*w

def get_size(w):
    return w.get_shape().as_list()

def sample(prob):
    '''
        input :
            prob 2D tensor
        return:
            sample 1 accroding to the probability 
    '''
    return (tf.sign(prob - tf.random_uniform(prob.get_shape(),minval = 0, maxval=1, dtype = tf.float32)) + 1)/2



def print_variables(keys):
    i = 0
    print(keys)
    while True:
        try:
            print(tf.get_collection(keys)[i])
            i+=1
        except IndexError:
            break;
