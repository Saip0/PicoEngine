from SYSTEM.DISPLAY import images, display

def render(UI,al=False):
    for elmt in UI:
        if elmt["type"] == "image":
            images.draw_image(
                              elmt["image"],
                              elmt["layout"]["pos"][0],
                              elmt["layout"]["pos"][1]
                              )
            
        elif elmt["type"] == "rect":
            display.draw_rect(
                    elmt["layout"]["pos"][0],
                    elmt["layout"]["pos"][1],
                    elmt["layout"]["size"][0],
                    elmt["layout"]["size"][1],
                    elmt["cor"]
                    )
        
        elif elmt["type"] == "text":
            if type(elmt["text"]) == str:
                display.draw_text(
                    elmt["layout"]["pos"][0],
                    elmt["layout"]["pos"][1],
                    elmt["text"],
                    font=elmt["font"],
                    leter_cor=elmt["cor"],
                    back_cor=elmt["back_cor"],
                )
            elif type(elmt["text"]) == list and al:
                for lin in range(elmt["lin"]):
                    display.draw_text(
                            elmt["layout"]["pos"][lin][0],
                            elmt["layout"]["pos"][lin][1],
                            elmt["text"][lin],
                            elmt["font"],
                            #action="Typ",
                            #interact=False,
                            leter_cor=elmt["cor"],
                            back_cor=elmt["back_cor"],
                        )
                    
            #print(type(elmt["text"]))
def update(ui):
    pass
    ui.action_ui()