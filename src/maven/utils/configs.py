import json
import yaml

def load_config(file_path: str):
    """Load configuration settings from a JSON or YAML file."""
    try:
        with open(file_path, "r") as file:
            if file_path.endswith(".json"):
                return json.load(file)
            elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
                return yaml.safe_load(file)
            else:
                raise ValueError("Unsupported config file format.")
    except Exception as e:
        print(f"Error loading config: {e}")
        return None
    
def validate_theme_config(theme_config: dict) -> bool:
    """Validate theme configuration for required keys."""
    required_keys = {"background", "text_color", "accent_color"}
    if not isinstance(theme_config, dict):
        print("Invalid theme config: Not a dictionary.")
        return False
    missing_keys = required_keys - theme_config.keys()
    if missing_keys:
        print(f"Invalid theme config: Missing keys {missing_keys}")
        return False
    return True

def load_theme(config: dict):
    """Load and apply theme settings from the configuration."""
    if "theme" in config and validate_theme_config(config["theme"]):
        theme = config["theme"]
        print(f"Applying theme: Background={theme['background']}, Text={theme['text_color']}, Accent={theme['accent_color']}")
    else:
        print("No valid theme found in config.")