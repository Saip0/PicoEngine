from SYSTEM.SCREENS.lock_screen.substates.home.substates.Rfind.substates.tags import events

def load_pg():
    events.next_tg_pg()
    
def pos_pg():
    events.ret_tg_pg()
    
def load_tgs():
    events.iniciar()
    
def adit_tag():
    events.option()