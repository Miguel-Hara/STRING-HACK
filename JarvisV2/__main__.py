import asyncio
import importlib

from pyrogram import idle
from JarvisV2 import LOG
from JarvisV2.modules import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("JarvisV2.modules." + all_module)
    LOG.print("[bold yellow]ʜᴀᴄᴋ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ɴᴏᴡ ʀᴇᴀᴅʏ ᴛᴏ ғᴜᴄᴋ ᴜsᴇʀs")
    await idle() 
    LOG.print("[bold red]ᴄᴀɴᴄᴇʟʟᴇᴅ ᴀʟʟ ᴛᴀsᴋ🤐..........")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
