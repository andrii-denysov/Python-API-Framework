import logging
import os
from datetime import datetime

# Create a logger
logger = logging.getLogger("POETRY_DB_LOGS")
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set level for console output

# Create directory if it doesn't exist
log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create a file handler
file_handler = logging.FileHandler(f"../logs/poetrydb_{datetime.now().strftime('%Y_%m_%d_%H-%M')}.log")
file_handler.setLevel(logging.INFO)  # Set level for file output

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Attach formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
