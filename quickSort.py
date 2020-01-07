import random
import time

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def pivotFirst(x, left, right):
    