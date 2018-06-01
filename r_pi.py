from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(19)

current = False

while True:
   prev = current
   current = button.is_pressed
   if current and not(prev):
      led.toggle()
