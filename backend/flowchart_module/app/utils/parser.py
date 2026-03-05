import json
import re


def extract_valid_json(text: str):
    """
    Extracts the first valid JSON block from a string.
    Handles 'Extra data' errors by stopping at the first complete JSON object.
    """
    try:
        # Try direct load first
        return json.loads(text.strip())
    except:
        # Use non-greedy regex to find the first balanced JSON block
        # This prevents 'Extra data' errors when LLM adds text after JSON
        match = re.search(r"(\{.*?\})", text, re.DOTALL)
        
        if not match:
            # Fallback for multi-line JSON
            match = re.search(r"(\{.*\})", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except:
                # If still fails, try to find the very first '{' and last '}'
                start = text.find('{')
                end = text.rfind('}')
                if start != -1 and end != -1:
                    try:
                        return json.loads(text[start:end+1])
                    except:
                        pass
        
        raise ValueError("Could not parse valid JSON from LLM output. Response was: " + text[:100])