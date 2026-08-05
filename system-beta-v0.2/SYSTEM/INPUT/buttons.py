from time import ticks_ms, ticks_diff
class Tc_input():
    def __init__(self,PL0=6,
                 PL1=7,PL2=8,
                 PL3=9,
                 PC0=10,PC1=11,
                 PC2=12,PC3=13):
        """ """
        from machine import Pin
        self.lin = [Pin(PL0,Pin.OUT),
                    Pin(PL1,Pin.OUT),
                   Pin(PL2,Pin.OUT),
                    Pin(PL3,Pin.OUT)]
        
        self.col = [Pin(PC0,Pin.IN,Pin.PULL_DOWN),
                    Pin(PC1,Pin.IN,Pin.PULL_DOWN),
                   Pin(PC2,Pin.IN,Pin.PULL_DOWN),
                    Pin(PC3,Pin.IN,Pin.PULL_DOWN)]

        self.tc_map = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"]
        ]
        self.last_press = 0
        
    def read(self):
        tc = None
        
        for num_l, line in enumerate(self.lin):
            line.on()
            for num_c, colun in enumerate(self.col):
                if colun.value():
                    tc = self.tc_map[num_l][num_c]
                    
            line.off()
        if tc:
            agora = ticks_ms()

            if ticks_diff(agora, self.last_press) >= 500:
                self.last_press = agora
                return tc
            
        return None