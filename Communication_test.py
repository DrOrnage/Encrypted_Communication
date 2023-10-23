import math
from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)

def base2_light(s):
    pass
def string_to_binary(x):
  l = [(ord(i)) for i in x]
  m = [(int(bin(i)[2:])) for i in l]
  return m