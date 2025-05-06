import time
from pygame.locals import *
import pygame, random

AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons2.png'
RED = (255,0,0)
GREEN = (0,255,0)
blue = (0,0,255)
blue2 = (70,200,255)
indigo = (75,0,130)
orange = (255,102,0)
yellow = (255,255,0)
violet = (128,0,255)
grey = (128,128,128)
maroon = (153,76,0)
black = (0,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
olive = (128,128,0)
CYAN = (0,255,255)
pink = (255,192,203)
MAGENTA = (255,0,255)
tan = (210,180,140)
teal = (0,128,128)
guanyador = 0

bala1 = pygame.image.load('assets/bala1.png')
bala2 = pygame.image.load('assets/bala2.png')
bala3 = pygame.image.load('assets/bala3.png')
bala12 = pygame.image.load('assets/bala12.png')
bala22 = pygame.image.load('assets/bala22.png')
bala32 = pygame.image.load('assets/bala32.png')
boom2 = pygame.image.load('assets/boom.png')
boom = pygame.image.load('assets/boom2.png')
gameover = pygame.image.load('assets/gameover2.png')
gameover2 = pygame.image.load('assets/gameover1.png')



# pantalles del joc
# pantalla actual = 1 = menu
# pantalla actual = 2 = credits
# pantalla actual = 3 = joc
# pantalla actual = 4 = game over
pantalla_actual = 1

# Jugador 1:
player_image = pygame.image.load('assets/nau1.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 7

# Jugador 2
player_image2 = pygame.image.load('assets/nau22.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 7

car_image = pygame.image.load('assets/car.png')
car_image2 = pygame.image.load('assets/car2.png')
car_rect = car_image.get_rect(midbottom=(AMPLADA // 1.3, ALTURA - 300))
car_rect2 = car_image2.get_rect(midbottom=(AMPLADA // 40, ALTURA - 190))
velocitat_car = 6
car_rect2.x = -300
car_rect.x = 650

# vides:
vides_jugador1 = 5
vides_jugador2 = 5
vides_jugador1_image = pygame.image.load('assets/cor1.png')
vides_jugador2_image = pygame.image.load('assets/cor2.png')


# Bala rectangular blanca:
bala_imatge = pygame.Surface((13,24)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
bales_jugador12 = [] #llista on guardem les bales del jugador 1
bales_jugador22 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 12
velocitat_bales2 = 7
temps_entre_bales = 400 #1 segon
temps_entre_bales2 = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2
temps_ultima_bala_jugador12 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador22 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.play()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Joc de naus") # Arcade

# Control de FPS
clock = pygame.time.Clock()
fps = 40

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def show_menu():
    imprimir_pantalla_fons("assets/fons2.png")
    text0 = "Arcatac!"
    text1 = "1. Començar partida"
    text2 = "2. Crèdits"
    text3 = "3. Sortir"
    font0 = pygame.font.SysFont(None, 100)
    font1 = pygame.font.SysFont(None, 50)
    img0 = font0.render(text0, True, black)
    img1 = font1.render(text1, True, blue)
    img2 = font1.render(text2, True, blue)
    img3 = font1.render(text3, True, RED)
    pantalla.blit(img0, (60, 60))
    pantalla.blit(img1, (60, 200))
    pantalla.blit(img2, (60, 300))
    pantalla.blit(img3, (60, 400))

def show_credits():
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    text0 = "Arcatac"
    text1 = "Programació:"
    text2 = "Gràfics:"
    text3 = "Música:"
    text4 = "Sons:"
    text5 = "Arnau Casadó i Xavi Sancho"
    text6 = "Rotch Gwylt - Tema"
    text7 = "Freesound.org"
    text8 = "Arnau Casadó"
    font0 = pygame.font.SysFont(None, 140)
    font1 = pygame.font.SysFont(None, 60)
    font2 = pygame.font.SysFont(None, 50)
    img0 = font0.render(text0, True, black)
    img1 = font1.render(text1, True, black)
    img2 = font1.render(text2, True, black)
    img3 = font1.render(text3, True, black)
    img4 = font1.render(text4, True, black)
    img5 = font2.render(text5, True, yellow)
    img6 = font2.render(text6, True, yellow)
    img7 = font2.render(text7, True, yellow)
    img8 = font2.render(text8, True, yellow)
    pantalla.blit(img0, (60, 60))
    pantalla.blit(img1, (60, 200))
    pantalla.blit(img5, (160, 250))
    pantalla.blit(img2, (60, 300))
    pantalla.blit(img8, (160, 350))
    pantalla.blit(img3, (60, 400))
    pantalla.blit(img6, (160, 450))
    pantalla.blit(img4, (60, 500))
    pantalla.blit(img7, (160, 550))

def moure_cotxes():
    car_rect.x -= velocitat_car #dreta a esquerra
    car_rect2.x += velocitat_car
    pantalla.blit(car_image,car_rect)
    pantalla.blit(car_image2, car_rect2)
    if car_rect.x + car_image.get_width() <= 0:
        aux = random.randint(200,2500,)
        car_rect.x = 700 + aux
    if car_rect2.x + car_image2.get_width() >= 900:
        aux = random.randint(400, 800, )
        car_rect2.x = 200 - aux




while True:
    #contador
    current_time = pygame.time.get_ticks()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                if event.key == K_3:
                    pygame.quit()
                if event.key == K_1:
                    pantalla_actual = 3
                if event.key == K_2:
                    pantalla_actual = 2

        if pantalla_actual == 2:
            show_credits()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1

        if pantalla_actual == 4 :
            for i in bales_jugador1:
                bales_jugador1.remove(i)
            for i in bales_jugador2:
                bales_jugador2.remove(i)
            for i in bales_jugador12:
                bales_jugador12.remove(i)
            for i in bales_jugador22:
                bales_jugador22.remove(i)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1
                    vides_jugador1 = 5
                    vides_jugador2 = 5




        if pantalla_actual == 3:

            # controlar trets de les naus
            if event.type == KEYDOWN:
                #jugador 1

                if event.key == K_UP and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                    pygame.mixer.music.load('assets/normal.mp3')
                    pygame.mixer.music.play()
                # jugador 2
                if event.key == K_w and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time
                    pygame.mixer.music.load('assets/laser.mp3')
                    pygame.mixer.music.play()

                if event.key == K_DOWN and current_time - temps_ultima_bala_jugador12 >= temps_entre_bales2:
                    bales_jugador12.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador12 = current_time
                    pygame.mixer.music.load('assets/supernormal.mp3')
                    pygame.mixer.music.play()
                # jugador 2
                if event.key == K_s and current_time - temps_ultima_bala_jugador22 >= temps_entre_bales2:
                    bales_jugador22.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador22 = current_time
                    pygame.mixer.music.load('assets/superlaser.mp3')
                    pygame.mixer.music.play()





    if pantalla_actual == 4:
        imprimir_pantalla_fons('assets/gameover1.png')
        text = "Player " + str(guanyador) + " Wins!"
        font = pygame.font.SysFont(None, 100)
        img = font.render(text,True, RED)
        pantalla.blit(img,(175,450))


    if pantalla_actual == 1:
        show_menu()


    if pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            player_rect.x -= velocitat_nau
        if keys[K_RIGHT]:
            player_rect.x += velocitat_nau

        # Moviment del jugador 2
        if keys[K_a]:
            player_rect2.x -= velocitat_nau2
        if keys[K_d]:
            player_rect2.x += velocitat_nau2
        # if keys[k_q]:
        #     car_rect.x -= velocitat_car
        # if keys[k_e]:
        #     car_rect.x += velocitat_car

        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())


        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala2, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("El jugador 1 ha rebut un impacte")
                bales_jugador1.remove(bala)  # eliminemd la bala
                pantalla.blit(boom, player_rect2)
                vides_jugador2 = vides_jugador2 - 1
            if car_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador1.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect)
            if car_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador1.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect2)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1


        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala32, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("El jugador 2 ha rebut un impacte")
                bales_jugador2.remove(bala)  # eliminem la bala
                pantalla.blit(boom, player_rect)
                vides_jugador1 = vides_jugador1 - 1
            if car_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador2.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect)

            if car_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador2.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect2)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        for bala in bales_jugador12: # bucle que recorre totes les bales
            bala.y -= velocitat_bales2 # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador12.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala1, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("El jugador 1 ha rebut un impacte")
                bales_jugador12.remove(bala)  # eliminemd la bala
                pantalla.blit(boom, player_rect2)
                vides_jugador2 = vides_jugador2 - 2
            if car_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador12.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect)
            if car_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador12.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect2)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1


        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador22:
            bala.y += velocitat_bales2
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador22.remove(bala)
            else:
                pantalla.blit(bala12, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("El jugador 2 ha rebut un impacte")
                bales_jugador22.remove(bala)  # eliminem la bala
                pantalla.blit(boom, player_rect)
                vides_jugador1 = vides_jugador1 - 2
            if car_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador22.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect)
            if car_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                bales_jugador22.remove(bala)  # eliminemd la bala
                pantalla.blit(boom2, car_rect2)
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1



        # dibuixar vides
        if vides_jugador1 >= 5:
            pantalla.blit(vides_jugador1_image, (720, 530))
        if vides_jugador1 >= 4:
            pantalla.blit(vides_jugador1_image, (740, 530))
        if vides_jugador1 >= 3:
            pantalla.blit(vides_jugador1_image, (700, 550))
        if vides_jugador1 >= 2:
            pantalla.blit(vides_jugador1_image, (720, 550))
        if vides_jugador1 >= 1:
            pantalla.blit(vides_jugador1_image, (740, 550))
        if vides_jugador1 <= 0:
            pantalla_actual = 4
            # vides_jugador2 = 0


        # dibuixar vides
        if vides_jugador2 >= 5:
            pantalla.blit(vides_jugador2_image, (80, 80))
        if vides_jugador2 >= 4:
            pantalla.blit(vides_jugador2_image, (60, 80))
        if vides_jugador2 >= 3:
            pantalla.blit(vides_jugador2_image, (100, 50))
        if vides_jugador2 >= 2:
            pantalla.blit(vides_jugador2_image, (80, 50))
        if vides_jugador2 >= 1:
            pantalla.blit(vides_jugador2_image, (60, 50))


        if vides_jugador2 <=0 or vides_jugador1 <=0:
            guanyador = 1
            if vides_jugador1 <= 0:
                guanyador = 2
            pantalla_actual = 4
            # vides_jugador1 = 0

    if pantalla_actual == 3:
    #dibuixar els jugadors:
        moure_cotxes()
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

    # if pantalla_actual == 3:
    #     pygame.mixer.music.load('assets/music.mp3')
    #     pygame.mixer.music.play()

    # if pantalla_actual == 4:
    #     pygame.mixer.music.load('assets/music2.mp3')
    #     pygame.mixer.music.play()
    #
    # if pantalla_actual == 2:
    #     pygame.mixer.music.load('assets/music1.mp3')
    #     pygame.mixer.music.play()


    pygame.display.update()
    clock.tick(fps)
