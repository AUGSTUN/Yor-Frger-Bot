import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://te.legra.ph/file/ac25f8e0345c810278813.mp4"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YOR = "**Moshi Moshi I'm Yor Forger!** \n\n"
  YOR += "×**I'm Working Properly** \n\n"
  YOR += "×**My Owner : [AUGSTUN🝪ZECROX](https://t.me/Aug0felix)** \n\n"
  YOR += f"×**Telethon Version : {tlhver}** \n\n"
  YOR += f"×**Pyrogram Version : {pyrover}** \n\n"
  YOR += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Rikka_Tyrant_bot?start=help"), Button.url("Support", "https://t.me/tyranteyeeee")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YOR,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  YOR = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/yorforgersupportgrp")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YOR,  buttons=BUTTON)
