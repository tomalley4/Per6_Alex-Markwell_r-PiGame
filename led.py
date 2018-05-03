from gpiozero import LED
from time import sleep

led = LED(17)

wait = 0.1

while True:
    led.on()
    sleep(wait)
    led.off()
    sleep(wait)
