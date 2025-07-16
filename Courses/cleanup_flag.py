import requests, json, re, pprint

URL = "http://141.85.224.115:7004/api-v3/get-user-records.php"

outer = requests.get(URL).json()
payload = json.loads(outer[0])

print(f"[+] Am primit {len(payload)} obiecte")

flag_re = re.compile(r'(SSS)\{[^}]+\}')
for user in payload:
    for v in user.values():
        if isinstance(v, str) and flag_re.search(v):
            print(flag_re.search(v).group(0))
