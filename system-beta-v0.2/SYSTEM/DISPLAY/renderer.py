from SYSTEM.DISPLAY import images, display

def render(UI):
    for elmt in UI:
        if elmt["type"] == "image":
            images.draw_image(elmt["image"],elmt["layout"]["pos"][0],elmt["layout"]["pos"][1])
            
        elif elmt["type"] == "text":
            display.draw_text(
                elmt["layout"]["pos"][0],
                elmt["layout"]["pos"][1],
                elmt["text"],
                font=elmt["font"],
                leter_cor=elmt["cor"],
                back_cor=elmt["back_cor"],
            )
        else:
            display.draw_rect(
                    elmt["layout"]["pos"][0],
                    elmt["layout"]["pos"][1],
                    elmt["layout"]["size"][0],
                    elmt["layout"]["size"][1],
                    elmt["cor"])
def update(ui):
    pass
    ui.action_ui()
