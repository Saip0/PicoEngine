from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.crate_not import ui as Cr_UI
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad import ui as Note_UI
from SYSTEM.DISPLAY.rederer import render
criar():
    for elmt in Cr_UI:
        if elmt["Typ"]:
            text = elmt
        elif elmt["Typing"]:
            surf = elmt
            
    if len(text.strip()) < 3:
        text["text"] = "INVALIDO"
        render([text,surf],al=True)
    
