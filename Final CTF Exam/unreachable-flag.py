import requests

url = 'http://ctf-13.security.cs.pub.ro:8003/'

params = {
    'whoIsTheBest': 'SecuritySummerSchoolSecuritySummerSchool'
}

try:
    response = requests.get(url, params=params, timeout = 5)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(e)
