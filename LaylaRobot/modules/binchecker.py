import requests
from telethon import events, Button, TelegramClient
import os
import logging
from LaylaRobot import pbot as bin


logging.basicConfig(level=logging.INFO)


@bin.on(events.NewMessage(pattern="^[!?/]bin"))
async def binc(event):
    xx = await event.reply("`Processing.....`")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
        res = url.json()
        vendor = res['data']['vendor']
        type = res['data']['type']
        level = res['data']['level']
        bank = res['data']['bank']
        country = res['data']['country']
        me = (await event.client.get_me()).username

        valid = f"""
<b>➤ Valid Bin:</b>

<b>Bin -</b> <code>{input}</code>
<b>Status -</b> <code>Valid Bin</code>
<b>Vendor -</b> <code>{vendor}</code>
<b>Type -</b> <code>{type}</code>
<b>Level -</b> <code>{level}</code>
<b>Bank -</b> <code>{bank}</code>
<b>Country -</b> <code>{country}</code>

<b>Checked By - @{me}</b>
<b>User-ID - {event.sender_id}</b>
"""
        await xx.edit(valid, parse_mode="HTML")
    except IndexError:
       await xx.edit("Plese provide a bin to check\n__`/bin yourbin`__")
    except KeyError:
        me = (await event.client.get_me()).username
        await xx.edit(f"**➤ Invalid Bin:**\n\n**Bin -** `{input}`\n**Status -** `Invalid Bin`\n\n**Checked By -** @{me}\n**User-ID - {event.sender_id}**")

print ("Successfully Started")
bin.run_until_disconnected()
