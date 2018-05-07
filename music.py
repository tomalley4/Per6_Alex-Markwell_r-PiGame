from gpiozero import Buzzer
from time import sleep

def wait(hertz):
	return ((1 / hertz) / 2) * 1000000

songT = []
waitT = []

songS = []
waitS = []
