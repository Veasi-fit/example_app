import asyncio
from pyrogram import Client
from userbot.handlers.context import setup_handlers
from config.config import load_config
from logs.config import get_logger
from userbot.utils.utils import join_chats
from userbot.lexicon.lexicon import chats

logger = get_logger()


# Первичные настройки перед работой юзербота
async def work(
    app: Client,
    chats: list[int | str],
):
    try:
        # Регистрация хендлера
        await setup_handlers(app)
        # Вступаем в чаты
        # (?) нужно ли вступать аккаунтом в чаты, дляих мониторинга
        # (?) или мониторинг может работать без этого
        await join_chats(app, chats)
    except Exception as e:
        logger.debug(f'ERROR: {e}')


# Функция запуска
async def run_app():
    config = load_config()

    app = Client(
        "userbot",
        api_id=config.userbot.api_id,
        api_hash=config.userbot.api_hash
    )

    async with app:
        await work(app, chats)
        logger.info("Userbot is running...")

        # Держим приложение запущенным
        # (!) не уверен что это здесь нужно, точку входа переписывал
        # (!) несколько раз, не успел проверить
        await asyncio.Event().wait()
