Import os

from strings import *
from var import Var






bot = TelegramClient(None, Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)

@bot.on(events.NewMessage(pattern="/start", incoming=True, func=lambda e: e.is_private))

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
a = int(a)
b = int(b)
ab = (a+b)

print("answer", ab)
