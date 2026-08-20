from SYSTEM.SCREENS.calculator import ui
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
                elmt["text"] = [""]
                elmt["lin"] = 0
                #print(3)
                elmt["text"][0] = str(eval(texto))
               #print(elmt["text"])
            except Exception:
                elmt["text"][0] = "Erro"
            texto_ui = elmt
            
        elif elmt["type"] == "rect" and elmt["action"] == "Typing":
            surfice = elmt
    #print(4)
    renderer.render([surfice])
    renderer.render([texto_ui],True)
        