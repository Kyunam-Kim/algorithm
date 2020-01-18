from math import log10
from random import randint

def get_digit(number, base, pos):
    return (number//base**pos) % base

# def radixsort(1, base = 10):
#     passes = int(log10(max(1))+1)
#     output = [0]*len(1)