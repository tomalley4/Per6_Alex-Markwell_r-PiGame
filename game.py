import pygame

screen = pygame.display.set_mode((int(input("How wide should the window be?\n")), int(input("How tall should the window be?\n"))))
running = True

if __name__ == '__main__':
   while running:
      event = pygame.event.poll()
      if event.type == pygame.QUIT:
         running = False
