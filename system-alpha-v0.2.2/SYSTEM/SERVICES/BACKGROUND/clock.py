from SYSTEM.SCREENS.lock_screen.substates.home.substates.clock import ui
from SYSTEM.DISPLAY.txt_ui import text_ui
from machine import RTC
import time
import json

t  = [0 for _ in range (6)]

class Clock:

    def __init__(self):
        global t
        self.last_save = time.ticks_ms()
        self.ARQUIVO = 'data/time.json'
        
        self.infor = [
            "An",
            "Mes",
            "Dia",
            "Hor",
            "Min",
            "Sec"]

        try:
            with open(self.ARQUIVO, 'r') as arquivo:
                t = json.load(arquivo)

            # Restaura o RTC com o último horário salvo
            RTC().datetime((
                t[0],  # ano
                t[1],  # mês
                t[2],  # dia
                t[6],  # weekday
                t[3],  # hora
                t[4],  # minuto
                t[5],  # segundo
                0
            ))

        except:
            # Não existe horário salvo
            t = time.localtime()

            # Salva o horário inicial
            with open(self.ARQUIVO, 'w') as arquivo:
                json.dump(list(t), arquivo)
        
        ui.UI += [
                text_ui(
                    text=f"{self.infor[_]} {t[_]}",
                    pos=(0, _ * 35),
                    font="16x32",
                    interact=False
                )
                for _ in range(6)
            ]
        #print(ui.UI)
        
    def set_time(self, mes=None, dia=None, hora=None, minuto=None):
        global t

        if mes is not None:
            t[1] = int(mes)

        if dia is not None:
            t[2] = int(dia)

        if hora is not None:
            t[3] = int(hora)

        if minuto is not None:
            t[4] = int(minuto)

        RTC().datetime((
            t[0],  # ano
            t[1],  # mês
            t[2],  # dia
            t[6],  # weekday
            t[3],  # hora
            t[4],  # minuto
            t[5],  # segundo
            0
        ))
        
        t = time.localtime()
        
        with open(self.ARQUIVO, 'w') as arquivo:
            json.dump(list(t), arquivo)
    

    def save_clock(self):
        global t

        t = time.localtime()

        #print(t)

        agora = time.ticks_ms()

        if time.ticks_diff(agora, self.last_save) >= 60000:
            self.last_save = agora

            with open(self.ARQUIVO, 'w') as arquivo:
                json.dump(list(t), arquivo)

        for _ in range(6):
            #print(ui.UI[_+2])
            ui.UI[_+2]["text"] = f"{self.infor[_]}:{t[_]}"
            
