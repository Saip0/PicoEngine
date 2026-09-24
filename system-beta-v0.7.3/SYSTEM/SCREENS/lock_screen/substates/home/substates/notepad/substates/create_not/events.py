from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.substates.create_not.ui import UI as Cr_UI
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.ui import UI as Note_UI
from SYSTEM.DISPLAY import renderer as Rd, txt_ui as TXU
from time import sleep
def criar():
    Ult_elmt = Note_UI[-1]
    font_sizes = {
        "8x16": (8,16),
        "16x16": (16,16),
        "16x32": (16, 32),
    }
    font = "16x16"
    #print(Ult_elmt["layout"]["pos"][1]+font_sizes[font][1])
    for elmt in Cr_UI:
        if elmt["action"] == "Typ":
            text = elmt
            #print(type(elmt["text"]))
            #print(len(text["text"][0].strip()))
            #print(elmt)
        elif elmt["action"] == "Typing":
            surf = elmt
            #print(surf)
        
            
    if len(text["text"][0].strip()) < 3 or text["text"][0] in ["INVALIDO","JA EXISTE"]:
        text["text"] = ["INVALIDO"]
        Rd.render([surf,text], al=True)
        
    elif text["text"][0] in [elmt["text"] for elmt in Note_UI]:
        text["text"] = ["JA EXISTE"]
        Rd.render([surf,text], al=True)
        
    else:
        #print(Ult_elmt["layout"]["pos"][1]+font_sizes[font][1])
        
        Nv_Bloc = TXU.text_ui(text=text["text"][0],
            pos=(0, Ult_elmt["layout"]["pos"][1]+font_sizes[font][1]),
            font=font,
            action="editar")
        
        Note_UI.append(Nv_Bloc)