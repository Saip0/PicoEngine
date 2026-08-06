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

        self.tc_maps = [
            #Num----------------------
            [
                [
                    ["1", "2", "3", "OK"],
                    ["4", "5", "6", "RET"],
                    ["7", "8", "9", "DEL"],
                    ["Map", "0", "Pag", ""]
                ],
                [
                    ["+", "-", "*", "OK"],
                    ["/", "%", "//", "RET"],
                    ["**", "(", ")", "DEL"],
                    ["Map", "", "Pag", ""]
                ]
            ],
            #Alfa-----------------
            [
                [
                    ["A", "B", "C", "OK"],
                    ["D", "E", "F", "RET"],
                    ["G", "H", "I", "DEL"],
                    ["Map", "J", "Pag", ""]
                ],
                [
                    ["K", "L", "M", "OK"],
                    ["N", "O", "P", "RET"],
                    ["Q", "R", "S", "DEL"],
                    ["Map", "T", "Pag", ""]
                ],
                [
                    ["U", "V", "W", "OK"],
                    ["X", "Y", "Z", "RET"],
                    ["", "", "", "DEL"],
                    ["Map", "", "Pag", ""]
                ]
            ]
        ]
        self.last_press = 0
        
    def read(self,Map=0,Pag=0):
        tc = None
        
        for num_l, line in enumerate(self.lin):
            line.on()
            for num_c, colun in enumerate(self.col):
                if colun.value():
                    tc = self.tc_maps[Map][Pag][num_l][num_c]
                    
            line.off()
        if tc:
            agora = ticks_ms()

            if ticks_diff(agora, self.last_press) >= 50:
                self.last_press = agora
                return tc
            
        return None