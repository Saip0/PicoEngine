from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [
        text_ui(text="TAGS",
            pos=(0, 0),
            font="16x32",
            action=None,
            interact=False),
        
        text_ui(text="PROXIMA_PAGINA",
            pos=(0, 38),
            font="16x16",
            action="next_tg_pg"),
    
    text_ui(text="RETORNAR_PAGINA",
            pos=(0,54),
            font="16x16",
            action="ret_tg_pg")
    ]