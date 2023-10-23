 from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
redcount = 0
greencount = 0

def base2_light(s):
    pass
    for i in s:
        if i == '1':
            green.toggle()
            time.sleep(0.5)
            green.toggle()
            time.sleep(1)
            redcount += 1
        else:
            red.toggle()
            time.sleep(0.5)
            red.toggle()
            time.sleep(1)
            greencount += 1
    redcountans = int(input"How many times did the red light flash?")
    if redcountans == redcount:
<<<<<<< Updated upstream
        print("You're correct!")
    else:
        print("You're wrong!")
    greencountans = int(input"How many times did the green light flash?")
    if greencountans == greencount:
        print("You're correct!")
    else:
        print("You're wrong!")
=======
        green.toggle()
        time.sleep(0.5)
        green.toggle()
        time.sleep(1)
        green.toggle()
        time.sleep(0.5)
        green.toggle()
        time.sleep(1)
    else:
        red.toggle()
        time.sleep(0.5)
        red.toggle()
        time.sleep(1)
        red.toggle()
        time.sleep(0.5)
        red.toggle()
        time.sleep(1)
    greencountans = int(input"How many times did the green light flash?")
    if greencountans == greencount:
        green.toggle()
        time.sleep(0.5)
        green.toggle()
        time.sleep(1)
        green.toggle()
        time.sleep(0.5)
        green.toggle()
        time.sleep(1)
    else:
        red.toggle()
        time.sleep(0.5)
        red.toggle()
        time.sleep(1)
        red.toggle()
        time.sleep(0.5)
        red.toggle()
        time.sleep(1)
    return None
>>>>>>> Stashed changes

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