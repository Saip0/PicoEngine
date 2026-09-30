from SYSTEM.DISPLAY.txt_ui import text_ui

UI = [{
        "type" : "rect",
        "cor" : "BRANCO",
        "font" : "16x32",
        "layout": {
            "pos": (40,40),
            "size": (200,60)
            },
        "action": "Typing",
        "interact": True   
        },
      text_ui(text="CLIQUE AQUI PARA CONFIRMAR",
            pos=(0, 140),
            font="8x16",
            action="nomear"),
      
      text_ui(text="MODO DE CRIAR",
            pos=(0, 180),
            font="16x32",
            action="Inform",
            interact=False)
      ]
