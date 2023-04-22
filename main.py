import pygame
pygame.display.set_mode([500,500])
while True:
    a = pygame.event.get()
    for f in a:
        #print(f)
        if f.type == pygame.QUIT:
            exit()
        if f.type == pygame.KEYDOWN:
            print("klavisha")
            print(pygame.KEYDOWN)
