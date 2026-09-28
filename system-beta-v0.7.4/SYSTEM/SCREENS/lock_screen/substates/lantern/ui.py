from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [
    text_ui("LANTERN",
            (0,0),
            "16x32",
            interact=False),
    
        text_ui("LIGAR",
            (0,150),
            "16x32",
            action="ligar"),
]
