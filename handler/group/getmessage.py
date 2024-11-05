# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts

# add import
import re

SOURCE_GROUP_ID = -1002288974096
TARGET_GROUP_ID = -1002264446732

pattern = re.compile(r"(beshariqga ketishim kerak|toshkentga ketishim kerak|toshkentdan beshariqqa ketish|beshariqdan toshkentga ketish)", re.IGNORECASE)



@dp.message_handler(lambda message: message.chat.type in ['group', 'supergroup'], content_types=['text'])  # Faqat guruhlarda va faqat matn uchun
async def forward_message(message: Message):
    if message.chat.id == SOURCE_GROUP_ID:
        admins = await bot.get_chat_administrators(message.chat.id)
        admin_ids = [admin.user.id for admin in admins]

        if message.from_user.id not in admin_ids and pattern.search(message.text.lower()): 
            text = message.text 
            username = message.from_user.username
            await bot.send_message(
                chat_id=TARGET_GROUP_ID,
                text=texts.user_message_send(
                    text=text,
                    username=username
                )
            )
            await bot.delete_message(SOURCE_GROUP_ID, message.message_id)
        else:
            print("----")
    else:
        print("----")

