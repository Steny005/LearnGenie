import json
import re


def extract_valid_json(text: str):

    try:
        return json.loads(text)

    except:

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            return json.loads(match.group())

        raise ValueError("No valid JSON found")