def start():
    #from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad import events
    from SYSTEM.STORAGE import storage
    from SYSTEM.DISPLAY import display
    import os 
    display.init()
    #storage.init()
    
    from SYSTEM.CORE import state_manager as SM
    from SYSTEM.SERVICES import navigator
    
    from SYSTEM.SERVICES.BACKGROUND import clock
    
    stat = SM.State()
    stat_mang = SM.StateManager(SM.LockScreen())
    #stat_mang = SM.StateManager(SM.Calculator())
    nav = navigator.nav(stat_mang,SM)
    
    clk = clock.Clock()
    
    while True:
        #print(events.Dados_Note)
        nav.move()
        clk.save_clock()