from math import log10
from random import randint

def get_digit(number, base, pos):
    return (number//base**pos) % base