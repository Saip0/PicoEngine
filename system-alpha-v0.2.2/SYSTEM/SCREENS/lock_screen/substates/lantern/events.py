from SYSTEM.SCREENS.lock_screen.substates.lantern import ui
from machine import Pin
led = Pin(22,Pin.OUT)


def ligar():
    print("ligado")
    ui.UI[1]["text"] = "DESLIGAR"
    led.on()
def desligar():
    print("desligado")
    ui.UI[1]["text"] = "LIGAR"
    led.off()
    
