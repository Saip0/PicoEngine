from SYSTEM.SCREENS.lock_screen.substates.lantern import events
from SYSTEM.SCREENS.lock_screen.substates.lantern import ui
from SYSTEM.DISPLAY import display,renderer


def switch():
    swich = ui.UI[1]
    
    display.draw_rect(swich["layout"]["pos"][0],
              swich["layout"]["pos"][1],
              swich["layout"]["size"][0]+int((len(swich["text"]) * 16)*1.25),
              swich["layout"]["size"][1])
    if swich["text"] == "LIGAR":
        events.ligar()
    elif swich["text"] == "DESLIGAR":
        events.desligar()
    
    swich["layout"]["size"][0] = (len(swich["text"]) * 16)
    renderer.render([swich])
