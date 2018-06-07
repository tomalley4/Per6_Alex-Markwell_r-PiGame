from gpiozero import LED, Button
from signal import pause
from time import sleep

led_r = LED(27)
led_b = LED(17)
led_y = LED(4)
led_w = LED(3)
led_g = LED(2)

but_r = Button(26)
but_b = Button(19)
but_y = Button(13)
but_w = Button(6)
but_g = Button(5)

but_run = Button(21)

if __name__ == "__main__":
   but_run.wait_for_press()
   
   led_r.on()
   led_b.on()
   led_y.on()
   led_w.on()
   led_g.on()

   but_run.wait_for_release()
   but_run.wait_for_press()

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
