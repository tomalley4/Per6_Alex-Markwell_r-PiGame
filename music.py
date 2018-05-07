from gpiozero import Buzzer
from time import sleep

beep = Buzzer(17)

def wait(hertz):
   return ((1 / hertz) / 2) * 1000

songT = []
waitT = []

songS = []
waitS = []

song = songT + [s] + songS
wait = waitT + [w] + waitS
