import requests
import re

def get_flag_from_ctf():
    url = "http://141.85.224.118:5000/send"
    payload = {"message": "just testing"}

    try:
        resp = requests.post(url, data=payload, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error contacting {url}: {e}")
        return

    text = resp.text
    print("=== Server response ===")
    print(text)
    print("=======================")

    m = re.search(r"flag\{.*?\}", text, re.IGNORECASE)
    if m:
        print("Found flag:", m.group(0))
    else:
        b64 = re.search(r"[A-Za-z0-9+/]{20,}={0,2}", text)
        if b64:
            print("Found Base64-looking string:", b64.group(0))

if __name__ == "__main__":
    get_flag_from_ctf()
