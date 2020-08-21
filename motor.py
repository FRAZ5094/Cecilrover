import RPi.GPIO as gpio
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
    gpio.output(left_forward,True)
    gpio.output(right_forward,True)
    sleep(time)
    gpio.output(left_forward,False)
    gpio.output(right_forward,False)

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

def right(time):
    print(f"right for {time} second")
    gpio.output(left_forward,True)
    gpio.output(right_backward,True)
    sleep(time)
    gpio.output(left_forward,False)
    gpio.output(right_backward,False)

try:
    while True:
        char = screen.getch()
        if char == ord("q"):
            break
        elif char == curses.KEY_UP:
            forward(0.5)
            sleep(0.5)
        elif char == curses.KEY_DOWN:
            backward(0.5)
            sleep(0.5)
        elif char == curses.KEY_LEFT:
            left(0.4)
            sleep(0.4)
        elif char == curses.KEY_RIGHT:
            right(0.4)
            sleep(0.4)
finally:
    print("exited")
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    gpio.cleanup()