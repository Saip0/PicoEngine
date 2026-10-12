from SYSTEM.SCREENS.lock_screen.substates.home.substates.Rfind.substates.tags import ui as tg_ui
from SYSTEM.DISPLAY.renderer import render as RD
from SYSTEM.SERVICES import navigator as nav
from SYSTEM.DISPLAY.txt_ui import text_ui
from SYSTEM.INPUT.buttons import Tc_input
from SYSTEM.DISPLAY import display
import json

map_pgs = {
    "pag" : 0,
    "elmts" : 0,
    "obj" : None
    }
def next_tg_pg():
    font_sizes = {
        "8x16": (8, 16),
        "16x16": (16, 16),
        "16x32": (16, 32),
    }

    ARQUIVO = 'data/tags_13,56.json'

    with open(ARQUIVO, 'r') as arquivo:
        tgs_list = json.load(arquivo)

    keys_tgs = list(tgs_list.keys())
    
    if len(keys_tgs) > map_pgs["elmts"] + 5:

        # Avança 5 tags
        map_pgs["elmt"] += 5

        # Mantém somente o primeiro elemento da UI
        tg_ui.UI[:] = tg_ui.UI[:3]

        # Próximas 5 tags
        page_tags = keys_tgs[map_pgs["elmts"]:map_pgs["elmts"] + 5]
        
        #print(tg_ui.UI)
        
        for elmt in page_tags:
            #print(tg_ui.UI[-1]["font"])
            tg_ui.UI.append(
                text_ui(
                    text=elmt,
                    pos=(
                        0,
                        tg_ui.UI[-1]["layout"]["pos"][1] +
                        font_sizes[tg_ui.UI[-1]["font"]][1] + 14
                        ), 
                    font="8x16",
                    action="adit_tag"
                )
            )
                    
        display.draw_rect(0,0,320,240)
       # print()
       # print("Após")
        RD(tg_ui.UI,True)
        #print(tg_ui.UI)
            
def ret_tg_pg():
    
    font_sizes = {
        "8x16": (8, 16),
        "16x16": (16, 16),
        "16x32": (16, 32),
    }

    ARQUIVO = 'data/tags_13,56.json'

    with open(ARQUIVO, 'r') as arquivo:
        tgs_list = json.load(arquivo)

    keys_tgs = list(tgs_list.keys())
    
    if map_pgs["elmts"] > 0:

        # Retorna 5 tags
        map_pgs["elmts"] -= 5

        # Mantém somente o primeiro elemento da UI
        tg_ui.UI[:] = tg_ui.UI[:3]

        # 5 Tags Anteriores
        page_tags = keys_tgs[map_pgs["elmts"]:map_pgs["elmts"]+5]
        
        print(tg_ui.UI)
        
        for elmt in page_tags:
            #print(tg_ui.UI[-1]["font"])
            tg_ui.UI.append(
                text_ui(
                    text=elmt,
                    pos=(
                        0,
                        tg_ui.UI[-1]["layout"]["pos"][1] +
                        font_sizes[tg_ui.UI[-1]["font"]][1] + 14
                        ), 
                    font="8x16",
                    action="adit_tag"
                )
            )
                    
        display.draw_rect(0,0,320,240)
        print()
        print("Após")
        RD(tg_ui.UI,True)
        print(tg_ui.UI)
        
def iniciar():
    font_sizes = {
        "8x16": (8, 16),
        "16x16": (16, 16),
        "16x32": (16, 32),
    }

    ARQUIVO = 'data/tags_13,56.json'
    
    if len(tg_ui.UI) < 4:
        try:
            with open(ARQUIVO, 'r') as arquivo:
                tgs_list = json.load(arquivo)

            keys_tgs = list(tgs_list.keys())
            keys_tgs = keys_tgs[:5]
        except:
            tgs_list = {}
            with open(ARQUIVO, 'w') as arquivo:
                    json.dump(tgs_list, arquivo)
            keys_tgs = list(tgs_list.keys())
            keys_tgs = keys_tgs[:5]
        
        for elmt in keys_tgs:
            tg_ui.UI.append(
                text_ui(
                    text=elmt,
                    pos=(
                        0,
                        tg_ui.UI[-1]["layout"]["pos"][1] +
                        font_sizes[tg_ui.UI[-1]["font"]][1] + 14
                        ), 
                    font="8x16",
                    action="adit_tag"
                )
            )
            
            
def option():

    map_pgs["obj"] = None
    #global map_pgs
    map_pgs["obj"] = nav.Objeto
    Init = nav.Dinamc_Init
    
    ARQUIVO = 'data/tags_13,56.json'
    TC = Tc_input()
    display.draw_rect(0,0,320,240)
    texts = [
        "1(ENTRAR)",
        "2(EDITAR)",
        "3(SAIR)",
        "4(APAGAR)"
        ]
    msg = [
        "APOS CONFIRMAR",
        "NAO PODERA",
        "RECUPERAR OQUE",
        "APAGOU TEM",
        "CERTEZA QUE",
        "DESEJA APAGAR O",
        "ITEM A SEGUIR?",
        "(A) SIM (B) NAO"]
    
    RD([text_ui(text=texts[_],
            pos=(0, _*16),
            font="16x16",
            action=None) for _ in range(4)])
    
    with open(ARQUIVO, 'r') as arquivo:
            tgs_list = json.load(arquivo)

        #keys_tgs = list(tgs_list.keys())
    
    while True:
        inpt = TC.read()
        
        if inpt in ["1","2","3","4"]:
            if inpt == "4":
                display.draw_rect(0,0,320,240)
                RD([text_ui(text=msg[_],
                        pos=(0,_*16),
                        font="16x16",
                        action=None) for _ in range(8)])
                while  True:
                    inpt = TC.read()
                    if inpt in ["OK","RET"]:
                        break
                    
                if inpt == "OK": 
                    tgs_list.pop(map_pgs["obj"]["text"])
                    tg_ui.UI.remove(map_pgs["obj"])
                
                    with open(ARQUIVO, 'w') as arquivo:
                        json.dump(tgs_list, arquivo)
            break
        
    display.draw_rect(0,0,320,240)
    RD(tg_ui.UI,True)