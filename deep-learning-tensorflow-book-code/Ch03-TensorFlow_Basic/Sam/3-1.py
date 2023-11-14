#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:03:21 2023

@author: sl
"""

import tensorflow as tf

# 그래프 노드를 정의하고 출력 합니다.

# 노드 선언     
node1 = tf.constant(3.0, dtype= tf.float32)
node2 = tf.constant(4.0)

#%%
print(node1.numpy(), node2.numpy()) # 노드 정보만 출력 


"""
<출력값> 
tf.Tensor(3.0, shape=(), dtype=float32) tf.Tensor(4.0, shape=(), dtype=float32)

"""
#%%

node3 = tf.add(node1, node2)
print('node3 :', node3)

print('node3.numpy() : ', node3.numpy() )
#%%
import tensorflow as tf

# 그래프 노드를 정의하고 출력합니다.
# 출력값 : <tf.Tensor: id=0, shape=(), dtype=float32, numpy=3.0>, <tf.Tensor: id=1, shape=(), dtype=float32, numpy=4.0>
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # 암시적으로 tf.float32 타입으로 선언될 것입니다.
print(node1, node2)

# 그래프를 실행합니다.
# 출력값 : [3.0, 4.0]
print(node1.numpy(), node2.numpy())

# 두개의 노드의 값을 더하는 연산을 수행하는 node3을 정의합니다.
# 출력값:
# node3: <tf.Tensor: id=2, shape=(), dtype=float32, numpy=7.0>
# node3.numpy(): 7.0
node3 = tf.add(node1, node2)
print("node3:", node3)
print("node3.numpy():", node3.numpy())



#%%
# Placeholder 

import tensorflow as tf
import numpy as np

# 2개의 값을 더하는 function을 정의합니다.
@tf.function
def add_two_values(x, y):
  return x + y
#%%
# 세션을 열고 그래프를 실행합니다.
# 출력값 :
# 7.5
# [ 3.  7.]
print(add_two_values(3, 4.5).numpy())
#%%

print(add_two_values(np.array([1, 3]), np.array([2, 4])).numpy())

#%%

# 노드를 추가해서 더 복잡한 그래프 형태를 만들어봅시다.
@tf.function
def add_two_values_and_multiply_three(x, y):
  return 3 * add_two_values(x, y)

#%%

# 출력값 : 22.5
print(add_two_values_and_multiply_three(3, 4.5).numpy())


#%%

a = tf.Variable(tf.float32)

b = tf.Variable(tf.float32)




