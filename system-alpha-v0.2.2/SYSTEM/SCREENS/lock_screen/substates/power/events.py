from SYSTEM.SERVICES.BACKGROUND import batery
from SYSTEM.INPUT.buttons import Tc_input
from SYSTEM.DISPLAY import renderer as RDR, display
from SYSTEM.SCREENS.lock_screen.substates.power import ui

def loop():
    bat = batery.Batery()
    tc = Tc_input()
    while True:
        inpt = tc.read()
        RDR.render(ui.UI,True)
        bat.updt()
        if inpt == "RET":
            display.draw_rect(0,0,320,240)
            break