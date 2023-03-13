import asyncio
from rustplus import RustSocket
import logging

logger = logging.getLogger(__name__)

with open("./serverInfo.txt", "r") as f:
    info = list(f)

IP = info[0]
PLAYERTOKEN = int(info[1])
STEAMID = int(info[2])

f.close()

async def sendChat(message):
    logger.debug(f"Message to send: [{message}]")
    to_return = ""
    socket = RustSocket(IP, "28082", STEAMID, PLAYERTOKEN)
    await socket.connect()
    to_return = await socket.send_team_message(message)
    return to_return

#asyncio.run(sendChat())