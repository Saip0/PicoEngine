tela = None
from libs import Init,cores
from libs.fontes import vga8x16, vga16x16, vga16x32

fontes = {
    "8x16" : vga8x16,
    "16x16" : vga16x16,
    "16x32" : vga16x32,
    }
color = {
    "PRETO" : cores.PRETO,
    "BRANCO" : cores.BRANCO,
    "AZUL" : cores.AZUL,
    }

def init():
    global tela
    tela = Init.l94_init(2,3,4,5,1)
    
def draw_rect(pos_x,pos_y,larg=32,alt=32,cor="PRETO"):
    
    tela.fill_vrect(
        pos_x,
        pos_y,
        larg,
        alt,
        color[cor])
    
def draw_text(pos_x=0,pos_y=0,text="Ola Mundo",font=fontes["8x16"],leter_cor="BRANCO",back_cor="PRETO"):
    
    tela.draw_text(
                pos_x,
                pos_y,
                text,
                fontes[font],
                color[leter_cor],
                color[back_cor],
            )
    