import pygame, random

p = pygame.display.set_mode([800, 600])
pygame.init()
b = pygame.font.SysFont("arial", 30)
sp = b.render("Пробел", True, [255, 255, 255])
no = b.render("Не закроюсь!", True, [255, 255, 255])
while True:
    a = pygame.event.get()
    for f in a:
        if f.type == pygame.QUIT:
            p.blit(no, [250, 250])

        if f.type == pygame.KEYDOWN:
            if f.key == pygame.K_SPACE:
                p.blit(sp, [random.randint(100, 500), random.randint(100, 700)])
            else:
                b1 = b.render("Клавиша: " + str(f.key), True, [255, 70, 65])
                p.blit(b1, [random.randint(100, 500), random.randint(100, 700)])

        if f.type == pygame.MOUSEBUTTONDOWN:
            if f.button == pygame.BUTTON_RIGHT:
                b1 = b.render("Клавиша: " + str(f.button) + ", pos: " + str(f.pos), True, [255, 255, 255])
                p.blit(b1, f.pos)
            elif f.button == pygame.BUTTON_LEFT:
                b1 = b.render("Клавиша: " + str(f.button) + ", pos: " + str(f.pos), True, [70, 255, 255])
                p.blit(b1, f.pos)
            else:
                b1 = b.render("Клавиша: " + str(f.button) + ", pos: " + str(f.pos), True, [200, 100, 60])
                p.blit(b1, f.pos)
        if f.type == pygame.MOUSEMOTION:
            pygame.draw.circle(p,[255,10,10],f.pos,50,10)
        pygame.display.flip()

