import asyncio
from rustplus import RustSocket
import time
import logging

with open("./serverInfo.txt", "r") as f:
    info = list(f)

IP = info[0]
PLAYERTOKEN = int(info[1])
STEAMID = int(info[2])

f.close()

async def readTeamChat():
    socket = RustSocket(IP, "28082", STEAMID, int(PLAYERTOKEN))
    await socket.connect()
    
    #reads team chat
    
    to_return = []
    getchat = await socket.get_team_chat()
    for message in getchat:
        to_return.append(f"{message.name}: {message.message}")

    await socket.disconnect()
    return to_return

