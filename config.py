from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config:
    API_ID = int(getenv("API_ID"))
    API_HASH = getenv("API_HASH")
    BOT_TOKEN = getenv("BOT_TOKEN")

    
    OWNER_ID = "1663603208"
    MONGO_DB_URI = "mongodb+srv://anmol:anmol@cluster0.fv0q0im.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    START_PIC = "https://telegra.ph/file/0eba143d65f9413f9ae04.jpg"
    SUDOERS = filters.user([1663603208])
