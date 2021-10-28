# Santos, 21 de outubro de 2021
# Iniciando o curso de criação de jogos da Alura
# Criando um jogo similar ao Pacman
##################################################################################################################
import pygame as pg

# Constantes
AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 50
        self.vel_x = 0.05
        self.vel_y = 0.05
        self.raio = self.tamanho / 2


    def calcular_regras (self):
        self.centro_x = self.centro_x + self.vel_x
        self.centro_y = self.centro_y + self.vel_y

        if self.centro_x + self.raio > 400:
            self.vel_x = -1
        if self.centro_x - self.raio < 0:
            self.vel_x = 1
        if self.centro_y + self.raio > 300:
            self.vel_y = -1
        if self.centro_y - self.raio < 0:
            self.vel_y = 1

    # Método para desenhar o pacman
    def pintar(self, tela):
        # Desenhar o corpo
        pg.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenhar a boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x - self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x - self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pg.draw.polygon(tela, PRETO, pontos, 0)

        # Desenhar o olho
        olho_x = int(self.centro_x - self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pg.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

#################################################################################################################
# Função onde o jogo ocorre
def pacman():
    pg.init()
    #############################################################################################################
    pacman = Pacman()
    pontos = 10
    texto = "Pontos: {}".format(pontos)

    fonte = pg.font.SysFont("arial", 48, True, False)
    imagem_texto = fonte.render(texto, True, (AMARELO))

    pg.init()
    tela = pg.display.set_mode((800, 600), 0)
    jogando = True

    # loop principal do jogo
    while jogando:

        tela.blit(imagem_texto, (100, 100))
        #tela.fill(PRETO)
        #pacman.pintar(tela)
        pacman.calcular_regras()
        pg.display.update()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()


##################################################################################################################
# Função principal para iniciar o programa
if __name__ == '__main__':
    pacman()