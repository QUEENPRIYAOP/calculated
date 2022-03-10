#  Copyright (c) 2021 thanosuser

import logging
import re

from pyrogram import Client
from pyrogram.errors import (
    FloodWait,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from telethon import Button, TelegramClient, events
from telethon.errors.rpcerrorlist import FloodWaitError as fwe
from telethon.errors.rpcerrorlist import PasswordHashInvalidError as phi
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError as pce
from telethon.errors.rpcerrorlist import PhoneCodeInvalidError as pci
from telethon.errors.rpcerrorlist import SessionPasswordNeededError as spn
from telethon.sessions import StringSession

from strings import *
from var import Var

logging.basicConfig(level=logging.INFO)

bot = TelegramClient(None, Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)

@bot.on(events.NewMessage(pattern="/start", incoming=True, func=lambda e: e.is_private))
async def begin(e):
    if e.fwd_from:
        return
    await e.reply(
a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
a = int(a)
b = int(b)
ab = (a+b)

print("answer", ab)

)
