# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import time
from datetime import datetime

import redis

from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register

ezzra = [
    "HALLO, MY NAME"
    "███████████████████████████████\n"
    "█▄─▄▄─█░▄▄░▄█░▄▄░▄█▄─▄▄▀██▀▄─██\n"
    "██─▄█▀██▀▄█▀██▀▄█▀██─▄─▄██─▀─██\n"
    "▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀\n",
]

rahkii = [
    "ngeng, im"
    "╔═══╦═══╦╗─╔╦╗╔═╦══╦══╗\n"
    "║╔═╗║╔═╗║║─║║║║╔╩╣╠╩╣╠╝\n"
    "║╚═╝║║─║║╚═╝║╚╝╝─║║─║║\n"
    "║╔╗╔╣╚═╝║╔═╗║╔╗║─║║─║║\n"
    "║║║╚╣╔═╗║║─║║║║╚╦╣╠╦╣╠╗\n"
    "╚╝╚═╩╝─╚╩╝─╚╩╝╚═╩══╩══╝\n",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.ezzra(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "HALLO, MY NAME\n"
        "███████████████████████████████\n"
        "█▄─▄▄─█░▄▄░▄█░▄▄░▄█▄─▄▄▀██▀▄─██\n"
        "██─▄█▀██▀▄█▀██▀▄█▀██─▄─▄██─▀─██\n"
        "▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀\n"
    )


@register(outgoing=True, pattern="^.rahkii(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "ngeng, im\n"
        "╔═══╦═══╦╗─╔╦╗╔═╦══╦══╗\n"
        "║╔═╗║╔═╗║║─║║║║╔╩╣╠╩╣╠╝\n"
        "║╚═╝║║─║║╚═╝║╚╝╝─║║─║║\n"
        "║╔╗╔╣╚═╝║╔═╗║╔╗║─║║─║║\n"
        "║║║╚╣╔═╗║║─║║║║╚╦╣╠╦╣╠╗\n"
        "╚╝╚═╩╝─╚╩╝─╚╩╝╚═╩══╩══╝\n"
    )


@register(outgoing=True, pattern="^.rping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**APA🦭**")
    await pong.edit("**KENAPA🦭**")
    await pong.edit("**HA KENAPA🦭**")
    await pong.edit("**HAA🦭**")
    await pong.edit("**GIMANA GIMANA?🦭**")
    await pong.edit("**WHAATT🦭**")
    await pong.edit("**🦭**")
    await pong.edit("`.............🏃🏻..🏃🏻.. 🦖`")
    await pong.edit("`............🏃🏻..🏃🏻.. 🦖.`")
    await pong.edit("`...........🏃🏻..🏃🏻.. 🦖..`")
    await pong.edit("`..........🏃🏻..🏃🏻.. 🦖...`")
    await pong.edit("`.........🏃🏻..🏃🏻.. 🦖....`")
    await pong.edit("`........🏃🏻..🏃🏻.. 🦖.....`")
    await pong.edit("`.......🏃🏻..🏃🏻.. 🦖......`")
    await pong.edit("`......🏃🏻..🏃🏻.. 🦖.......`")
    await pong.edit("`.....🏃🏻..🏃🏻.. 🦖........`")
    await pong.edit("`....🏃🏻..🏃🏻.. 🦖.........`")
    await pong.edit("`...🏃🏻..🏃🏻.. 🦖..........`")
    await pong.edit("`..🏃🏻..🏃🏻.. 🦖...........`")
    await pong.edit("`.🏃🏻..🏃🏻.. 🦖............`")
    await pong.edit("`🏃🏻..🏃🏻.. 🦖.............`")
    await pong.edit("`.🏃🏻.. 🦖..............`")
    await pong.edit("`🏃🏻.. 🦖...............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**{ALIVE_NAME}**        \n"
        f"**➾Kecepatan : ** %sms  \n"
        f"**➾Branch : ** RXE \n" % (duration)
    )


@register(outgoing=True, pattern="^.lping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**`{ALIVE_NAME}`**\n"
        f"✧ **-ꜱɪɢɴᴀʟ- :** "
        f"`%sms` \n"
        f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
        f"`{uptime}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"`%sms` \n" f"➾ __Uptime__ __:__ " f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**loading..**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**PONG!!**\n"
        f"**TEST MODE:** "
        f"`%sms` \n"
        f"**ᴜᴘᴛɪᴍᴇ:** "
        f"`{uptime}` \n"
        f"**RXE USER:** `{ALIVE_NAME}`" % (duration)
    )


@register(outgoing=True, pattern="^.kocok$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8===✊D💦")
    await pong.edit("8====D💦💦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**KONTOL!! **\n**NGENTOT** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


CMD_HELP.update(
    {
        "ping": "𝑹𝑿𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫: `.ping` | `.lping` | `.xping` | `.sinyal` | `.sping` | `.pink` | `.fping`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝑹𝑿𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫: `.kecepatan`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝑹𝑿𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫: `.pong`\
         \n↳ : Sama Seperti Perintah Ping."
    }
)
