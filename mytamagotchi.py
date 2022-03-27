import pygame
import time
import random
import glob

#iniciar pygame
pygame.init()

#música do jogo
pygame.mixer.music.load("sons/undertale_ost_shop.wav")
pygame.mixer.music.set_volume(0.02)

#fonte do jogo
FONTEJOGO = 'fontes/Organic_Brand.ttf'

#tela
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('My Tamagotchi')
clock = pygame.time.Clock()

#coordenadas da Muriel
x = 170
y = 178

#cores
white = (255,255,255)
black = (0,0,0)
ciano = (230, 255, 252)
lilas = (254, 240, 255)
gray = (237,237,237)
bright_gray = (237,237,237)
bright_pink = (255,222,229)
bright_yellow = (251,255,201)

#imagens do tamagotchi
tamagotchi_morto = pygame.image.load('imagens/tamagotchi/tamagotchi_morto.png')
tamagotchi_oi = pygame.image.load('imagens/tamagotchi/tamagotchi_oi.png')
tamagotchi_feliz = pygame.image.load('imagens/tamagotchi/tamagotchi_feliz.png')
    
#frames
frame_dia = pygame.image.load('imagens/frames/frame_dia.png')
frame_noite = pygame.image.load('imagens/frames/frame_noite.png')
frame_noite_dentro = pygame.image.load('imagens/frames/frame_noite_dentro.png')
frame_banho = pygame.image.load('imagens/frames/frame_banho.png')

#icone
icon = pygame.image.load('imagens/icon_tamagotchi.png')
pygame.display.set_icon(icon)

#sons
som_comendo = pygame.mixer.Sound("sons/som_comendo.wav")
som_chuveiro = pygame.mixer.Sound("sons/WaterSprayer.wav")
som_curar = pygame.mixer.Sound("sons/pokemon_healing_sound_effect.wav")
som_dormindo = pygame.mixer.Sound("sons/som_dormindo.wav")
som_morrendo = pygame.mixer.Sound("sons/som_morrendo.wav")
eterna_forest = pygame.mixer.Sound("sons/eterna_forest.wav")
musica_quase_morrendo = pygame.mixer.Sound("sons/undertale_ost_075_barrier.wav")
musica_morreu = pygame.mixer.Sound("sons/undertale_ost_078_you_idiot.wav")

#botões
botao_sair = pygame.image.load('imagens/botoes/botao_sair.png')
botao_sair2 = pygame.image.load('imagens/botoes/botao_sair2.png')
botao_remedio = pygame.image.load('imagens/botoes/botao_remedio.png')
botao_remedio2 = pygame.image.load('imagens/botoes/botao_remedio2.png')
botao_bolo = pygame.image.load('imagens/botoes/botao_bolo.png')
botao_bolo2 = pygame.image.load('imagens/botoes/botao_bolo2.png')
botao_frango = pygame.image.load('imagens/botoes/botao_frango.png')
botao_frango2 = pygame.image.load('imagens/botoes/botao_frango2.png')
botao_chuveiro = pygame.image.load('imagens/botoes/botao_chuveiro.png')
botao_chuveiro2 = pygame.image.load('imagens/botoes/botao_chuveiro2.png')
botao_dormir = pygame.image.load('imagens/botoes/botao_dormir.png')
botao_dormir2 = pygame.image.load('imagens/botoes/botao_dormir2.png')

#balões, fedor e cocô
balao_bolo = pygame.image.load('imagens/balao_bolo.png')
balao_frango = pygame.image.load('imagens/balao_frango.png')
coco = pygame.image.load('imagens/coco.png')
fedor = pygame.image.load('imagens/fedor.png')

#timers
TIMERFOME = pygame.USEREVENT
pygame.time.set_timer(TIMERFOME, 1000)
TIMERCOMENDO = 6

TIMERSONO = pygame.USEREVENT
pygame.time.set_timer(TIMERSONO, 1000)
TIMERDORMINDO = 15

TIMERSUJO = pygame.USEREVENT
pygame.time.set_timer(TIMERSUJO, 1000)

TIMERDOENTE = pygame.USEREVENT
pygame.time.set_timer(TIMERDOENTE, 1000)
TIMERREMEDIO = 10

