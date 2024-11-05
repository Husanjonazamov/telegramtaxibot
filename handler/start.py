# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts



@dp.message_handler(commands=['start'])
async def start_handler(message: Message, state: FSMContext):
    """
    asosiy start funksiyasi
    """
    first_name = message.from_user.first_name
    await message.answer(texts.START.format(first_name))
    

