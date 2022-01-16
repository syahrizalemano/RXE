# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Command` **ERROR*")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t 🔰  "
        await event.edit(
            "**RXE USERBOT**\n\n"
            f"**RXE USER {DEFAULTUSER}**\n**RXE MODULE : {len(modules)}**\n\n"
            "**• RXE MENU :**\n"
            f"◉ {string}◉\n\n✐ **CATATAN :**  `.help animasi`\n✐  support : @rxesupport"
        )
        await asyncio.sleep(1000)
        await event.delete()
