import os
import api_consts

def get_gemini_key():
    key = os.environ.get(api_consts.GEMINI_API_KEY)
    if not key:
        print(f"ERROR: Pleaset set your {api_consts.GEMINI_API_KEY} environment variable.")
        return None

    return key

def get_gemini_url():
    url = os.environ.get(api_consts.GEMINI_API_URL)
    if not url:
        print(f"ERROR: Pleaset set your {api_consts.GEMINI_API_URL} environment variable.")
        return None

    return url