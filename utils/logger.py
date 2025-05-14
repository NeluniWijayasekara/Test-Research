import logging
import os
from datetime import datetime
from config import LOG_DIR

# Ensure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Log file with timestamp
log_filename = datetime.now().strftime(f"{LOG_DIR}/log_%Y-%m-%d_%H-%M-%S.log")

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("SymptomDetectionApp")
