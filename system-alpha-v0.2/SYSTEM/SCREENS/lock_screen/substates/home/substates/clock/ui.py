from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [{
        "type" : "rect",
        "cor" : "BRANCO",
        "font" : "16x16",
        "layout": {
            "pos": (130,20),
            "size": (40,120)
            },
        "action": "Typing",
        "interact": True   
        },
      text_ui(text="MOD TIME",
            pos=(130,150),
            font="16x16",
            action="mod_hor"),
      ]