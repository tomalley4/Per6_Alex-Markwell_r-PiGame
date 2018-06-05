import pygame

def binary(num, dec_inp = True):
   pass

if __name__ == '__main__':
   screen = pygame.display.set_mode((int(input("How wide should the window be?\n")), int(input("How tall should the window be?\n"))))
   running = True
   while running:
      event = pygame.event.poll()
      if event.type == pygame.QUIT:
         running = False
