from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired

@app.on_message(filters.command(["givelink", "getlink", "link"]))
async def give_link(bot, message):

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /link <chat_id>")

    try:
        chat_id = int(message.command[1])  # << IMPORTANT FIX

        link = await bot.export_chat_invite_link(chat_id)
        await message.reply(f"✅ Chat Invite Link:\n{link}")

    except ValueError:
        await message.reply("❌ Invalid chat_id format!")

    except ChatAdminRequired:
        await message.reply("❌ Bot admin nahi hai ya invite permission nahi hai!")

    except Exception as e:
        await message.reply(f"⚠️ Error: {e}")
