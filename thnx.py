"""plugin idea by kiddo"""
"""ANIMATION idea provided by  @Rishisuperyo in tg :) """
"""PLUGIN MEANS :- tq = thanks--> many users say thanks but they also say tq ---> tq means thanks"""
"""USAGE FOR PLUGIN TQ :-.tq ''''
'""U CAN USE THIS PLUGIN TO SAY THANKS ANYONE"""
"""PLUGIN BY RISHISUPERYO"""

from telethon import events
import asyncio
from uniborg.util import Op Rocky Rishisuperyo Bot_cmd
from bot import CMD_HELP, ALIVE_NAME
@borg.on(events.NewMessage(pattern=r"^.tq", outgoing=True))
async def _(event):
    a="▀▀▀▀█▀▀▀▀             Q Q Q Q \n           |█                      Q             Q \n            ░                      Q             Q\n            █                      Q            Q\n            ░                         Q        Q\n            █                            Q  Q\n                                                   Q\n                                                      Q"
    await event.edit(a)