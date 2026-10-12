from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad.substates.writ_txt.ui import UI as Wr_UI
from SYSTEM.SCREENS.lock_screen.substates.home.substates.notepad import events

def Salvar():
    for Ui in Wr_UI:
        #Procura pela anotação atual que está dentro de Wr_UI
        if Ui["action"] == "Typ":
            encontrado = False
            #Aprós encontra-la se ela o programa salva a atualização da UI em Dados_Note
            for Dados in events.Dados_Note:
                if Dados["ID"] == Ui["ID"]:
                    events.Dados_Note[events.Dados_Note.index(Dados)] = Ui
                    encontrado = True
            if not encontrado:
                events.Dados_Note.append(Ui)
