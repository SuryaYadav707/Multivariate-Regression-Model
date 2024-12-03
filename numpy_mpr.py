#!/usr/bin/env python
# coding: utf-8

# In[2]:


# numpy_mpr.py

class CustomNumpy:
    @staticmethod
    def dot(X, theta):
        # Custom implementation of dot product
        if len(X.shape) == 1:
            return sum(X * theta)
        else:
            return [sum(row * theta) for row in X]

    @staticmethod
    def sum(X):
        # Custom implementation of sum
        total = 0
        for element in X:
            total += element
        return total

    @staticmethod
    def mean(X, axis=None):
        # Custom implementation of mean
        if axis is None:
            return CustomNumpy.sum(X) / len(X)
        elif axis == 0:
            return [CustomNumpy.mean(col) for col in zip(*X)]
        elif axis == 1:
            return [CustomNumpy.mean(row) for row in X]

    @staticmethod
    def zeros(shape, dtype=None):
        # Custom implementation of zeros
        if dtype is None:
            return [0] * shape[0]
        else:
            return [dtype(0)] * shape[0]

    @staticmethod
    def sqrt(X):
        # Custom implementation of square root
        return [x ** 0.5 for x in X]


# In[ ]:




