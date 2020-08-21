#import RPi.GPIO as gpio
from time import sleep
import keyboard
import curses


screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
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
    return
    gpio.output(left_forward,True)
    gpio.output(right_forward,True)
    sleep(time)
    gpio.output(left_forward,False)
    gpio.output(right_forward,False)
    gpio.cleanup()

def backward(time):
    print(f"backward for {time} second")
    return
    gpio.output(left_backward,True)
    gpio.output(right_backward,True)
    sleep(time)
    gpio.output(left_backward,False)
    gpio.output(right_backward,False)   

def left(time):
    print(f"left for {time} second")
    return
    gpio.output(left_backward,True)
    gpio.output(right_forward,True)
    sleep(time)
    gpio.output(left_backward,False)
    gpio.output(right_forward,False)
    gpio.cleanup()

def right(time):
    print(f"right for {time} second")
    return
    gpio.output(left_forward,True)
    gpio.output(right_backward,True)
    time(sleep)
    gpio.output(left_forward,False)
    gpio.output(right_backward,False)

try:
    while True:
        char = screen.getch()
        if char == ord('esc'):
            break
        elif char == curses.KEY_UP:
            forward(1)
            sleep(0.5)
        elif char == curses.KEY_DOWN:
            backward(1)
            sleep(0.5)
        elif char == curses.KEY_LEFT:
            left(1)
            sleep(0.5)
        elif char == curses.KEY_RIGHT:
            right(1)
            sleep(0.5)
finally:
    print("exited")
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()