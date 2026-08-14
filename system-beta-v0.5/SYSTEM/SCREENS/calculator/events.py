from SYSTEM.SCREENS.calculator import ui
from SYSTEM.DISPLAY import renderer
def igual():
    for elmt in ui.UI:
        if elmt["action"] == "Typ":
            for txt in elmt["text"]:
                texto += txt
                print(texto)
            try:
                elmt["text"][0] = str(eval(texto))
            except Exception:
                elmt["text"][0] = "Erro"
                
            texto_ui = elmt
        elif elmt["type"] == "rect" and elmt["action"] == "Typing":
            surfice = elmt
    renderer.render([surfice,texto_ui])
        