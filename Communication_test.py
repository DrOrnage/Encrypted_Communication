from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
yellow = Pin(13, Pin.OUT)

def wrong_input():
    yellow.toggle()
    time.sleep(0.3)
    yellow.toggle()
    time.sleep(0.3)
    yellow.toggle()
    time.sleep(0.3)
    yellow.toggle()
    time.sleep(1)
    return None

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

base2_light("01010010")
end()
base2_light("00110110")
wrong_input()