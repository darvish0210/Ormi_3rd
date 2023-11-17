import requests

HOST = 'http://localhost:8000'

LOGIN_URL = HOST+'/account/login/'
# 로그인

LOGIN_INFO = {
    "email": "yj@ghmail.com",
    "password": "yj123!@#"
}

# 로그인 요청
response = requests.post(LOGIN_URL,data=LOGIN_INFO)


print(response.status_code)
print(response.text)
print(response.json())

token = response.json()['access_token']
# 로그인한 사용자만 들어갈 수 있는 URL에 접속
# headers에 token을 넣어서 보냅니다.
header = {
    'Authorization': 'Bearer ' + token
}

data = {
    'title':'제목',
    'content':'내용',
    'author':1
}

res = requests.get(HOST+'/account/test',headers=header,data=data)
print(res.status_code)
print(res.text)