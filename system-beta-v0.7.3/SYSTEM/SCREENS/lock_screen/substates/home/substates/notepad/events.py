from SYSTEM.DISPLAY import display as DP, txt_ui as TXU, renderer as RD
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.ui import UI as Note_UI
from SYSTEM.INPUT.buttons import Tc_input
from SYSTEM.SERVICES import navigator as nav
def edit():
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
    
    while True:
        inpt = TC.read()
        if inpt in ["1","2","3","4"]:
            #print("opção", inpt)
            #print(Objeto)
            if inpt == "4":
                for elmt in Note_UI:
                    if elmt == Objeto:
                        Note_UI.remove(Objeto)
            elif inpt == "2":
                #print(str(Init))
                DP.draw_rect(0,0,320,240)
                Init["Init_State"](Init["ST_MAP"]["Create_Note"]())
            break
        
    if inpt in ["3","4"]:
        DP.draw_rect(0,0,320,240)
        RD.render(Note_UI)