TIMERPERIODODIA = pygame.USEREVENT
pygame.time.set_timer(TIMERPERIODODIA, 1000)

class Tamagotchi(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.spritesNormal = [pygame.image.load('imagens/tamagotchi/tamagotchi_normal.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_normal2.png')]
        self.spritesSono = [pygame.image.load('imagens/tamagotchi/tamagotchi_sono0.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono1.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono3.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono4.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono5.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono6.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono7.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_sono8.png')]
        self.spritesFome = [pygame.image.load('imagens/tamagotchi/tamagotchi_fome.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome2.png')]
        self.spritesMorrendo = [pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo0.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo1.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo3.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo4.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo5.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo6.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo7.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo8.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_morrendo9.png')]
        self.spritesFomeSono = [pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono0.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono1.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono3.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono4.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono5.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono6.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_sono7.png')]
        self.spritesFomeDoenca = [pygame.image.load('imagens/tamagotchi/tamagotchi_fome_doenca0.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_doenca1.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_doenca2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_fome_doenca3.png')]
        self.spritesFeliz = [pygame.image.load('imagens/tamagotchi/tamagotchi_feliz.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_feliz2.png')]
        self.spritesDormindo = [pygame.image.load('imagens/tamagotchi/tamagotchi_dormindo2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_dormindo2.png'),pygame.image.load('imagens/tamagotchi/tamagotchi_dormindo2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_dormindo2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_dormindo.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_dormindo.png')]
        self.spritesDoenca = [pygame.image.load('imagens/tamagotchi/tamagotchi_doenca.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca2.png')]
        self.spritesDoencaSono = [pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono0.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono1.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono2.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono3.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono4.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono5.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono6.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono7.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono8.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_doenca_sono9.png')]
        self.spritesComendoGostou = [pygame.image.load('imagens/tamagotchi/tamagotchi_comendo_gostou.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_comendo_gostou2.png')]
        self.spritesComendoNaoGostou = [pygame.image.load('imagens/tamagotchi/tamagotchi_comendo_naogostou.png'), pygame.image.load('imagens/tamagotchi/tamagotchi_comendo_naogostou2.png')]
        
        self.current_sprite = 0
        self.image = self.spritesNormal[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def update(self, x):
        self.current_sprite += 0.20

        if x == 0:
            if self.current_sprite >= len(self.spritesNormal):
                self.current_sprite = 0

            self.image = self.spritesNormal[int(self.current_sprite)]

        elif x == 1:
            if self.current_sprite >= len(self.spritesFome):
                self.current_sprite = 0

            self.image = self.spritesFome[int(self.current_sprite)]

        elif x == 3:
            if self.current_sprite >= len(self.spritesSono):
                self.current_sprite = 0

            self.image = self.spritesSono[int(self.current_sprite)]

        elif x == 4:
            if self.current_sprite >= len(self.spritesDoenca):
                self.current_sprite = 0

            self.image = self.spritesDoenca[int(self.current_sprite)]

        elif x == 5:
            if self.current_sprite >= len(self.spritesFomeSono):
                self.current_sprite = 0

            self.image = self.spritesFomeSono[int(self.current_sprite)]

        elif x == 6:
            if self.current_sprite >= len(self.spritesDoencaSono):
                self.current_sprite = 0

            self.image = self.spritesDoencaSono[int(self.current_sprite)]

        elif x == 7:
            if self.current_sprite >= len(self.spritesFomeDoenca):
                self.current_sprite = 0

            self.image = self.spritesFomeDoenca[int(self.current_sprite)]

        elif x == 8:
            if self.current_sprite >= len(self.spritesMorrendo):
                self.current_sprite = 0

            self.image = self.spritesMorrendo[int(self.current_sprite)]

        elif x == 9:
            if self.current_sprite >= len(self.spritesFeliz):
                self.current_sprite = 0

            self.image = self.spritesFeliz[int(self.current_sprite)]

        elif x == 10:
            if self.current_sprite >= len(self.spritesDormindo):
                self.current_sprite = 0

            self.image = self.spritesDormindo[int(self.current_sprite)]

        elif x == 11:
            if self.current_sprite >= len(self.spritesComendoGostou):
                self.current_sprite = 0

            self.image = self.spritesComendoGostou[int(self.current_sprite)]

        elif x == 12:
            if self.current_sprite >= len(self.spritesComendoNaoGostou):
                self.current_sprite = 0

            self.image = self.spritesComendoNaoGostou[int(self.current_sprite)]


moving_sprites = pygame.sprite.Group()
tamagotchi = Tamagotchi(x,y)
moving_sprites.add(tamagotchi)

class Nuvem(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.spritesNuvem = [pygame.image.load('imagens/frames/frame_dia.png'), pygame.image.load('imagens/frames/frame_dia_nuvem0.png'), pygame.image.load('imagens/frames/frame_dia_nuvem2.png'), pygame.image.load('imagens/frames/frame_dia_nuvem3.png'), pygame.image.load('imagens/frames/frame_dia_nuvem4.png'), pygame.image.load('imagens/frames/frame_dia_nuvem5.png'), pygame.image.load('imagens/frames/frame_dia_nuvem6.png'), pygame.image.load('imagens/frames/frame_dia_nuvem7.png'), pygame.image.load('imagens/frames/frame_dia_nuvem8.png'), pygame.image.load('imagens/frames/frame_dia_nuvem9.png')]

        self.current_sprite = 0
        self.image = self.spritesNuvem[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]

    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.spritesNuvem):
            self.current_sprite = 0

        self.image = self.spritesNuvem[int(self.current_sprite)]

nuvens_sprites = pygame.sprite.Group()
dianuvem = Nuvem(x,y)
nuvens_sprites.add(dianuvem)
 

#funções gerais
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
             
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,50))

    smallText = pygame.font.Font("freesansbold.ttf",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)),(y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def randomizer(x):
    r = random.randrange(0,x)
    return r

def quitgame():
    pygame.quit()
    quit()
    

#telas
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font(FONTEJOGO, 100)
        TextSurf, TextRect = text_objects("Muriel,", largeText)
        TextRect.center = ((display_width/2), (15*display_height/20))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font(FONTEJOGO, 70)
        TextSurf, TextRect = text_objects("a Tamagotchi", largeText)
        TextRect.center = ((display_width/2), (9*display_height/10))
        gameDisplay.blit(TextSurf, TextRect)
        
        gameDisplay.blit(tamagotchi_oi,(display_width/3,(2*display_height)/12))

        button("JOGAR",120,150,120,50,white,bright_pink,game_loop)
        button("SAIR",550,150,120,50,white,bright_yellow,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def murielMorreu():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(som_morrendo)
    pygame.mixer.Sound.play(musica_morreu)
    pygame.mixer.Sound.set_volume(som_morrendo, 0.3)
    pygame.mixer.Sound.set_volume(musica_morreu, 0.1)
    pygame.mixer.Sound.fadeout(musica_morreu,5000)
    
    gameDisplay.fill(ciano)
    largeText = pygame.font.Font(FONTEJOGO, 80)
    TextSurf, TextRect = text_objects("A Muriel morreu...", largeText)
    TextRect.center = ((display_width/2), (3*display_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(tamagotchi_morto,(display_width/3,(2*display_height)/12))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("VOLTAR NO TEMPO",80,50,350,50,white,bright_pink,game_loop)
        button("SAIR",550,50,150,50,white,bright_yellow,quitgame)

        pygame.display.update()
        clock.tick(15)
        
def sair():
    clock.tick(60)
    start = time.time()

    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(som_morrendo)
    pygame.mixer.Sound.play(musica_quase_morrendo)
    pygame.mixer.Sound.set_volume(som_morrendo, 0.3)
    pygame.mixer.Sound.set_volume(musica_quase_morrendo, 0.1)
    pygame.mixer.Sound.fadeout(musica_quase_morrendo, 3000)

    gameDisplay.fill(white)
    largeText = pygame.font.Font(FONTEJOGO, 100)
    TextSurf, TextRect = text_objects("Voce escolheu", largeText)
    TextRect.center = ((display_width/2), (15*display_height/20))
    gameDisplay.blit(TextSurf, TextRect)

    largeText = pygame.font.Font(FONTEJOGO, 70)
    TextSurf, TextRect = text_objects("matar a Muriel.", largeText)
    TextRect.center = ((display_width/2), (9*display_height/10))
    gameDisplay.blit(TextSurf, TextRect)

    gameDisplay.blit(tamagotchi_morto,(display_width/3,(2*display_height)/12))
       
    pygame.display.update()
    time.sleep(3)

def venceu():
    clock.tick(60)
    start = time.time()

    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(eterna_forest)
    pygame.mixer.Sound.set_volume(eterna_forest, 0.3)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font(FONTEJOGO, 70)
        TextSurf, TextRect = text_objects("Voce cuidou da Muriel", largeText)
        TextRect.center = ((display_width/2), (15*display_height/20))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.Font(FONTEJOGO, 70)
        TextSurf, TextRect = text_objects("enquanto ela precisava!", largeText)
        TextRect.center = ((display_width/2), (9*display_height/10))
        gameDisplay.blit(TextSurf, TextRect)

        gameDisplay.blit(tamagotchi_feliz,(display_width/3,(2*display_height)/12))
                

        button("CUIDAR NOVAMENTE",80,50,350,50,white,bright_pink,game_loop)
        button("SAIR",550,50,150,50,white,bright_yellow,quitgame)
        
        pygame.display.update()
        clock.tick(15)
    
    

#Ações
def comer(gostou, vontade_coco, sujo, quantos_dias, periodo_dia):
    clock = pygame.time.Clock()
    moving_sprites.draw(gameDisplay)
    pygame.mixer.Sound.play(som_comendo)
    pygame.mixer.Sound.set_volume(som_comendo,0.1)

    tempo = True
    contadortempo = 0
 

    while tempo:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == TIMERPERIODODIA:
                contadortempo += 1
                periodo_dia += 1

                if contadortempo == TIMERCOMENDO:
                    tempo = False
                
        if gostou:
            moving_sprites.update(11)
        elif not gostou:
            moving_sprites.update(12)

        if periodo_dia <= 30:    
            nuvens_sprites.update()
            nuvens_sprites.draw(gameDisplay)
        elif periodo_dia > 30:
            gameDisplay.blit(frame_noite_dentro,(0,0))
    
            
        moving_sprites.draw(gameDisplay)
        botaoremedio()
        botaobolo()
        botaofrango()
        botaochuveiro()
        botaodormir()
        botaosair()
        mostrardias(quantos_dias)

        if sujo > 50:
            mostrar_fedor()

        if vontade_coco:
            mostrar_coco()
        
        clock.tick(10)
        pygame.display.update()
        
    #time.sleep(2)
    pygame.mixer.Sound.set_volume(som_comendo,0)
    return gostou, periodo_dia

def esta_dormindo(vontade_coco, sujo, quantos_dias, periodo_dia):
    clock.tick(60)
    start = time.time()
    moving_sprites.draw(gameDisplay)
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.Sound.play(som_dormindo)
    pygame.mixer.Sound.set_volume(som_dormindo,0.6)

    tempo = True
    contadortempo = 0

    while tempo:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == TIMERPERIODODIA:
                contadortempo += 1
                periodo_dia += 1

                if contadortempo == TIMERDORMINDO:
                    tempo = False
                
        moving_sprites.update(10)

        if periodo_dia <= 30:    
            nuvens_sprites.update()
            nuvens_sprites.draw(gameDisplay)
        elif periodo_dia > 30:
            gameDisplay.blit(frame_noite_dentro,(0,0))
            
        moving_sprites.draw(gameDisplay)
        botaoremedio()
        botaobolo()
        botaofrango()
        botaochuveiro()
        botaodormir()
        botaosair()
        mostrardias(quantos_dias)

        if sujo > 50:
            mostrar_fedor()

        if vontade_coco:
            mostrar_coco()


        clock.tick(10)
        pygame.display.update()

    pygame.mixer.Sound.set_volume(som_dormindo,0)
    return periodo_dia

def tomar_banho():
    clock.tick(60)
    start = time.time()

    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.Sound.play(som_chuveiro)
    pygame.mixer.Sound.set_volume(som_chuveiro,1)

    gameDisplay.blit(frame_banho,(0,0))
    pygame.display.update()
    time.sleep(5)
    pygame.mixer.Sound.set_volume(som_chuveiro,0)


def tomar_remedio(vontade_coco, sujo, quantos_dias, periodo_dia):
    clock = pygame.time.Clock()
    moving_sprites.draw(gameDisplay)
    pygame.mixer.Sound.play(som_curar)
    pygame.mixer.Sound.set_volume(som_curar,0.2)

    tempo = True
    contadortempo = 0

    while tempo:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == TIMERPERIODODIA:
                contadortempo += 1
                periodo_dia += 1

                if contadortempo == TIMERREMEDIO:
                    tempo = False

        moving_sprites.update(12)
    
        if periodo_dia <= 30:    
            nuvens_sprites.update()
            nuvens_sprites.draw(gameDisplay)
        elif periodo_dia > 30:
            gameDisplay.blit(frame_noite_dentro,(0,0))


        moving_sprites.draw(gameDisplay)
        botaoremedio()
        botaobolo()
        botaofrango()
        botaochuveiro()
        botaodormir()
        botaosair()
        mostrardias(quantos_dias)

        if sujo > 50:
            mostrar_fedor()

        if vontade_coco:
            mostrar_coco()

        
        clock.tick(10)
        pygame.display.update()
    
    pygame.mixer.Sound.set_volume(som_curar,0)
    return periodo_dia
      

#Botões
def botaosair():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 128 > mouse[0] > 0 and 128 > mouse[1] > 0:
        gameDisplay.blit(botao_sair2,(10,0))
            
    else:
        gameDisplay.blit(botao_sair,(10,0))

def botaoremedio():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 160 > mouse[0] > 0 and 160 + 450 > mouse[1] > 450:
        gameDisplay.blit(botao_remedio2,(0,450))
            
    else:
        gameDisplay.blit(botao_remedio,(0,450))

def botaobolo():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (160)*2 > mouse[0] > 160 and 160 + 450 > mouse[1] > 450:
        gameDisplay.blit(botao_bolo,(160,450))
            
    else:
        gameDisplay.blit(botao_bolo2,(160,450))

def botaofrango():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (160)*3 > mouse[0] > 160+160 and 160 + 450 > mouse[1] > 450:
        gameDisplay.blit(botao_frango2,(160+160,450))
            
    else:
        gameDisplay.blit(botao_frango,(160+160,450))

def botaochuveiro():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (160)*4 > mouse[0] > 160+160+160 and 160 + 450 > mouse[1] > 450:
        gameDisplay.blit(botao_chuveiro2,(160+160+160,450))
            
    else:
        gameDisplay.blit(botao_chuveiro,(160+160+160,450))

def botaodormir():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (160)*5 > mouse[0] > 160+160+160+160 and 160 + 450 > mouse[1] > 450:
        gameDisplay.blit(botao_dormir2,(160+160+160+160,450))
            
    else:
        gameDisplay.blit(botao_dormir,(160+160+160+160,450))


#Balões, fedor e cocô
def balaobolo():
    gameDisplay.blit(balao_bolo,(50,130))

def balaofrango():
    gameDisplay.blit(balao_frango,(50,130))

def mostrar_coco():
    gameDisplay.blit(coco,(325,178))

def mostrar_fedor():
    gameDisplay.blit(fedor,(165,160))


#mostrar dias
def mostrardias(quantos_dias):
    largeText = pygame.font.Font(FONTEJOGO, 20)
    TextSurf = largeText.render("Dias de vida:", True, white)
    TextRect = TextSurf.get_rect()
    TextRect.center = (200), (20)
    gameDisplay.blit(TextSurf, TextRect)

    quantos_dias = str(quantos_dias)
    largeText = pygame.font.Font(FONTEJOGO, 20)
    TextSurf = largeText.render(quantos_dias, True, white)
    TextRect = TextSurf.get_rect()
    TextRect.center = (275), (20)
    gameDisplay.blit(TextSurf, TextRect)

    
#jogo
def game_loop():
    
    fome = 70
    sono = 0
    doença = 0
    vontadeCoco = 0
    sujo = 0
    doente = False
    quanto_tempo_doente = 0
    periodo_dia = 0
    dia = True
    quantos_dias = 0
    desejo = 0

    pygame.mixer.music.play(-1)
    
    gameExit = False
    dormindo = False
    comendo = False
    tomando_banho = False
    tomando_remedio = False
    coco_aparece = False

    clock = pygame.time.Clock()


    while not gameExit:

        pygame.mixer.music.unpause()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        gostou = False
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if 128 > mouse[0] > 0 and 128 > mouse[1] > 0:
                if click[0] == 1:
                    sair()
                    quitgame()
                        
            if event.type == TIMERPERIODODIA:
                if periodo_dia > 61:
                    periodo_dia -= 1
                elif periodo_dia < 61:
                    periodo_dia += 1
                elif periodo_dia == 61:
                    periodo_dia = 0
                    quantos_dias += 1
                    if quantos_dias >= 5:
                        venceu()

            if event.type == TIMERFOME:
                if fome < 0:
                    fome += 1
                elif fome > 0:
                    fome -= 1

                if fome == 0:
                    pygame.time.set_timer(TIMERFOME, 0)
                    murielMorreu()

            #desejo = 0  ---> não tá com desejo de nada
            #desejo = 1  ---> tá com desejo de frango
            #desejo = 2  ---> tá com desejo de bolo

            if  desejo == 1 and ((160)*3 > mouse[0] > 160+160) and (160 + 450 > mouse[1] > 450):
                if click[0] == 1:
                    comendo = True
                    gostou = True
            elif desejo == 2 and ((160)*2 > mouse[0] > 160) and (160 + 450 > mouse[1] > 450):
                if click[0] == 1:
                    comendo = True
                    gostou = True
            else:
                if (((160)*3 > mouse[0] > 160+160) and (160 + 450 > mouse[1] > 450)) or ((160*2 > mouse[0] > 160) and (160 + 450 > mouse[1] > 450)):
                    if click[0] == 1:
                        comendo = True
                        gostou = False
                        
            #COCO
            if (coco_aparece and (432 < mouse[0] < 490) and (370 < mouse[1] < 435)):
                if click[0] == 1:
                    coco_aparece = False
                    
            #BANHO
            if event.type == TIMERSUJO:
                if sujo > 100:
                    sujo -= 1
                elif sujo < 100:
                    sujo += 1

                if sujo == 100:
                    murielMorreu()

            if ((160)*4 > mouse[0] > 160+160+160) and (160 + 450 > mouse[1] > 450):
                if click[0] == 1:
                    tomando_banho = True

            #DORMIR
            if event.type == TIMERSONO:
                if sono > 100:
                    sono -= 1
                elif sono < 100:
                    sono += 1

                if sono == 100:
                    murielMorreu()

            if (160)*5 > mouse[0] > 160+160+160+160 and 160 + 450 > mouse[1] > 450:
                if click[0] == 1:
                    dormindo = True

            #TOMAR PILULA
            if event.type == TIMERDOENTE:
                if doente == True:
                    if quanto_tempo_doente > 100:
                        quanto_tempo_doente -= 1
                    elif quanto_tempo_doente < 100:
                        quanto_tempo_doente += 1

                    if quanto_tempo_doente >= 50:
                        murielMorreu()
                
            if (160 > mouse[0] > 0) and (160 + 450 > mouse[1] > 450):
                if click[0] == 1:
                    tomando_remedio = True                  

    
#################################################### MOSTRAR NA TELA

        nuvens_sprites.draw(gameDisplay)
        
        if periodo_dia <= 30:    
            nuvens_sprites.update()
        elif periodo_dia > 30:
            gameDisplay.blit(frame_noite_dentro,(0,0))

        botaoremedio()
        botaobolo()
        botaofrango()
        botaochuveiro()
        botaodormir()
        botaosair()
        mostrardias(quantos_dias)

        moving_sprites.draw(gameDisplay)
                   
        if comendo == False and (tomando_banho == False) and (tomando_remedio == False) and (dia == True):

            if fome >= 80 and sono <= 20 and doente == False:
                moving_sprites.update(9)

            #mostrar tamagotchi apenas com fome 
            elif sono <= 50 and doente == False:
                if fome > 40:
                    moving_sprites.update(0)
                elif fome == 40:
                    moving_sprites.update(0)
                    r = randomizer(2)
                    if r == 0:
                        desejo = 1
                    elif r == 1:
                        desejo = 2
                elif fome < 40 and fome > 0:
                    moving_sprites.update(1)
                    if desejo == 1:
                        balaofrango()
                    elif desejo == 2:
                        balaobolo()
                elif fome <= 0:
                    gameDisplay.blit(tamagotchi_morto, (x,y))

            elif fome >= 40 and doente == False:
                if sono <= 50:
                    moving_sprites.update(0)
                    
                elif sono > 50 and sono < 100:
                    moving_sprites.update(3)

                elif sono >= 100:
                    gameDisplay.blit(tamagotchi_morto, (x,y))

            #mostrar tamagotchi apenas doente
            elif fome >= 40 and sono <= 50:
                if doente == True:
                    if quanto_tempo_doente >= 50:
                        gameDisplay.blit(tamagotchi_morto, (x,y))
                    else:
                        moving_sprites.update(4)
                else:
                    moving_sprites.update(0)

            #mostrar tamagotchi com sono e com fome
            elif fome < 40 and sono > 50 and doente == False:
                if fome == 0 or sono == 100:
                    gameDisplay.blit(tamagotchi_morto, (x,y))
                else:
                    moving_sprites.update(5)

            #mostrar tamagotchi com sono e doente
            elif fome >= 40 and sono > 50 and doente == True:
                if sono >= 100 or quanto_tempo_doente >= 50:
                    gameDisplay.blit(tamagotchi_morto, (x,y))
                else:
                    moving_sprites.update(6)
                    
            #mostrar tamagotchi com fome e doente:
            elif fome < 40 and sono <= 50 and doente == True:
                if fome == 0 or quanto_tempo_doente >= 50:
                    gameDisplay.blit(tamagotchi_morto, (x,y))
                else:
                    moving_sprites.update(7)

            #todos
            elif fome < 40 and sono > 50 and doente == True:
                if fome == 0 or sono == 100 or quanto_tempo_doente >= 50:
                    gameDisplay.blit(tamagotchi_morto, (x,y))
                else:
                    moving_sprites.update(8)
                    
            

                
#######################################################

        #randomizar doenca
                
        if doente == False:
            doenca = randomizer(1000)

            if doenca == 2:
                doente = True

                quanto_tempo_doente = 0
            
#######################################################
            

        if (comendo == False) and (tomando_banho == False) and (tomando_remedio == False) and (dia == False):
            gameDisplay.blit(frame_noite,(0,0))

        if (comendo == True):
            gostou, periodo_dia = comer(gostou, coco_aparece, sujo, quantos_dias, periodo_dia)
            if gostou == True:
                fome += 40
            elif gostou == False:
                fome += 20

            desejo = 0
            vontadeCoco += 34
            
            comendo = False
            gostou = False

            if fome > 100:
                fome = 100

        if vontadeCoco >= 100:
            coco_aparece = True
            vontadeCoco = 0
        
        if (tomando_banho == True):
            tomar_banho()
            pygame.mixer.music.set_volume(0.02)
            tomando_banho = False
            sujo = 0

        if (dormindo == True):
            esta_dormindo(coco_aparece, sujo, quantos_dias, periodo_dia)
            pygame.mixer.music.set_volume(0.02)
            dormindo = False
            sono = 0            
             
        if(tomando_remedio == True):
            periodo_dia = tomar_remedio(coco_aparece, sujo, quantos_dias, periodo_dia)
            tomando_remedio = False
            doente = False

        if coco_aparece:
            mostrar_coco()

        if sujo > 50:
            mostrar_fedor()

            
        clock.tick(10)
        pygame.display.update()
    

game_intro()
game_loop()
pygame.quit()
quit()

