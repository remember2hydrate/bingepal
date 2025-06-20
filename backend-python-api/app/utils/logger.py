import logging

LOG_FILE = "app.log"

logger = logging.getLogger("binge-pal")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# Stream handler (console)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
