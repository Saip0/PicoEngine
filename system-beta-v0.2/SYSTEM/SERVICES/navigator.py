from SYSTEM.INPUT.buttons import Tc_input
from SYSTEM.DISPLAY import display
from SYSTEM.DISPLAY import renderer
    
class nav:
    def __init__(self,stat_mang,SM):
        self.Stm = stat_mang
        self.obj = 0
        self.info_obj = self.Stm.state.ui
        self.event_map = SM.EVENT_MAP
        self.state_map = SM.STATE_MAP
        self.nav_map = []
        self.tc = Tc_input()
        
        
        #self.pos_x = int(self.info_obj[self.obj]["layout"]["pos"][0] +(
        #                self.info_obj[self.obj]["layout"]["size"][0]*1.25))
        
        self.seta = [{
            "type": "image",
            "image": "seta",
            "layout": {
                "pos": [
                    int(self.info_obj[self.obj]["layout"]["pos"][0] +(
                        self.info_obj[self.obj]["layout"]["size"][0]*1.25)),
                    
                    self.info_obj[self.obj]["layout"]["pos"][1]
                ],
                "size": None
                    }
                }]
        
        
        renderer.render(self.seta)
        
    def atualizar_seta(self):
        
        item = self.info_obj[self.obj]
        self.seta[0]["layout"]["pos"] = [
            int(item["layout"]["pos"][0] + item["layout"]["size"][0] * 1.25),
            item["layout"]["pos"][1],
        ]
    def atualizar_tela(self,inpt="B"):
        
        display.draw_rect(0,0,320,240)
        
        if inpt == "A":
            self.Stm.change_state(self.state_map[self.info_obj[self.obj]["action"]]())
        else:
            self.Stm.change_state(self.state_map[self.nav_map[-1]]())
        self.info_obj = self.Stm.state.ui
            
        for elm in self.seta:
            elm["layout"]["pos"][0] = 400
            elm["layout"]["pos"][1] = 400
        self.obj = 0
        self.atualizar_seta()
        renderer.render(self.seta)
                
    def move(self):
        input_state = self.tc.read()
        if type(self.Stm.state).__name__ != "Typing":
        
            if (input_state == '2' and 
                self.obj > (len(self.info_obj)*-1)):
                try:
                    if self.info_obj[self.obj-1]["interact"]:
                        display.draw_rect(self.seta[0]["layout"]["pos"][0],self.seta[0]["layout"]["pos"][1])
                        self.obj -= 1
                        self.atualizar_seta()
                        
                except IndexError:
                    pass
                renderer.render(self.seta)
                
            elif (input_state == '8' and
                  self.obj < (len(self.info_obj)-1)):
                try:
                    if self.info_obj[self.obj+1]["interact"]:
                        display.draw_rect(self.seta[0]["layout"]["pos"][0],self.seta[0]["layout"]["pos"][1])
                        self.obj += 1
                        self.atualizar_seta()
                except IndexError:
                    pass
                
                renderer.render(self.seta)
                
            elif input_state == 'A':
                if self.info_obj[self.obj]["action"] in self.state_map:
                        
                    self.atualizar_tela(inpt="A")
                        
                elif self.info_obj[self.obj]["action"] in self.event_map:
                    display.draw_rect(self.seta[0]["layout"]["pos"][0],
                                      self.seta[0]["layout"]["pos"][1])
                    
                    self.event_map[self.info_obj[self.obj]["action"]]()
                    
                    #display.draw_rect(0,0,320,240)
                    #self.Stm.draw()
                    #self.info_obj = self.Stm.state.ui
        
                    for elm in self.seta:
                        elm["layout"]["pos"][0] = 400
                        elm["layout"]["pos"][1] = 400
                    self.obj = 0
                    self.atualizar_seta()
                    renderer.render(self.seta)
                
                if str(self.Stm.last_state) not in self.nav_map:
                         self.nav_map.append(str(self.Stm.last_state))
            
        if input_state == "B" and len(self.nav_map) > 0:
            #print("Entrando Em",self.nav_map[-1])
            self.atualizar_tela()
            self.nav_map.pop(-1)
            #print(self.nav_map)
            
            for elm in self.seta:
                    elm["layout"]["pos"][0] = 400
                    elm["layout"]["pos"][1] = 400
            self.obj = 0
            self.atualizar_seta()
            renderer.render(self.seta)
            
            
        if self.info_obj[self.obj]["type"] == "text":
            pass
            #print(str(self.info_obj[self.obj]["text"]))
        #for _ in self.info_obj:
        #    if _["type"] == "text":
        #        print(_["layout"]["size"])
        #print(str(self.Stm.last_state))     Estado anterior
        #print(str(self.info_obj[self.obj]["action"]))
        #print(str(type(self.Stm.state).__name__)) Estado atual
        #print(self.nav_map)    
