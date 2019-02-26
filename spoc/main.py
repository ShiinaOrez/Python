import requests
from spoc_test import connect

USERNAME = "..."
PASSWORD = "..."

HEADER = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "spoc.ccnu.edu.cn",
    "Origin": "http://spoc.ccnu.edu.cn",
    "Referer": "http://spoc.ccnu.edu.cn/studentHomepage",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}

def login_once():
    code = ""
    session = requests.Session()
    session.get("http://spoc.ccnu.edu.cn/starmoocHomepage", headers = HEADER)
    response = session.get("http://spoc.ccnu.edu.cn/userLoginController/getVerifCode")
    print(response.headers)
    q = response.json().get("data")
    result = connect(q)
    for reg in result.get("Result").get("regions"):
        for line in reg.get("lines"):
            for w in line.get("words"):
                if w.get("word") is not None:
                    code = w.get("word")
                    print(code)
                    break
    if len(code) < 4:
        print("[log]Length too Short!")
    payload = {
        "loginName": USERNAME,
        "password": USERNAME,
        "verifCode": code
    }
    response = session.post(
        "http://spoc.ccnu.edu.cn/userLoginController/userLogin",
        data = payload)
    response = session.get("http://spoc.ccnu.edu.cn/studentHomepage")
    if "assignmentUserId" in response.text:
        print("Y")

if __name__ == "__main__":
    login_once()
