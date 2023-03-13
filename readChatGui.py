import PySimpleGUI as sg
from readTeamChat import readTeamChat
import asyncio


async def getchat():
    return await readTeamChat()


async def chatgui():
    
    layout = [[sg.Text("Live Chat:")], [sg.Button("Refresh")], [sg.Text(key='-TEXT-', size=(350,350))]]

    # Create the window
    window = sg.Window("Rust Plus Team Chat", layout, finalize=True, size=(400,700))

    while True:
        window.refresh()    
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Refresh" or "-CHAT-":
            # Reading from chat
            chat_list = await getchat()
            window["-TEXT-"].update("\n".join(chat_list))
            window.refresh()


    window.close()
