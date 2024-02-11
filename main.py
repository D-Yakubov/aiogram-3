from aiogram import Bot, Dispatcher
from asyncio import run
from functions import get_user_info

dp = Dispatcher()

async def startup_answer(bot: Bot):
	await bot.send_message(chat_id=1206612180, text="Bot ishga tushdi!")

async def shutdown_answer(bot: Bot):
	await bot.send_message(chat_id=1206612180, text="Bot ishdan to'xtadi!")

async def start():

	dp.startup.register(startup_answer)
	dp.message.register(get_user_info)
	dp.shutdown.register(shutdown_answer)
	bot = Bot("6524002067:AAF84OhGOgZpiYD8d6P6Vilsghf043NE-Qk")
	await dp.start_polling(bot, polling_timeout=1)

run(start())
