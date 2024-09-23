import asyncio
from pyrogram import Client
from logs.config import get_logger
from pyrogram.errors import FloodWait

logger = get_logger()


# Вступление в чаты
@logger.catch(reraise=True)
async def join_chats(app: Client, chats: list[int | str]):
    for chat in chats:
        try:
            await app.join_chat(chat)
            await asyncio.sleep(10)  # Задержка в 10 секунд
            # (!) если никуда не торопитесь, возможно, стоит поставить 1+ мин
            # (!) чтобы не попадать на FloodWait
            logger.info("Successfully joined")
        # Подождите N секунд перед продолжением
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            logger.info(f"Failed to join: {e}")
