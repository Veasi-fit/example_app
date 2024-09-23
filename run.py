import asyncio
from userbot.app import run_app
from logs.config import get_logger

logger = get_logger()


@logger.catch(reraise=True)
async def main():
    logger.info('ЗАПУСК APP')

    # ЗАПУСК
    try:
        await run_app()
    except Exception as e:
        logger.debug(f"ОШИБКА ПРИ ЗАПУСКЕ APP {e}")

asyncio.run(main())
logger.debug("APP - STARTED")

# (!) могут возникнуть проблемы с импортами
# (!) приложение поднимается через докер
# (!) запускайте через poetry
# (!) команда запуска в докер ["poetry", "run", "python", "run.py"]
