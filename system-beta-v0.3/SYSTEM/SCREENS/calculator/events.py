from SYSTEM.SCREENS.calculator import ui
from SYSTEM.DISPLAY import renderer
def igual():
    for elmt in ui.UI:
        if elmt["action"] == "Typ":
            try:
                elmt["text"] = str(eval(elmt["text"]))
            except Exception:
                elmt["text"] = "Erro"
                
            texto_ui = elmt
        elif elmt["type"] == "rect" and elmt["action"] == "Typing":
            surfice = elmt
    renderer.render([surfice,texto_ui])
        