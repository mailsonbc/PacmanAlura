# Santos, 21 de outubro de 2021
# Iniciando o curso de criação de jogos da Alura
# Criando um jogo similar ao Pacman
##################################################################################################################
import pygame as pg

# Constantes
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
FPS = 60
TELA_X = 800
TELA_Y = 600


#################################################################################################################
# Classes
class Pacman:
    def __init__(self):
        self.linha = 1
        self.coluna = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = TELA_X // 30
        self.vel_x = 1
        self.vel_y = 1
        self.raio = self.tamanho // 2

    def calcular_regras (self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        if self.centro_x + self.raio > TELA_X:
            self.vel_x = -1
        if self.centro_x - self.raio < 0:
            self.vel_x = 1
        if self.centro_y + self.raio > TELA_Y:
            self.vel_y = -1
        if self.centro_y - self.raio < 0:
            self.vel_y = 1


    # Método para desenhar o pacman
    def pintar(self, tela):
        # Desenhar o corpo
        pg.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenhar a boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pg.draw.polygon(tela, PRETO, pontos, 0)

        # Desenhar o olho
        olho_x = int(self.centro_x + self.raio / 6)
        olho_y = int(self.centro_y - self.raio * 0.55)
        olho_raio = int(self.raio / 10)
        pg.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

#################################################################################################################
# Função onde o jogo ocorre
def pacman():
    # criando o objeto pacman
    pacman = Pacman()

    pg.init()
    tela = pg.display.set_mode((TELA_X, TELA_Y), 0)
    jogando = True

    # loop principal do jogo
    while jogando:


        tela.fill(PRETO)
        pacman.pintar(tela)
        pacman.calcular_regras()
        pg.display.update()
        pg.time.delay(100)

        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()


##################################################################################################################
# Função principal para iniciar o programa
if __name__ == '__main__':
    pacman()
