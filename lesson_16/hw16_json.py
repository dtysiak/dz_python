import os
import json
import logging

logging.basicConfig(
    filename="json__Tysiak.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder_path = "."

for filename in os.listdir(folder_path):
    if not filename.endswith(".json"):
        continue

    full_path = os.path.join(folder_path, filename)

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"File '{filename}' is NOT valid JSON: {e}")
    except Exception as e:
        logging.error(f"Error while reading '{filename}': {e}")