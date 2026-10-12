import modulos
from modulos import init
from modulos import st7789
from modulos import vga16x32

from machine import Pin, SPI,RTC
import time
import json

tft = init.Init(2,3,4,5)
def salv_time():
    temp = time.localtime()
    with open('data/time.json','w') as json_fil:
        json.dump(list(temp),json_fil)
    
def carregar_time():
    try:
        with open('data/time.json','r') as json_fil:
            temp = json.load(json_fil)
    except:
        temp = time.localtime()
        with open('data/time.json','w') as json_fil:
            json.dump(list(temp),json_fil)
    return temp

def set_rtc_from_saved(t):
    rtc = RTC()
    rtc.datetime((
        t[0],  # year
        t[1],  # month
        t[2],  # day
        t[6],  # weekday
        t[3],  # hour
        t[4],  # minute
        t[5],  # second
        0      # subseconds
    ))
dads_sav = carregar_time()
set_rtc_from_saved(dads_sav)
tft.fill(st7789.BLACK)
while True:
    data = []
    hors = []
    tempo = time.localtime()
    for num,temp in enumerate(tempo):
        if num <= 2:
            data.append(temp)
        elif num <= 5:
            hors.append(temp)
    for num,dat in enumerate(data):
        tft.text(vga16x32,str(dat),70,num*30)
        if num == 0:
            tft.text(vga16x32,"Ano:",0,num*30)
        elif num == 1:
            tft.text(vga16x32,"Mes:",0,num*30)
        elif num == 2:
            tft.text(vga16x32,"Dia:",0,num*30)
    tft.text(vga16x32,"Horas:",0,120)
    for num,tempo in enumerate(hors):
        tft.text(vga16x32,str(tempo),num*50,150)

    salv_time()


