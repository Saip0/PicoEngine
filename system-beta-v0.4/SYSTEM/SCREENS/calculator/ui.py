font_sizes = {
    "8x16": (8,16),
    "16x16": (16,16),
    "16x32": (16, 32),
}

def text_ui(text, pos, font="8x16", action=None, interact=True):
    w, h = font_sizes[font]

    return {
        "type": "text",
        "text": text,
        "font": font,
        "layout": {
            "pos": pos,
            "size": ((len(text) * w), h)
        },
        "action": action,
        "interact": interact
    }


UI = [
    
        {
        "type" : "rect",
        "cor" : "BRANCO",
        "layout": {
            "pos": (0,0),
            "size": (225,176)
            },
        "action": "Typing",
        "interact": True
        },
        {
        "type": "image",
        "image": "igual",
        "layout": {
            "pos": (0, 176),
            "size": (64, 64)
        },
        "action": "igual",
        "interact": True
    },
    ]