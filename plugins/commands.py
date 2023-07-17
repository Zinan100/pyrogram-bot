from pyrogram import Client as app, filters

@app.on_message(filters.command('start'))
async def start_msg(bot, msg, _):
  h = await msg.reply_text(".")
  await asyncio.sleep(1)
  await h.delete()
  h1 = await msg.reply_text("..")
  await asyncio.sleep(1)
  await h1.delete()
  h2 = await msg.reply_text("...")
  await asyncio.sleep(1)
  await h2.delete()
  await msg.reply_text(
    text=f"hlo {msg.from_user.mention},/n I am an no use bot"
  )
