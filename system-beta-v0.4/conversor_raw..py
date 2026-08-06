"""
Tool: Image Converter

Purpose:
Converts images to RGB565 RAW format for ILI9341 display.

Note:
This script was generated with AI assistance.
Review required before major modifications.
"""
from PIL import Image
from pathlib import Path

def main(local):
    
    script_dir = Path(__file__).parent

    img = Image.open(local).convert("RGB")
    w, h = img.size

    out_name = script_dir / (Path(local).stem + ".raw")

    with open(out_name, "wb") as f:
        f.write(w.to_bytes(2, "little"))
        f.write(h.to_bytes(2, "little"))

        for y in range(h):
            for x in range(w):
                r, g, b = img.getpixel((x, y))

                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                f.write(rgb565.to_bytes(2, "big"))

    print("Salvo em:", out_name)

while True:
    try:
        local = input("local -> ")
        main(local)

    except Exception as e:
        print(e, "\n<local inválido>")

    else:
        print("<Arquivo Salvo Com Sucesso>")