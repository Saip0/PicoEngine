def start():
    #from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad import events
    from libs.init import Comp_SPI0
    from SYSTEM.STORAGE import storage
    from SYSTEM.DISPLAY import display
    import os
    
    
    spi = Comp_SPI0()
    display.init(spi)
    
    #storage.init()
    
    from SYSTEM.CORE import state_manager as SM
    from SYSTEM.SERVICES import navigator
    
    from SYSTEM.SERVICES.BACKGROUND import clock,batery
    
    stat = SM.State()
    stat_mang = SM.StateManager(SM.LockScreen())
    #stat_mang = SM.StateManager(SM.Calculator())
    nav = navigator.nav(stat_mang,SM)
    
    clk = clock.Clock()
    bat = batery.Batery()
    
    while True:
        #print(events.Dados_Note)
        nav.move()
        clk.save_clock()
        bat.updt()