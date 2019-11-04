import pygame
import random 

# breite window(fenster)
B_W = 1400
# hoehe window(fenster)
H_W = 400
# BREITE balken
B_B = 20
# hoehe balken
H_balken = 80
# Hoehe/Breite Ball
HB_Ball = 10

screen = pygame.display.set_mode((B_W, H_W))
farbe1 = (255, 255, 255)
weiterlaufen = True

pygame.key.set_repeat(1, 10)

# zeile balken
y_balken = random. randint(0, H_W)
print('y_balken: ', y_balken)
x_balken = B_W - B_B - 2

y_ball = random. randint(0, H_W)
x_ball = 1
print('y_ball: ', y_ball)
while weiterlaufen:
    screen.fill((250, 0, 250))

    # zeichne balken
    pygame.draw.rect(screen, farbe1, (x_balken , y_balken, B_B, H_balken), 2)
    # zeichne ball 
    pygame.draw.rect(screen, farbe1, (x_ball, y_ball, HB_Ball, HB_Ball), 2)
    pygame.display.update()
    
    # pygame.time.wait(1)

    for event in pygame.event.get():

      print(y_balken)

      if event.type == pygame.KEYDOWN:

          if event.key == pygame.K_UP:
             y_balken = y_balken - 1
          if event.key == pygame.K_DOWN:
             y_balken = y_balken + 1
     
    x_ball = x_ball + 1
    if x_ball > B_W:
        weiterlaufen = False

    print('ball: ', x_ball, y_ball)
    print('balken: ', x_balken, y_balken)
    print()

    # Test:
    # (y_ball + HB_Ball) <= y_balken   dann verloren
    # (y_ball) >= y_balken + H_balken) dann verloren
    # sonst gewonnen

    if y_ball + HB_Ball <= y_balken:
        print('verloren 1')
    else:
        if y_ball >= y_balken + H_balken:
            print('verloren 2')
        else:
                print ('gewonnen')
