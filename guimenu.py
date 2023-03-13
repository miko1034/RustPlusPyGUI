import PySimpleGUI as sg
import asyncio
from readChatGui import chatgui
from sendChatGui import sendChat

async def menuwindow():
    
    layout = [[sg.Text("Welcome to menu")], [sg.Button("Open Team Chat", key="-CHAT-")], [sg.Button("Send Message", key="-SEND-")]]
    choice = None
    window = sg.Window("Menu", layout, finalize=True, size=(400,400))
    while True:
        window.refresh()    
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break 
        if event == "-CHAT-":
            await chatgui()
        if event == "-SEND-":
            await sendChat()

    window.close()
