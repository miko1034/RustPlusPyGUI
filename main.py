from readChatGui import chatgui, getchat
from sendChat import sendChat
import asyncio
from guimenu import menuwindow
import logging

logging.basicConfig(level=logging.DEBUG, format="%(relativeCreated)6d %(threadName)s %(message)s ")

main = menuwindow()
asyncio.run(main)