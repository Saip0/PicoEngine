from SYSTEM.SCREENS.lantern import ui
from machine import Pin
led = Pin(14,Pin.OUT)


def ligar():
    print("ligado")
    ui.UI[1]["text"] = "desligar"
    led.on()
def desligar():
    print("desligado")
    ui.UI[1]["text"] = "ligar"
    led.off()
    