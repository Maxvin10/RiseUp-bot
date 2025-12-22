from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from handlers.handlers import router

from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN topilmadi. .env yoki Railway Variables ni tekshiring.")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()


@dp.message(Command("help"))
async def helper(message: Message):
    await message.answer(
        "Bot ma'lumotlari:\n"
        "/start - ishga tushirish\n"
        "/help - yordam\n"
        "/ask - AI-yordamchi orqali muloqot"
    )


async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(router)

    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Yordam"),
        BotCommand(command="/course", description="Kurslar ro'yxati"),
        BotCommand(command="/task", description="Vazifalar ro'yxati"),
        BotCommand(command="/ask", description="AI-yordamchi orqali muloqot"),
    ])

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
