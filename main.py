# Santos, 21 de outubro de 2021
# Iniciando o curso de criação de jogos da Alura
# Criando um jogo similar ao Pacman
##################################################################################################################
import pygame as pg

#Constantes
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)


#################################################################################################################
#Função onde o jogo ocorre
def pacman():
    pg.init()
    #############################################################################################################
    tela = pg.display.set_mode((640, 480), 0)
    x = 50
    vel_x = 0.1
    y = 50
    vel_y = 0.1
    jogando = True
    #############################################################################################################

    #loop principal do jogo
    while jogando:

        x = x + vel_x
        y = y + vel_y
        if (x + 30) > 640:
            vel_x = -0.1
        elif (x - 30) < 0:
            vel_x = 0.1
        if (y + 30) > 480:
            vel_y = -0.1
        elif (y - 30) < 0:
            vel_y = 0.1
        tela.fill((PRETO))
        pg.draw.circle(tela, AMARELO, (int(x), int(y)), 25, 0)
        pg.display.update()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()


##################################################################################################################
#Função principal para iniciar o programa
if __name__ == '__main__':
    pacman()
