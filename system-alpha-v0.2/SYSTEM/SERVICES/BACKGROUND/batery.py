from SYSTEM.SCREENS.lock_screen.substates.power.ui import UI
from SYSTEM.DISPLAY.txt_ui import text_ui
from machine import ADC
import time


class Batery:

    def __init__(self):

        # GP26 = ADC0 = pino físico 31
        self.adc = ADC(26)

        # Divisor de tensão: 10k + 10k
        self.DIVISOR = 2.0

        # Referência aproximada do ADC
        self.ADC_REF = 3.3

    def ler_bateria(self):

        total = 0

        # Faz várias leituras para estabilizar
        for _ in range(20):
            total += self.adc.read_u16()
            time.sleep_ms(5)

        leitura = total / 20

        # Tensão no ADC
        tensao_adc = (leitura / 65535) * self.ADC_REF

        # Recupera tensão real da bateria
        tensao_bateria = tensao_adc * self.DIVISOR

        return tensao_bateria

    def calcular_porcentagem(self, tensao):

        if tensao >= 4.20:
            return 100

        elif tensao >= 4.00:
            return 80 + (tensao - 4.00) / 0.20 * 20

        elif tensao >= 3.85:
            return 60 + (tensao - 3.85) / 0.15 * 20

        elif tensao >= 3.70:
            return 40 + (tensao - 3.70) / 0.15 * 20

        elif tensao >= 3.50:
            return 20 + (tensao - 3.50) / 0.20 * 20

        elif tensao >= 3.20:
            return 5 + (tensao - 3.20) / 0.30 * 15

        else:
            return 0

    def updt(self):

        tensao = self.ler_bateria()
        porcentagem = self.calcular_porcentagem(tensao)

        # Limita entre 0 e 100
        porcentagem = max(0, min(100, porcentagem))

        # --------------------------------
        # SUBSTITUI AS UIS
        # --------------------------------
        #print(UI)
        
        UI[0] = text_ui(
            text="BATERIA: {:.2f}V".format(tensao),
            pos=(0, 0),
            font="16x32",
            interact=None,
            action=None
        )

        UI[1] = text_ui(
            text="CARGA: {:.0f}%".format(porcentagem),
            pos=(0, 88),
            font="16x32",
            interact=None,
            action=None
        )