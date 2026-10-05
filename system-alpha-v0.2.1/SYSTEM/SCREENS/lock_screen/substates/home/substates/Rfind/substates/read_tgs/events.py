from SYSTEM.SCREENS.lock_screen.substates.home.substates.Rfind.substates.read_tgs import ui
from SYSTEM.SCREENS.lock_screen.substates.home.substates.Rfind.substates.tags import ui as tg_ui
from SYSTEM.DISPLAY.renderer import render as RD
from SYSTEM.DISPLAY.txt_ui import text_ui
from SYSTEM.INPUT.buttons import Tc_input
from libs.init import Comp_SPI0
from time import sleep
import json

def read_tg():
    
    font_sizes = {
        "8x16": (8,16),
        "16x16": (16,16),
        "16x32": (16, 32),
    }
    
    
    comp = Comp_SPI0()

    tela = comp.l94_init()
    rfid = comp.mfrc522_init()
    
    delet = {
        "type" : "rect",
        "cor" : "PRETO",
        "layout": {
            "pos": (10,95),
            "size": (250,30)
            },
        "action": None ,
        "interact": False
        }
    
    tag = text_ui(text="",
            pos=(10, 95),
            font="8x16",
            action=None,
            interact=False)
    
    RD(ui.UI, True)
    Tc = Tc_input()
    
    ARQUIVO = 'data/tags_13,56.json'
    
    try:
            with open(ARQUIVO, 'r') as arquivo:
               tgs_list = json.load(arquivo)
               
    except:
        tgs_list = {}
        with open(ARQUIVO, 'w') as arquivo:
                json.dump(tgs_list, arquivo)
    
    while True:
        
        if Tc.read() == "RET":
            break
        
        comp.cs_rfid()

        status, _ = rfid.request(rfid.REQIDL)

        if status == rfid.OK:

            status, uid = rfid.anticoll()

            if status == rfid.OK:

              #  uid_texto = ":".join(
              #      "{:02X}".format(byte)
               #     for byte in uid
                #)

                comp.cs_tft()
                #print(uid)
                
                tag["text"] = str(uid)
                
                RD([delet,tag], True)
                
                tag_uid = text_ui(text=str(uid),
                            pos=(0, tg_ui.UI[-1]["layout"]["pos"][1] + font_sizes[tg_ui.UI[-1]["font"]][1] +5),
                            font="8x16",
                            action="adit_tag")
                
                if not any(tag_uid["text"] == elmt["text"] for elmt in tg_ui.UI):
                    pass
                    
                    #tgs_list[str(uid)] = uid
                        
                    #with open(ARQUIVO, 'w') as arquivo:
                     #   json.dump(tgs_list, arquivo)
                
                if len(tg_ui.UI) > 6:
                    if not any("Proxima_Pagina" and "RETORNAR_PAGINA" == elmt["text"] for elmt in tg_ui.UI):
                        
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
                    
                else:
                    if not any(tag_uid["text"] == elmt["text"] for elmt in tg_ui.UI):
                        
                        tg_ui.UI.append(tag_uid)
                
                sleep(0.25)

        comp.deselect_all()
        sleep(0.1)

