import logging
import sys

from loguru import logger

from app.config.settings import settings


def setup_logging():
    # Intercept standard logging
    class InterceptHandler(logging.Handler):
        def emit(self, record):
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno

            frame, depth = logging.currentframe(), 2
            while frame.f_code.co_filename == logging.__file__:
                frame = frame.f_back
                depth += 1

            logger.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage()
            )

    # Replace standard logging with loguru
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # Remove default loguru handler
    logger.remove()

    # Add custom handler
    if settings.JSON_LOGS:
        logger.add(
            sys.stdout,
            serialize=True,
            level=settings.LOG_LEVEL,
        )
    else:
        log_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
            "<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        )
        logger.add(
            sys.stdout,
            format=log_format,
            level=settings.LOG_LEVEL,
            colorize=True,
        )

    # Specific logger settings for libraries if needed
    for name in ["uvicorn", "uvicorn.access", "fastapi"]:
        _logger = logging.getLogger(name)
        _logger.handlers = [InterceptHandler()]
        _logger.propagate = False
