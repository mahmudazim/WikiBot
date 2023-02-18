import logging

from aiogram import Bot, Dispatcher, executor, types
from wikipedia import wikipedia

API_TOKEN = 'YOUR_API_TOKEN'
wikipedia.set_lang("uz")
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom!\nMen wikibotman!")



@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)