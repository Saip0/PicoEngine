from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [
        {
        "type" : "rect",
        "cor" : "BRANCO",
        "font" : "16x16",
        "layout": {
            "pos": (0,35),
            "size": (200,190)
            },
        "action": "Typing",
        "interact": True
        },
         text_ui(text="Pag1",
            pos=(200, 176),
            font="16x16",
            action="next_pg"),
        ]