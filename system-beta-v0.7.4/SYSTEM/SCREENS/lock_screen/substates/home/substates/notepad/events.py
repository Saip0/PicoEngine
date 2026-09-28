from SYSTEM.DISPLAY import display as DP, txt_ui as TXU, renderer as RD
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.substates.writ_txt.ui import UI as Wr_UI
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.substates.create_not.ui import UI as Cr_UI
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.ui import UI as Note_UI
from SYSTEM.INPUT.buttons import Tc_input
from SYSTEM.SERVICES.typing import ui as Tp_UI
from SYSTEM.SERVICES import navigator as nav

Objeto = None
Dados_Note = []
def edit():
    global Objeto
    Objeto = nav.Objeto
    Init = nav.Dinamc_Init
    
    
    
    TC = Tc_input()
    texts = [
        "1(ENTRAR)",
        "2(EDITAR)",
        "3(SAIR)",
        "4(APAGAR)"
        ]
    RD.render([TXU.text_ui(text=texts[_],
            pos=(0, _*16),
            font="16x16",
            action=None) for _ in range(4)])
    #surfice = [for elmt in Wr_UI if elmt["action"]  == "Typing"]
    for elmt in Wr_UI:
        if elmt["action"] == "Typing":
            surfice = elmt
            
    print(surfice)
    global Dados_Note
    
    Nota_existente = None

    for Dados in Dados_Note:
        if Dados["ID"] == Objeto["text"]:
            Nota_existente = Dados
            break

    if Nota_existente:
        Note_txt = Nota_existente
    else:
        Note_txt = Tp_UI.text_ui(
            text=[""],
            pos=[surfice["layout"]["pos"]],
            font=surfice["font"],
            action="Typ",
            interact=False,
            cor="PRETO",
            back_cor=surfice["cor"],
            line=0,
            ID=Objeto["text"]
        )
        
    
    while True:
        inpt = TC.read()
        if inpt in ["1","2","3","4"]:
            #print("opção", inpt)
            #print(Objeto)
            DP.draw_rect(0,0,320,240)
            if inpt == "4":
                for elmt in Note_UI:
                    if elmt == Objeto:
                        Note_UI.remove(Objeto)
                for Dados in Dados_Note:
                    if Dados["ID"] == Note_txt["ID"]:
                        Dados_Note.remove(Dados)
                    
                        
            elif inpt == "1":
                Objeto = None
                #Cria Se Não Houver Nada
                if not len(Dados_Note):
                    Dados_Note.append(Note_txt)
                    Wr_UI.append(Note_txt)
                    
                else:
                    #Salva e Carrega se já existir
                    for Ui in Wr_UI:
                        #Procura pela anotação atual que está dentro de Wr_UI
                        if Ui["action"] == "Typ":
                            encontrado = False
                            #Aprós encontra-la se ela o programa salva a atualização da UI em Dados_Note
                            for Dados in Dados_Note:
                                if Dados["ID"] == Ui["ID"]:
                                    Dados_Note[Dados_Note.index(Dados)] = Ui
                                    encontrado = True
                                    #Se o ID da UI atual e da que será carregada nn bater
                                    #O programa carrega a UI nova por cima da antiga dentro de Wr_UI
                                    if Dados["ID"] != Note_txt["ID"]:     
                                        Wr_UI[Wr_UI.index(Ui)] = Note_txt
                                    break
                            #Se nn for encontrada apenas salva em Dados_Note pq provavelmen é uma UI Nova
                            if not encontrado:
                                Dados_Note.append(Note_txt)
                                Wr_UI[Wr_UI.index(Ui)] = Note_txt 
                                break
                            
                print(f"\n##UI Wr_UI##\n{Wr_UI}\n")
                print(f"\n##Dados_Note##\n{Dados_Note}\n")
                Init["Init_State"](Init["ST_MAP"]["Write_Text"]())
            elif inpt == "2":
                #print(Cr_UI)
                for Uis in Cr_UI:
                    if Uis["action"] == "Inform":
                        print(Uis)
                        Cr_UI[Cr_UI.index(Uis)]["text"] = "MODO EDITAR"
                
                titulo = [elmt for elmt in Cr_UI if elmt["action"] == "Inform"]
                Cr_UI[Cr_UI.index(titulo[0])]["text"] = "MODO EDITAR"
                
                titulo_creat = [elmt for elmt in Note_UI if elmt["action"] == "Create_Note"]
                Note_UI[Note_UI.index(titulo_creat[0])]["text"] = "EDITAR"
                Note_UI[Note_UI.index(titulo_creat[0])]["layout"]["size"] = [96,0]
                #Cr_UI.append()
                
                Init["Init_State"](Init["ST_MAP"]["Create_Note"]())
            break
        
    if inpt in ["3","4"]:
        Objeto = None
        RD.render(Note_UI)
