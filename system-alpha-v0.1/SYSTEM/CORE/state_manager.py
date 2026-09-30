from SYSTEM.DISPLAY import renderer
from SYSTEM.SERVICES.typing import ui as typ_uis, events as typ_events

from SYSTEM.SCREENS.lock_screen import ui as lock_uis

from SYSTEM.SCREENS.lock_screen.substates.lantern import (
    ui as lantern_uis,
    pross_events as pross_event_lantern
)

from SYSTEM.SCREENS.lock_screen.substates.power import (
    ui as power_uis,
    pross_events as pross_event_power
)

from SYSTEM.SCREENS.lock_screen.substates.home import ui as home_uis

from SYSTEM.SCREENS.lock_screen.substates.home.substates.calculator import (
    ui as calculator_uis,
    pross_events as pross_event_calculator
    )

from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad import (
    ui as note_uis,
    pross_events as pross_event_notpad
    )

from SYSTEM.SCREENS.lock_screen.substates.home.substates.clock import (
    ui as clock_uis,
    pross_events as pross_event_clock
    )

from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.substates.create_not import (
    ui as create_uis,
    pross_events as pross_event_creat
    )

from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.substates.writ_txt import (
    ui as writ_uis,
    pross_events as pross_event_writ
    )

from SYSTEM.SCREENS.lock_screen.substates.home.substates.snake import (
    ui as snake_uis,
    pross_events as pross_event_snake,
    )

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
        renderer.render(self.ui,True)
    def update(self):
        pass
        
class Lantern(State):
    def __init__(self):
        self.ui = lantern_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Lantern")
    def draw(self):
        renderer.render(self.ui,True)

class Home(State):
    def __init__(self):
        self.ui = home_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Home")
    def draw(self):
        renderer.render(self.ui,True)

class Calculator(State):
    def __init__(self):
        self.ui = calculator_uis.UI
        
    def on_enter(self):
        #print(calculator_uis.UI)
        print("Entrou na tela Calculator")
    def draw(self):
        renderer.render(self.ui,True)
        
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
        
class NotePad(State):
    def __init__(self):
        self.ui = note_uis.UI
        
    def on_enter(self):
        print("Entrou na tela NotePad")
    def draw(self):
        renderer.render(self.ui,True)
        
class Create_Note(State):
    def __init__(self):
        self.ui = create_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Create")
    def draw(self):
        renderer.render(self.ui,True)

class Write_Text(State):
    def __init__(self):
        self.ui = writ_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Write")
    def draw(self):
        renderer.render(self.ui,True)
#power_uis
class Clock(State):
    def __init__(self):
        self.ui = clock_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Clock")
        pross_event_clock.updt()
    def draw(self):
        renderer.render(self.ui,True)

class Power(State):
    def __init__(self):
        self.ui = power_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Power")
        pross_event_power.load()
    def draw(self):
        renderer.render(self.ui,True)

class Snake(State):
    def __init__(self):
        self.ui = snake_uis.UI
        
    def on_enter(self):
        print("Entrou na tela Snake")
    def draw(self):
        renderer.render(self.ui,True)
        
STATE_MAP = {
    "Power" : Power,
    "Lantern": Lantern,
    "LockScreen" : LockScreen,
    "Home" : Home,
    "Calculator" : Calculator,
    "Typing" : Typing,
    "NotePad" : NotePad,
    "Create_Note" : Create_Note,
    "Write_Text" : Write_Text,
    "Clock" : Clock,
    "Snake" : Snake,
}

EVENT_MAP = {        
    "ligar" : pross_event_lantern.switch,
    "igual" : pross_event_calculator.igual,
    "apagar" : pross_event_calculator.apagar,
    "nomear" : pross_event_creat.create,
    "editar" : pross_event_notpad.editar,
    "save" : pross_event_writ.save,
    "mod_hor" : pross_event_clock.save_hors,
    "play_snake" : pross_event_snake.iniciar,
}