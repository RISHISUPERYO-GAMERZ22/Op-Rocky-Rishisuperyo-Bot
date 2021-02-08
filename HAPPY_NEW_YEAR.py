from telethon import events
import asyncio
from uniborg.util import Op Rocky Rishisuperyo Bot_cmd
from bot import CMD_HELP, ALIVE_NAME
@borg.on(events.NewMessage(pattern=r"^/hpnyear", outgoing=True))
async def hapy(event):
    a = "`✨┏━┓━┓━┓━┓━┓🎉\n🎈┃H┃A┃P┃P┃Y┃🎊\n🎉┗━┛━┛━┛━┛━┛🎈\n\n┏━┓━┓━┓⠀⠀⠀⠀\n┃N┃E┃W┃⠀⠀⠀⠀\n┗━┛━┛━┛⠀⠀⠀⠀\n\n🎊┏━┓━┓━┓━┓━┓🍾\n🎈┃Y┃E┃A┃R┃❤️🎉⠀\n🎉┗━┛━┛━┛━┛━┛🎆`"
    await event.edit(a)
