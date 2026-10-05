from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [
    
        {
        "type" : "rect",
        "cor" : "BRANCO",
        "font" : "16x16",
        "layout": {
            "pos": (0,0),
            "size": (225,176)
            },
        "action": "Typing",
        "interact": True
        },
        
        text_ui(text="=",
            pos=(0, 176),
            font="16x32",
            action="igual"),
        
        text_ui(text="DEL",
            pos=(161, 176),
            font="16x32",
            action="apagar"),

    ]

