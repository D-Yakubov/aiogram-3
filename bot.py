from aiogram import Bot, Dispatcher, types
from asyncio import run

dp = Dispatcher()

async def echo(message: types.Message, bot: Bot):
	await message.copy_to(chat_id=message.chat.id)

async def start():

	dp.message.register(echo)
	bot = Bot("6524002067:AAF84OhGOgZpiYD8d6P6Vilsghf043NE-Qk")
	await dp.start_polling(bot, polling_timeout=1)

run(start())
