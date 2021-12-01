# import numpy as np
from numpy import *


# PEP8

def fill_matrix(i, j):
    return i + j


row = [i for i in range(10)]

L = [row for i in range(10)]

# print(L)

array = array(L, dtype=float16)
'''
print(type(array))
print(array)
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)
print(array.itemsize)
'''
shape = (3, 3)
print(ones(shape))
print(zeros(shape))
print(empty(shape))
print(eye(10))

arange_nums = arange(5, 35, 10)
print(type(arange_nums))
print(arange_nums)

linspace_nums = linspace(5, 35, 3)
print(type(linspace_nums))
print(linspace_nums)

mtrx = fromfunction(fill_matrix, (10, 10))
print(type(mtrx))
print(mtrx)

v = full(10, 0)
print(type(v))
print(v)

arange_nums_1 = arange(9)
v1 = arange_nums_1.reshape(3, 3)
print(type(v1))
print(v1)

random_matrix = random.random((3, 3))
print(type(random_matrix))
print(random_matrix)
print(random_matrix.min())
print(random_matrix.max())

rand_int_matrix = random.randint(low=0, high=100, size=(3, 4))
print(rand_int_matrix)
print(rand_int_matrix.max(initial=0))
print(rand_int_matrix.min(initial=100))
print(mean(rand_int_matrix, axis=0))  # по столбцам
print(mean(rand_int_matrix, axis=1))  # по строкам

"""
v2 = random.random(3)
mean_v2 = v2.mean()
print(v2)
print(mean_v2)
"""

M_ones = ones((5, 5))
print(M_ones)
M_ones[1:-1, 1:-1] = 0
print(M_ones)

Z = diag(arange(1, 5), k=-1)
print(Z)

import numpy as np

M = np.ones((5, 5))
M += 10
L = np.ones((5, 5))
# print(L)
# print(L + M)
R = np.random.randint(low=0, high=100, size=(3, 4))
K = np.random.randint(low=0, high=100, size=(3, 4))
print(R)
# print(K)
# print(R > K)
# print(np.cos(R))
print(np.max(R))
print(np.min(R))
# print(np.min(K))
# print(np.sum(L))
print(R.max(axis=0, initial=0))
print(R.min(axis=1, initial=100))
