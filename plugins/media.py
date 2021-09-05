from pyrogram import Client, filters
from pyromod import listen

from pyrogram.types import InputMediaPhoto,InputMediaDocument,InputMediaVideo,InputMediaAnimation,InputMediaAudio
from asyncio import TimeoutError
PACK = filters.animation | filters.document| filters.video|filters.audio |filters.photo


@Client.on_message(PACK  & filters.private)
async def media(client, message):
    
     if message.photo:
        file_id = message.photo.file_id
        mid = InputMediaPhoto(file_id)

     elif message.document:
        file_id = message.document.file_id
        mid = InputMediaDocument(file_id)

     elif message.video:
        file_id = message.video.file_id
        mid = InputMediaVideo(file_id)

     elif message.animation:
        file_id = message.animation.file_id
        mid = InputMediaAnimation(file_id)

     elif message.audio:
          file_id  = message.audio.file_id
          mid = InputMediaAudio(file_id)
     else:
         print('no way')

     try:
         a = await client.ask(message.chat.id,'Now send me the link of the message of the channnel that you need to edit',
                    filters=filters.text, timeout=30)

     except TimeoutError:
           await message.reply_text(
             "```Session Timed Out.Resend the file to Start again```",
             parse_mode="md",
             quote=True
           )
           return
     link = a.text
     a = "-100"
     try:
         id = link.split('/')[4]
         msg_id = link.split('/')[5]
         chid = a + str(id)

     except:
          chid = link.split('/')[3]
          msg_id = link.split('/')[4]          

     try:
        await client.edit_message_media(
               chat_id = chid,
               message_id = int(msg_id),
               media = mid
              )
     except Exception as e:
           await message.reply_text(e)
           return
     await message.reply.text('**successfully Edited the media**')

         
   
