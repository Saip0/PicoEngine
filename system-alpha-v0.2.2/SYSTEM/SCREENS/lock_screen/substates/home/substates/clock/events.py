from SYSTEM.DISPLAY.renderer import render
from SYSTEM.DISPLAY import display
from SYSTEM.SCREENS.lock_screen.substates.home.substates.clock import ui
from SYSTEM.SERVICES.BACKGROUND import clock
from SYSTEM.INPUT.buttons import Tc_input
from time import sleep

def atualizar():
    clk = clock.Clock()
    tc = Tc_input()
    display.draw_rect(48,105,64,32)
    
    while True:
        inpt = tc.read()
        if inpt == "RET":
            print("Saiu")
            display.draw_rect(0,0,320,240)
            sleep(1)
            break
        
        render([ui.UI[_] for _ in range(3,8)],True)
            
        clk.save_clock()

def mod_hor():
    for Uis in ui.UI:
        if Uis["action"] == "Typ":
            txt_ui = Uis
    
    txt_ui["text"].pop(-1)

    print(txt_ui)

    mods_list = len(txt_ui["text"])

    for i, elmt in enumerate(txt_ui["text"]):
        txt_ui["text"][i] = elmt.replace("/", "")

    if mods_list > 3:
        if all(txt_ui["text"][i].isdigit() for i in range(4)):

            if 0 < int(txt_ui["text"][0]) <= 12:
                mes = txt_ui["text"][0]

            if 0 < int(txt_ui["text"][1]) <= 31:
                dia = txt_ui["text"][1]

            if 0 <= int(txt_ui["text"][2]) <= 23:
                hora = txt_ui["text"][2]

            if 0 <= int(txt_ui["text"][3]) <= 59:
                minut = txt_ui["text"][3]
            
            clk = clock.Clock()      
            clk.set_time(mes, dia, hora, minut)
            ui.UI.remove(txt_ui)
            
    