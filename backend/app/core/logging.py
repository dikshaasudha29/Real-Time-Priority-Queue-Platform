import logging
import sys

from app.core.config import Settings


def configure_logging(settings: Settings) -> None:
    """
    Configures Python's root logger with a consistent format and level.

    Called once, at application startup (from app.main), before anything
    else runs. Every module in the app can then just do:
        logger = logging.getLogger(__name__)
    and get consistent, correctly-formatted output without repeating
    configuration in every file.
    """
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        stream=sys.stdout,
    )

    # Quiet down noisy third-party loggers unless we're actively debugging them.
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
