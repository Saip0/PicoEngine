font_sizes = {
    "8x16": (8,16),
    "16x16": (16,16),
    "16x32": (16, 32),
}

def text_ui(text, pos, font="8x16", action=None, interact=True,cor="BRANCO",back_cor="PRETO",line=0):
    
    w, h = font_sizes[font]
    
    return {
        "type": "text",
        "text": text,
        "lin" : line,
        "cor" : cor,
        "back_cor" : back_cor,
        "font": font,
        "layout": {
            "pos": pos,
            "size": ((len(text[line]) * w), h)
        },
        "action": action,
        "interact": interact
    }
UI = []