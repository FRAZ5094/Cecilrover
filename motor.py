import RPi.GPIO as gpio
from time import sleep
import keyboard

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

left_forward=16
left_backward=15
right_backward=11
right_forward=13

gpio.setup(left_forward,gpio.OUT)
gpio.setup(left_backward,gpio.OUT)
gpio.setup(right_forward,gpio.OUT)
gpio.setup(right_backward,gpio.OUT)

def forward(time):
    print(f"forward for {time} second")
    gpio.output(left_forward,True)
    gpio.output(right_forward,True)
    sleep(time)
    gpio.output(left_forward,False)
    gpio.output(right_forward,False)
    gpio.cleanup()

def backward(time):
    print(f"backward for {time} second")
    gpio.output(left_backward,True)
    gpio.output(right_backward,True)
    sleep(time)
    gpio.output(left_backward,False)
    gpio.output(right_backward,False)   

def left(time):
    print(f"left for {time} second")
    gpio.output(left_backward,True)
    gpio.output(right_forward,True)
    sleep(time)
    gpio.output(left_backward,False)
    gpio.output(right_forward,False)
    gpio.cleanup()

def right(time):
    print(f"right for {time} second")
    gpio.output(left_forward,True)
    gpio.output(right_right,True)
    time(sleep)
    gpio.output(left_forward,False)
    gpio.output(right_right,False)

try:
    while True:
        print(keyboard.read_key())
        if keyboard.is_pressed('esc'):
            break
        elif keyboard.is_pressed("up"):
            forward(1)
            sleep(0.5)
        elif keyboard.is_pressed("down"):
            backward(1)
            sleep(0.5)
        elif keyboard.is_pressed("left"):
            left(1)
            sleep(0.5)
        elif keyboard.is_pressed("right"):
            right(1)
            sleep(0.5)
finally:
    print("exited")