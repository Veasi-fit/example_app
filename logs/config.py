from loguru import logger
import sys

# Настройка логирования
logger.remove()  # Удаляем все обработчики, чтобы избежать дублирования логов
logger.add(
    sys.stdout,
    level="DEBUG",
    format="{time} {level} {module} {line} {message}"
)


# Функция для получения логгера
def get_logger():
    return logger
