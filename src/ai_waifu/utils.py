import json
import logging
import os
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Dict, Optional, TypeVar

T = TypeVar('T')

def load_config(file_path: str) -> Dict[str, Any]:
    """Load configuration from JSON file with validation."""
    config_path = Path(file_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file {file_path} not found")
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        if not isinstance(config, dict):
            raise ValueError("Config file must contain a JSON object")
        return config
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in config: {e}")
        raise

def error_handler(func: Callable[..., T]) -> Callable[..., Optional[T]]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Optional[T]:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            return None
    return wrapper