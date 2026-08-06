from SYSTEM.SCREENS.lantern import events
from SYSTEM.SCREENS.lantern import ui
from SYSTEM.DISPLAY import display,renderer


def switch():
    swich = ui.UI[1]
    
    display.draw_rect(swich["layout"]["pos"][0],
              swich["layout"]["pos"][1],
              swich["layout"]["size"][0]+int((len(swich["text"]) * 8)*1.25),
              swich["layout"]["size"][1])
    if swich["text"] == "ligar":
        events.ligar()
    elif swich["text"] == "desligar":
        events.desligar()
    
    swich["layout"]["size"][0] = (len(swich["text"]) * 8)
    renderer.render([swich])