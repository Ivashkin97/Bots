import aiogram
from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = 'TOKEN'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)





