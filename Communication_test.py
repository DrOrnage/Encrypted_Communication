from machine import Pin
import time
import math

user = input("Enter the text: ")

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
yellow = Pin(13, Pin.OUT)

<<<<<<< Updated upstream
def wrong_input():
=======
def wronginput():
>>>>>>> Stashed changes
    yellow.toggle()
    time.sleep(0.3)
    yellow.toggle()
    time.sleep(0.3)
    yellow.toggle()
    time.sleep(0.3)
    yellow.toggle()
    time.sleep(1)
    return None
<<<<<<< Updated upstream
=======

def string_to_binary(x):
  #Uses ord function which converts individual string into a value through ASCII table
  l = [(ord(i)) for i in x]
  #the bin function converts each value in l to binary. It is slicing from 2 onwards because the function returns a prefix "0b" indicating that it is a binary value
  m = [bin(i)[2:] for i in l]
  m = [str(item) for item in m]
  return m

lst = string_to_binary(user)
>>>>>>> Stashed changes

def base2_light(s):
    for i in s:
        if i == '1':
            green.toggle()
            time.sleep(0.5)
            green.toggle()
            time.sleep(1)
        else:
            red.toggle()
            time.sleep(0.5)
            red.toggle()
            time.sleep(1)
    return None

def end():
    green.toggle()
    red.toggle()
    time.sleep(0.3)
    green.toggle()
    red.toggle()
    time.sleep(0.3)
    green.toggle()
    red.toggle()
    time.sleep(0.3)
    green.toggle()
    red.toggle()
    time.sleep(1)

<<<<<<< Updated upstream
base2_light("01010010")
end()
base2_light("00110110")
wrong_input()
=======
for i in lst:
    base2_light(i)
    end()
>>>>>>> Stashed changes
