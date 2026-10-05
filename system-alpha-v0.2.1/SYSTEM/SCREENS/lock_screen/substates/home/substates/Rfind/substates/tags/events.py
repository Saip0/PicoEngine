from SYSTEM.SCREENS.lock_screen.substates.home.substates.Rfind.substates.tags import ui as tg_ui
import json

map_pgs = {
    "pag" : 0,
    "elmt" : 0
    }
def next_tg_pg():
    
    font_sizes = {
        "8x16": (8,16),
        "16x16": (16,16),
        "16x32": (16, 32),
    }
    
    num_tg = len(tg_ui.UI)-3
    map_pgs["elmt"] += num_tg
    #tg_ui.UI[:] = tg_ui.UI[:1]
    tg_ui.UI = [tg_ui.UI[0]]
    
    ARQUIVO = 'data/tags_13,56.json'
    
    with open(ARQUIVO, 'r') as arquivo:
       tgs_list = json.load(arquivo)
       
    tgs_list = tgs_list[map_pgs["elmt"]:]
    keys_tgs = list(tgs_list.keys())
    
    if tgs_list:
        for _,elmt in enumerate(tgs_list):
            if _ < 6:
                
                tg_ui.UI.append(
                    text_ui(text=keys_tgs[_],
                            pos=(0, tg_ui.UI[-1]["layout"]["pos"][1] + font_sizes[tg_ui.UI[-1]["font"]][1] +5),
                            font="8x16",
                            action="adit_tag")
                    )
            else:
                
                tg_ui.UI.append(
                            text_ui(text="PROXIMA_PAGINA",
                                pos=(0, tg_ui.UI[-1]["layout"]["pos"][1] + font_sizes[tg_ui.UI[-1]["font"]][1] +10),
                                font="16x16",
                                action="next_tg_pg"))
                        
                tg_ui.UI.append(
                    text_ui(text="RETORNAR_PAGINA",
                        pos=(0, tg_ui.UI[-1]["layout"]["pos"][1] + font_sizes[tg_ui.UI[-1]["font"]][1] +16),
                        font="16x16",
                        action="ret_tg_pg"))
                        
                break
            