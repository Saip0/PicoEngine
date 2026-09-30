from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [
        text_ui(text="SNAKE GAME",
            pos=(30,0),
            font="16x16",
            interact=False),
        
        text_ui(text="JOGAR",
            pos=(30,90),
            font="16x16",
            action="play_snake"),
    ]
