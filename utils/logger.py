import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(asctime)s; %(message)s:"
)

logger = logging.getLogger(__name__)

def info(message: str):
    logger.info(f"#{message}#")

def warning(message: str):
    logger.warning(f"#!{message}!#")