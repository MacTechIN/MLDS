import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

import tensorflow as tf


dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')

print(dftrain.head())

y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

