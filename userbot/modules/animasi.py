from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.lipkol(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`ka ayo lipkol`")
    sleep(2)
    await typew.edit("`lipcrot jg gapapa`")
    sleep(1)
    await typew.edit("`hayo HAYO`")


# Create by myself @localheart


@register(outgoing=True, pattern="^.idns(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        
"██╗██████╗░\n"
"██║██╔══██╗\n"
"██║██║░░██║\n"
"██║██║░░██║\n"
"██║██████╔╝\n"
"╚═╝╚═════╝░\n"

"███╗░░██╗░██████╗\n"
"████╗░██║██╔════╝\n"
"██╔██╗██║╚█████╗░\n"
"██║╚████║░╚═══██╗\n"
"██║░╚███║██████╔╝\n"
"╚═╝░░╚══╝╚═════╝░ IDONOT SLEEP\n"
    )


# Create by myself @localheart


@register(outgoing=True, pattern="^.gigitnih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "░▄▄▄▄░\n"
        "▀▀▄██►\n"
        "▀▀███►\n"
        "░▀███►░█►\n"
        "▒▄████▀▀\n"

        "\n**RAWWRR**"
    )


# Create by myself @localheart


@register(outgoing=True, pattern="^.anjing(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
"░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░\n"
"░█░░░░░░░░▀▄░░░░░░▄░\n"
"█░░▀░░▀░░░░░▀▄▄░░█░█\n"
"█░▄░█▀░▄░░░░░░░▀▀░░█\n"
"█░░▀▀▀▀░░░░░░░░░░░░█\n"
"█░░░░░░░░░░░░░░░░░░█\n"
"█░░░░░░░░░░░░░░░░░░█\n"
"░█░░▄▄░░▄▄▄▄░░▄▄░░█░\n"
"░█░▄▀█░▄▀░░█░▄▀█░▄▀░\n"
"░░▀░░░▀░░░░░▀░░░▀░░░\n"
"gug gug"
    )


CMD_HELP.update(
    {
        "animasi2": "𝑹𝑿𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫: `.lipkoko;`\
    \n↳ : slipcrot\
    \n\n𝑹𝑿𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫: `.idns`\
    \n↳ : Coba aja.\
    \n\n𝑹𝑿𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫: `.gigitnih`\
    \n↳ : xixixi.\
    \n\n𝑹𝑿𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫: `anjing`\
    \n↳ : mirip anjing comel."
    }
)
