from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.substates.create_not.ui import UI as Cr_UI
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.ui import UI as Note_UI
from SYSTEM.DISPLAY import renderer as Rd, txt_ui as TXU
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad import events
def criar():
    Objeto = events.Objeto
    print(Objeto)
    #Objeto = None
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
        elif elmt["action"] == "Inform":
            titulo = elmt
    titulo_criar = [elmt for elmt in Note_UI if elmt["action"] == "Create_Note"]
            
    if len(text["text"][0].strip()) < 3 or text["text"][0] in ["INVALIDO","JA EXISTE"]:
        text["text"] = ["INVALIDO"]
        Rd.render([surf,text], al=True)
        
    elif text["text"][0] in [elmt["text"] for elmt in Note_UI if elmt != Objeto]:
        text["text"] = ["JA EXISTE"]
        Rd.render([surf,text], al=True)
        
    else:
        if Objeto == None:
            #print(Ult_elmt["layout"]["pos"][1]+font_sizes[font][1])
            
            Nv_Bloc = TXU.text_ui(text=text["text"][0],
                pos=(0, Ult_elmt["layout"]["pos"][1]+font_sizes[font][1]),
                font=font,
                action="editar")
            
            Note_UI.append(Nv_Bloc)
        else:
            if len(events.Dados_Note):
                    for Dados in events.Dados_Note:
                        if Dados["ID"] == Objeto["text"]:
                            print(f"Antigo ID Note\n\n {events.Dados_Note[events.Dados_Note.index(Dados)]["ID"]}"
                                  f"\n Novo ID Note \n\n {text["text"][0]}")
                            events.Dados_Note[events.Dados_Note.index(Dados)]["ID"] = text["text"][0]
                            
            for elmt in Note_UI:
                if elmt == Objeto:
                    Itm = Note_UI[Note_UI.index(elmt)]
                    Itm["text"] = text["text"][0]
                    Itm["layout"]["size"][0] = len(text["text"][0])*font_sizes[font][0]
                          
            #print(len(text["text"])*font_sizes[font][0])
            events.Objeto = None
            Cr_UI[Cr_UI.index(titulo)]["text"] = "MODO CRIAR"
            Note_UI[Note_UI.index(titulo_criar[0])]["text"] = "CRIAR"
            print(f"##ITEM ATUALIZADO \n{Itm}\n\n\n ###Dados_Note Atualizados{events.Dados_Note}")
            
            
