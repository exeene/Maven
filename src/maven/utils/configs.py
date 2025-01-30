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