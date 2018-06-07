from game import *
from r_pi import *

if input("Do you want to initially input decimal or binary? (d/b)\n")[0].lower() == 'b':
   r,b,y,w,g = 0,1,2,3,4

   current = [False, False, False, False, False]
   testing = True

   run = [0,0,0,0,0]

   while True:
      prev = eval(str(current))
      current[r] = but_r.is_pressed
      current[b] = but_b.is_pressed
      current[y] = but_y.is_pressed
      current[w] = but_w.is_pressed
      current[g] = but_g.is_pressed

      if current[r] and not(prev[r]):
         led_r.toggle()
         run[4] = 1-run[4]
      if current[b] and not(prev[b]):
         led_b.toggle()
         run[3] = 1-run[3]
      if current[y] and not(prev[y]):
         led_y.toggle()
         run[2] = 1-run[2]
      if current[w] and not(prev[w]):
         led_w.toggle()
         run[1] = 1-run[1]
      if current[g] and not(prev[g]):
         led_g.toggle()
         run[0] = 1-run[0]

      if but_run.is_pressed: break
   run2 = 0
   for i in range(5):
      run2 += run[i]*[1,10,100,1000,10000][i]
   print(binary(run2, False))
else:
   numb = int(input("Input a decimal value between 1 and 31: "))
   use = '00000'+str(binary(numb))
   if use[-5] == '1': led_r.on()
   else: led_r.off()
   if use[-4] == '1': led_b.on()
   else: led_b.off()
   if use[-3] == '1': led_y.on()
   else: led_y.off()
   if use[-2] == '1': led_w.on()
   else: led_w.off()
   if use[-1] == '1': led_g.on()
   else: led_g.off()
   but_run.wait_for_press()

led_r.off()
led_b.off()
led_y.off()
led_w.off()
led_g.off()
