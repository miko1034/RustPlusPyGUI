import PySimpleGUI as sg
from sendChat import sendChat as rSendChat
import asyncio
import logging

logger = logging.getLogger(__name__)

async def sendChat():
    
    layout = [[sg.Text("Send a message")], [sg.Button("Send", key="-SEND-")], [sg.Input(key='-TEXT-', size=(100,150))]]
    window = sg.Window("Send A Message", layout, finalize=True, size=(150,150))

    while True:
        window.refresh()    
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "-SEND-":
            # Reading from chat
            await rSendChat(values['-TEXT-'])
            window["-TEXT-"].update("Message Sent")
            window.refresh()


    window.close()
