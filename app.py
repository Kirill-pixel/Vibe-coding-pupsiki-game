"""Бот + веб-сервер с игрой в одном процессе. Токен и адрес берутся из переменных окружения."""
import asyncio
import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           MenuButtonWebApp, Message, WebAppInfo)
from aiohttp import web

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ["BOT_TOKEN"]      # токен от @BotFather
GAME_URL = os.environ["GAME_URL"]    # https-адрес игры, например https://game.site.ru/
PORT = int(os.getenv("PORT", "15080"))
INDEX = Path(__file__).parent / "index.html"

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🎮 Играть в «Пупсики»", web_app=WebAppInfo(url=GAME_URL))
    ]])
    await message.answer(
        "🏠 Дина пригласила всех в гости... но из-под плиты лезут тараканы! Жми кнопку.",
        reply_markup=kb,
    )


async def index(_request):
    return web.FileResponse(INDEX)


async def main():
    app = web.Application()
    app.router.add_get("/", index)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", PORT).start()
    logging.info("Игра доступна на порту %s", PORT)

    bot = Bot(TOKEN)
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Играть", web_app=WebAppInfo(url=GAME_URL))
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
