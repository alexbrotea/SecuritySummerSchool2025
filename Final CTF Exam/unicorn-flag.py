from subprocess import check_output, Popen, PIPE

prefix = b"42"

Popen([
    "./md5_chosen_prefix_coll",
    "--prefix1=prefix1.bin", "--prefix2=prefix2.bin",
    "--out1=msg1.bin", "--out2=msg2.bin"
]).wait()

import requests
url = "http://ctf-13.security.cs.pub.ro:8000/"
with open("msg1.bin","rb") as f1, open("msg2.bin","rb") as f2:
    r = requests.post(url, files={
        'val1': ('msg1.bin', f1, 'application/octet-stream'),
        'val2': ('msg2.bin', f2, 'application/octet-stream'),
    })
print(r.text)
