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
        "type": "image",
        "image": "cadeado",
        "layout": {
            "pos": (0, 0),
            "size": (64, 64)
        },
        "action": "Home",
        "interact": True
    },
    {
        "type": "image",
        "image": "power",
        "layout": {
            "pos": (0, 88),
            "size": (64, 64)
        },
        "action": "Power",
        "interact": True
    },
    {
        "type": "image",
        "image": "tocha",
        "layout": {
            "pos": (0, 176),
            "size": (64, 64)
        },
        "action": "Lantern",
        "interact": True
    },
    
]
