from gpiozero import LED
from time import sleep

led = LED(17)

wait = float(input("How many seconds should the light stay on at a time?\n"))

while True:
    led.on()
    sleep(wait)
    led.off()
    sleep(wait)
