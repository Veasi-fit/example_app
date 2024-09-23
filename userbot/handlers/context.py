from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

from userbot.lexicon.lexicon import (
    keywords, chats, resiver
)
from logs.config import get_logger

logger = get_logger()


# Хендлер мониторинга сообщений из чатов
async def handle_message(app: Client, message: Message):
    if any(keyword in message.text.lower() for keyword in keywords):
        msg = (
            f"{message.text}\n\n"
            f"Контакт: @{message.from_user.username}\n\n"
            f"Источник: {message.chat.username}"
        )
        try:
            # (!) позже узнал отправлять от лица аккаунта, вроде, небезопасно
            # (!) нужно ли менять подход - не знаю
            logger.debug('Sending message to mailbot')
            await app.send_message(
                chat_id=resiver,
                text=msg
            )
            logger.debug(f'message: {msg}\n was sended')
        except Exception as e:
            logger.error(f'Failed to send message: {e}')


# Регистрация хендлера
async def setup_handlers(app: Client):
    try:
        logger.debug('Setting up handlers')
        app.add_handler(
            MessageHandler(handle_message, filters.chat(chats=chats))
        )
        logger.debug('Set up handlers - success')
    except Exception as e:
        logger.debug(f'Еrror till set up handler: {e}')
