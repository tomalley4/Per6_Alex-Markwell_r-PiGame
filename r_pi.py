from gpiozero import LED, Button
from signal import pause
from time import sleep

if __name__ == "__main__":
   led_r = LED(27)
   led_b = LED(17)
   led_y = LED(4)
   led_w = LED(3)
   led_g = LED(2)
   button = Button(19)

   led_r.on()
   led_b.on()
   led_y.on()
   led_w.on()
   led_g.on()

   sleep(1)

   led_r.off()
   led_b.off()
   led_y.off()
   led_w.off()
   led_g.off()

   current = False

   '''while True:
      prev = current
      current = button.is_pressed
      if current and not(prev):
         led.toggle()
   '''
