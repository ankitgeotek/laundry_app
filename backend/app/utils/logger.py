# app/utils/logger.py

import logging
import os
import datetime
import time

"""
Centralized Logger Configuration Module.

This module creates a logs folder (if it doesn't exist) and sets up a log file
named with the current timestamp. It configures a logger that writes debug,
info, and error messages to that file. Additionally, it provides a decorator
function to log the time taken by functions.

Usage:
    from app.utils.logger import logger, log_time_taken

    @log_time_taken
    def some_function():
        # function code here
        pass
"""

# Define the folder where log files will be stored.
LOG_FOLDER = "logs"
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)
    # Log folder creation; using print here because logger isn't initialized yet.
    print(f"Created log folder: {LOG_FOLDER}")

# Create a log file name with the current timestamp.
log_filename = datetime.datetime.now().isoformat("_", timespec="seconds").replace(":", "-") + ".log"
LOG_FILE_PATH = os.path.join(LOG_FOLDER, log_filename)

# Ensure the log file exists (creates an empty file if it does not).
if not os.path.isfile(LOG_FILE_PATH):
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
        pass

# Create and configure the logger.
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)  # Set the logger to capture all levels (DEBUG and above).

# Create a file handler that writes log messages to the log file.
file_handler = logging.FileHandler(LOG_FILE_PATH, mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)  # Ensure the file handler captures DEBUG messages.

# Create a formatter and set it for the file handler.
formatter = logging.Formatter("%(module)s:%(funcName)s:%(levelname)s:%(asctime)s:%(lineno)d:%(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger.
logger.addHandler(file_handler)

# Log that the logger has been successfully initialized.
logger.info("Logger initialized and application has started.")

def log_time_taken(func):
    """
    Decorator that logs the time taken by a function to execute.

    Args:
        func (callable): The function whose execution time is to be logged.

    Returns:
        callable: The wrapped function with time logging.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time.
        result = func(*args, **kwargs)  # Execute the original function.
        end_time = time.time()  # Record the end time.
        time_taken = end_time - start_time  # Calculate the elapsed time.
        logger.info(f"Function '{func.__name__}' took {time_taken:.4f} seconds to complete")
        return result  # Return the result of the function.
    return wrapper
