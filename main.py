import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Update, ChatJoinRequest, Message
from aiogram.filters import CommandStart
import os
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.chat_join_request()
async def approve_join_request(request: ChatJoinRequest):
    user = request.from_user
    chat = request.chat

    try:
        await bot.approve_chat_join_request(
            chat_id=chat.id,
            user_id=user.id
        )
        logger.info(f"✅ Принят: {user.full_name} (@{user.username}) → {chat.title}")


    except Exception as e:
        logger.error(f"❌ Ошибка при принятии {user.id}: {e}")



async def main():
    logger.info("🤖 Бот запущен...")
    await dp.start_polling(bot, allowed_updates=["chat_join_request", "message"])


if __name__ == "__main__":
    asyncio.run(main())
