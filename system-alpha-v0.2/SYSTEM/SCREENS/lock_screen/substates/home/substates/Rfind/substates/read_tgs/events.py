from SYSTEM.SCREENS.lock_screen.substates.home.substates.Rfind.substates.read_tgs import ui
from SYSTEM.DISPLAY.renderer import render as RD
from SYSTEM.DISPLAY.txt_ui import text_ui
from SYSTEM.INPUT.buttons import Tc_input
from libs.init import Comp_SPI0
from time import sleep

def read_tg():
    
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
                
                sleep(0.25)

        comp.deselect_all()
        sleep(0.1)

