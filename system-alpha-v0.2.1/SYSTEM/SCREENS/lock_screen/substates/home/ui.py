from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [
        text_ui(text="CALCULADORA",
            pos=(0, 0),
            font="16x16",
            action="Calculator"),

        
    text_ui(text="BLOCO",
            pos=(0,30),
            font="16x16",
            action="NotePad"),
        
        text_ui(text="RELOGIO",
            pos=(0,60),
            font="16x16",
            action="Clock"),
        
        text_ui(text="SNAKE_GAME",
            pos=(0,90),
            font="16x16",
            action="Snake"),
        
        text_ui(text="RF_13,56MHZ",
            pos=(0,120),
            font="16x16",
            action="Rfind"),
        
        text_ui(text="IR_38KHZ",
            pos=(0,150),
            font="16x16",
            action="IR"),
        
        text_ui(text="NFC_2,4GHZ",
            pos=(0,180),
            font="16x16",
            action="NFC"),
    ]
