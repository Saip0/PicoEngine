from SYSTEM.SCREENS.lock_screen.substates.home.substates.calculator import ui
from SYSTEM.DISPLAY import renderer
from time import sleep
def igual():
    texto = ""
    for elmt in ui.UI:
        if elmt["action"] == "Typ":
            #print(elmt)
            for txt in elmt["text"]:
                #print(elmt["text"])
                #print(0)
                texto += str(txt)
            try:
                #print(1)
                print(texto)
               # elmt["text"] = [""]
               # elmt["lin"] = 0
                #print(3)
                texto = str(eval(texto))
               #print(elmt["text"])
            except Exception:
                texto = "Erro"
            texto_ui = elmt
            
        elif elmt["type"] == "rect" and elmt["action"] == "Typing":
            surfice = elmt
    #print(4)
    quart_surf = int(surfice["layout"]["size"][0] * 0.75)
    #quart_surf = int(surf * 0.75)
    text_lin = []
    chr_surf = quart_surf // 8
    size_text = len(texto)*8
    #print(texto)
    #print(quart_surf)
    #print(size_text)
    while True:
        size_text = len(texto) * 8
        
        if size_text <= quart_surf or len(text_lin)*16 > surfice["layout"]["size"][1]*0.75:
            #print("saiu")
            if len(texto) < 10:
                text_lin.append(texto)
            break
        
        elif size_text > quart_surf:
            text_lin.append(texto[:chr_surf])
            texto = texto[chr_surf:]
            
        size_text = len(texto) * 8
        #print(size_text)
        
    #print(text_lin)
    #print("Barra")
    #print(texto)
    texto_ui["text"] = text_lin
    texto_ui["lin"] = len(text_lin)-1
    texto_ui["layout"]["pos"] = [[0,i*16] for i in range(len(text_lin))]
    #print(texto_ui["lin"])
            
            
    renderer.render([surfice])
    renderer.render([texto_ui],True)

def apagar():
    UI = ui.UI
    for elmt in UI:
        if elmt["action"] == "Typ":
            #print(elmt)
            #elmt = 0
            #print(elmt)#
            UI.remove(elmt)
            #UI.pop(UI.index(elmt))
        elif elmt["type"] == "rect":
            surfice = elmt
    renderer.render([surfice])

