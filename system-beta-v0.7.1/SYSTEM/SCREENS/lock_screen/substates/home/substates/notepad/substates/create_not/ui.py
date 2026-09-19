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
      text_ui(text="(A) CLIQUE AQUI PARA CONFIRMAR",
            pos=(0, 176),
            font="8x16",),
      
      text_ui(text="(B) PARA CANCELAR E SAIR",
            pos=(0, 200),
            font="8x16",)
      ]
