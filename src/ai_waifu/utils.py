import json
import logging
from functools import wraps
from typing import Any, Callable, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_config(file_path: str) -> dict:
    """
    Load JSON configuration from a file.

    :param file_path: Path to the JSON config file.
    :return: Parsed JSON as a dictionary.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file is not a valid JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON format in {file_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error loading config from {file_path}: {e}")
        raise

def error_handler(func: Callable) -> Callable:
    """
    Decorator to handle errors in functions.

    :param func: Function to be wrapped.
    :return: Wrapped function that logs errors and returns None on failure.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(f"Error in {func.__name__}: {e}")
            return None
    return wrapper
