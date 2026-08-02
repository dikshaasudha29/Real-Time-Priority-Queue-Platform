import logging
import sys

from app.core.config import Settings


def configure_logging(settings: Settings) -> None:
    
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        stream=sys.stdout,
    )
    # Quiet down noisy third-party loggers unless we're actively debugging them.
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
