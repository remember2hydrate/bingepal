import logging
from logging.handlers import RotatingFileHandler
import os

# ✅ Ensure logs directory exists before anything else
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("bingepal")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "dev.log")
file_handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3)
file_handler.setFormatter(formatter)

if not os.path.exists(log_path):
    open(log_path, "a").close()

if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
