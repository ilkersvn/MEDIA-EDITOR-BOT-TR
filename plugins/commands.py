from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MSG = """**Merhaba {}
  
Ben Medya Değiştirme botuyum...

Belge, video, gif, ses, fotoğraf vb. düzenleyebilirsiniz...

Daha fazla bilgi için /help **

"""


HELP_MSG = """
Sırasıyla adımları takip edin..

🌀Önce bana değiştirmek istediğiniz medyanın yerine bir medya gönderin

🌀Değiştirmek istediğiniz medyanın bağlantısını gönderin

Not: Botun kanalda yönetici olduğuna dikkat edin

"""






@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text="OWNER",url = "t.me/")]]),
        reply_to_message_id=message.message_id
    )    



@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=HELP_MSG,
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id
    )    
