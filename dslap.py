"""
DANGERSLAP Plugin For Userbot
usage:- /slap in reply to any message, or u gonna dslap urself.
"""

import random

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from bot.utils import OP ROCKY RISHISUPERYO BOT_cmd
from bot import ALIVE_NAME

DANGERSLAP_TEMPLATES = [
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} uske mouth pa with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} feka ek {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} diya ek friendly push to help {user2} learn to swim in 100+° hot lava.",
 
]
 
ITEM = [

    "cast iron skillet",
    "large trout",
    "baseball bat",
    "cricket bat",
    "wooden cane",
    "nail",
    "printer",
    "shovel",
    "CRT monitor",
    "physics textbook",
    "toaster",
    "portrait of Richard Stallman",
    "television",
    "five ton truck",
    "roll of duct tape",
    "book",
    "laptop",
    "old television",
    "sack of rocks",
    "rainbow trout",
    "rubber chicken",
    "spiked bat",
    "fire extinguisher",
    "heavy rock",
    "chunk of dirt",
    "beehive",
    "piece of rotten meat",
    "bear",
    "ton of bricks",
    "maths book",
    "football",
    "spiked shoes",
    "iron chair",
    "bottle with 10 ton of rocks",
    "old window",
    "old door",
    "big almira",
    "rotten eggs",
    "strong tool",
    "iron bat",
    "iron table",
    "wooden table",
    "iron chair",
    "date expired medicines",
    "iron rod",
    "big calender",
    "music player",
    "iron made raido",
    "iron made dvd player",
    "cd player",
    "electric wire",
    "cd",
    "dvd",
    "CPU of computer",
    "Monitor of computer",
    "100 days unwashed dirty smell clothes",
    "Remote",
    "Old Smartphone",
    "Old battery",
    "Bouncy ball",
    "Earth globe",
    "Old dirty plastic",
    
]

THROW = [
    "throws",
    "flings",
    "chucks",
    "hurls", 
    "fek ka mari",
    
]

HIT = [
    "hits",
    "whacks",
    "slaps",
    "smacks",
    "bashes",
    "smashes",
    
]

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "IndianBot"


@borg.on(lightning_cmd("song2 ?(.*)"))
async def who(event):
    if event.fwd_from:
        return
    replied_user = await get_user(event)
    caption = await slap(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.edit(caption)

    except:
        await event.edit("Can't slap this nibba !!")


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("I don't slap strangers !!")
            return None

    return replied_user


async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}"

    temp = random.choice(DANGERSLAP_TEMPLATES)
    item = random.choice(ITEM)
    hit = random.choice(HITS)
    throw = random.choice(THROWS)

    caption = temp.format(
        user1=DEFAULTUSER, user2=slapped, item=item, hits=hit, throws=throw
    )

    return caption