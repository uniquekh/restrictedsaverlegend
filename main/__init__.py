#Join me at telegram @LegendBotzs

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("21179966", default=None, cast=int)
API_HASH = config("d97919fb0a3c725e8bb2a25bbb37d57c", default=None)
BOT_TOKEN = config("7066937947:AAEqiZ95P9X5Xjd_Dj801ef1gN7Ij1Uvtvc", default=None)
SESSION = config("AQFDLj4AwVJQxc4eJUHWn9ZTGW30o-HHgs_xR6fiolhw5Y-a0AOXT6v0lmwAi9VoAbp_gH05uMhon9BrB0RjWwwk1eY3eZ_WBzpHiV0bMwQinGRQlYiiORqgHiFzW17uT_6SLsmd03gtIzicFjun3lXO0TfSogSw5FnbQVxuTyMzaXTRmzPdl89UuBt2hU_LC-cLOac8jErdnc_01OyqS5uceC59tIo-r8k8YoCVBXfPP2faysgAXPKNHZfrlGNlnwore-5yRdkWfGMweEH1tj4Bes1fIXN10iVkfJjJwPuq1w6R_wglb47HvRtlT6ajHLThZl6ehCJMSd53gaRJKKFHlHAGrwAAAAG0r_Q_AA", default=None)
FORCESUB = config("@scammer_botxz", default=None)
AUTH = config("7326397503", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @LegendBotzs.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
