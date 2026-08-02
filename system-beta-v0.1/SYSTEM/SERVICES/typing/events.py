from SYSTEM.SERVICES.typing import ui as t_ui
from SYSTEM.INPUT import buttons as but
from SYSTEM.DISPLAY import renderer
class Typ:
    def __init__(self,ui):
        #print(t_ui.UI)
        #print(len(t_ui.UI))
        #print(t_ui.UI[0])
        #print(t_ui.UI)
        
        self.tc = but.Tc_input()
        t_ui.UI = ui
        self.texto = ""
        if len(t_ui.UI) > 0:
            for elmt in t_ui.UI:
                #print(elmt["type"])
                if elmt["type"] == "rect":
                    self.surfice = elmt
                    self.posit = elmt["layout"]["pos"]
                    
            self.txt_ui = t_ui.text_ui(text=self.texto,pos=self.posit, font="8x16",
                                  action=None, interact=False,cor="PRETO",back_cor="BRANCO")
            
            t_ui.UI.append(self.txt_ui)
            
        
    def escrever(self,tc_state):
        #print(tc_state, tc_state)
        if (tc_state not in ["A","C","D","*","#",None] and
            self.txt_ui["layout"]["size"][0] < self.surfice["layout"]["pos"][0]+(
                self.surfice["layout"]["size"][0])*0.75):
            self.texto += tc_state
            #self.txt_ui["text"] += tc_state
        #print(self.txt_ui["text"])
        #print(self.txt_ui["text"])
                
    def loop(self):
        while True:
            tc_state = self.tc.read()
            if tc_state == "B":
                break 
            self.escrever(tc_state)
            self.txt_ui = t_ui.text_ui(text=self.texto,pos=self.posit, font="8x16",
                                  action=None, interact=False,cor="PRETO",back_cor="BRANCO")
            
            print(self.surfice["layout"]["pos"][0]+(self.surfice["layout"]["size"][0]))
            print(self.txt_ui["layout"]["size"][0])
            renderer.render([self.txt_ui])
                
        



#print("indefinido")
#expressao = "2 + 3 * (4 ** 2)"
#resultado = eval(expressao)
#print(resultado)

#mandar a UI de texto para a UI do estado anterior
#e criar uma ação para que possa ser identificado
#a UI q pode ser escrita
#por exemplo, após o fechamento do Typ, ele salva a UI de texto na UI do estado anterior
#após isso o Typ vai analisar se existe uma UI que ele ja escreveu usando a chave action
#e se tiver ele apenas reultiliza ela, mas se não, ele cria uma outra do 0