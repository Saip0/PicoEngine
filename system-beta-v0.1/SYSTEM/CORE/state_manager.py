from SYSTEM.DISPLAY import renderer
from SYSTEM.SERVICES.typing import ui as typ_uis, events as typ_events

from SYSTEM.SCREENS.lock_screen import ui as lock_uis
from SYSTEM.SCREENS.lantern import ui as lantern_uis,pross_events as pross_event_lantern
from SYSTEM.SCREENS.home import ui as home_uis
from SYSTEM.SCREENS.calculator import ui as calculator_uis

class State:
    def on_enter(self):
        pass
    def on_exit(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
        
class StateManager:
    def __init__(self, initial_state):
        
        self.state = None
        self.last_state = None
        self.change_state(initial_state)
    def change_state(self,new_state):
        global last_state_ui
        if self.state != None:
            self.last_state = type(self.state).__name__
        self.state = new_state 
        self.state.ui
        last_state_ui = self.state.ui
        self.state.on_enter()
        self.state.draw()
        
    def update(self):
        self.state.update()
        
    def draw(self):
        self.state.draw()

class LockScreen(State):
    def __init__(self):
        self.ui = lock_uis.UI
    def on_enter(self):
        print("Entrou na tela LockScreen")
        
    def draw(self):
        renderer.render(self.ui)
    def update(self):
        pass
        
class Lantern(State):
    def __init__(self):
        self.ui = lantern_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Lantern")
    def draw(self):
        renderer.render(self.ui)

class Home(State):
    def __init__(self):
        self.ui = home_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Home")
    def draw(self):
        renderer.render(self.ui)

class Calculator(State):
    def __init__(self):
        self.ui = calculator_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Calculator")
    def draw(self):
        renderer.render(self.ui)
        
class Typing(State):
    def __init__(self):
        global last_state_ui
        self.Typ = typ_events.Typ(last_state_ui)
        self.ui = typ_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Typing")
    def draw(self):
        renderer.render(self.ui)
        self.Typ.loop()
        
STATE_MAP = {
    "Lantern": Lantern,
    "LockScreen" : LockScreen,
    "Home" : Home,
    "Calculator" : Calculator,
    "Typing" : Typing,
}

EVENT_MAP = {
    "unlock": "unlock",
    "power": "power",        
    "ligar": pross_event_lantern.switch,
}