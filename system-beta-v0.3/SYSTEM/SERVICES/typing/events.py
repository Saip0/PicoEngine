from SYSTEM.SERVICES.typing import ui as t_ui
from SYSTEM.INPUT import buttons as but
from SYSTEM.DISPLAY import renderer
class Typ:
    def __init__(self,ui):
        #print(t_ui.UI)
        #print(len(t_ui.UI))
        #print(t_ui.UI[0])
        #print(t_ui.UI)
        self.ui = ui
        self.tc = but.Tc_input()
        self.tc_map = self.tc.tc_maps
        self.Map = 0
        self.Pag = 0
        t_ui.UI = ui
        txt = False
        if len(t_ui.UI) > 0:
            for elmt in t_ui.UI:
                if elmt["type"] == "text" and elmt["action"] == "Typ":
                    self.txt_ui = elmt
                    self.texto = elmt["text"]
                    self.posit = elmt["layout"]["pos"]
                    txt = True
                elif elmt["type"] == "rect":
                    self.surfice = elmt
            for elmt in t_ui.UI:
                if elmt["type"] == "rect" and not txt:
                    self.texto = ""
                    #print(elmt["type"])
                    self.surfice = elmt
                    self.posit = elmt["layout"]["pos"]
                    self.txt_ui = t_ui.text_ui(text=self.texto,pos=self.posit, font="8x16",
                            action="Typ", interact=False,cor="PRETO",back_cor=elmt["cor"])
            if not self.txt_ui in t_ui.UI:
                t_ui.UI.append(self.txt_ui)
            
        
    def escrever(self,tc_state):
        #print(tc_state, tc_state)
        if (tc_state not in ["OK","RET","DEL","","Map","Pag",None] and
            self.txt_ui["layout"]["size"][0] < self.surfice["layout"]["pos"][0]+(
                self.surfice["layout"]["size"][0])*0.75):
            self.texto += tc_state
            #self.txt_ui["text"] += tc_state
        #print(self.txt_ui["text"])
        #print(self.txt_ui["text"])
            
    def apagar(self,tc_state):
        if tc_state == "DEL" and len(self.texto) > 0:
            self.texto = self.texto[:-1]
            renderer.render([self.surfice])
            
    def gerenciar_map(self,tc_state):
        if tc_state == "Map":
            if self.Map < len(self.tc_map)-1:
                self.Map += 1
            else:
                self.Map = 0
                
        elif tc_state == "Pag":
            if self.Pag < len(self.tc_map[0])-1:
                self.Pag += 1
            else:
                self.Pag = 0
            
            
    def loop(self):
        while True:
            tc_state = self.tc.read(Map=self.Map,Pag=self.Pag)
            if tc_state == "RET":
                self.Map = 0
                self.Pag = 0
                return self.ui.append(self.txt_ui)
                break
            
            self.tc_map = self.tc.tc_maps
            self.escrever(tc_state)
            self.apagar(tc_state)
            self.gerenciar_map(tc_state)
            self.txt_ui = t_ui.text_ui(text=self.texto,pos=self.posit, font="8x16",
                                  action="Typ", interact=False,cor="PRETO",back_cor="BRANCO")
            
            #print(self.surfice["layout"]["pos"][0]+(self.surfice["layout"]["size"][0]))
            #print(self.txt_ui["layout"]["size"][0])
            #print(self.txt_ui["text"])
            renderer.render([self.txt_ui])
            #print(self.Pag)