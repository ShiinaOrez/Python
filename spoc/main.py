import requests
from spoc_test import connect
from pprint import pprint

USERNAME = "2017211712"
PASSWORD = "2017211712"

HEADER = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Access-Control-Allow-Headers": "X-Requested-With",
    "Host": "spoc.ccnu.edu.cn",
    "Content-Type": "application/json",

    "Origin": "http://spoc.ccnu.edu.cn",
    "Referer": "http://spoc.ccnu.edu.cn/studentHomepage",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
}

LOGIN = [
#    "http://spoc.ccnu.edu.cn/userLoginController/checkLogin",
    "http://spoc.ccnu.edu.cn/userLoginController/getUserProfile",
    "http://spoc.ccnu.edu.cn/userInfo/getUserInfo",
]

def get_site(session, userId):
    payload = {
        "pageNum": 1,
        "pageSize": 4,
        "termCode": "201901",
        "userId": userId
    }
    pprint(session.cookies)
    response = session.post("http://spoc.ccnu.edu.cn:80/studentHomepage/getMySite", data=payload, headers=HEADER)
    with open("415.html", "w") as f:
        f.write(response.content.decode("utf-8"))

def get_info(session, userId):
    response = session.get("http://spoc.ccnu.edu.cn/userInfo/getUserInfo")
    pprint(response.json())

def get_unsubmit(session, userId):
    payload = {
        "userId": userId,
    }
    response = session.post("http://spoc.ccnu.edu.cn:80/assignment/getUnSubmitDetailByStu", data=payload, headers=HEADER)
    pprint(response.__dict__)

def get_class(session, userId):
    param = {
        "userId": userId,
    }
    response = session.get("http://spoc.ccnu.edu.cn/api/friend/getInitList", params=param)
    pprint(response.json())

def login_once():
    code = ""
    session = requests.Session()
    response = session.get("http://spoc.ccnu.edu.cn/userLoginController/getVerifCode")
#    print(session.cookies)
#    q = response.json().get("data")
#    result = connect(q)
#    print(result)
#    for reg in result.get("Result").get("regions"):
#        for line in reg.get("lines"):
#            for w in line.get("words"):
#                if w.get("word") is not None:
#                    code = w.get("word")
#                    print(code)
#                    break
#    if len(code) < 4:
#        print("[log]Length too Short!")

    payload = {
        "loginName": USERNAME,
        "password": PASSWORD,
#        "verifCode": code
    }
    for url in LOGIN:
        response = session.post(url, data=payload)
    userInfo = response.json()
    pprint(session.cookies)
    uid = userInfo.get("data").get("userInfoVO").get("id")
    print("UserID:", uid)
    get_class(session, uid) #获取参与课堂
#    get_unsubmit(session, uid) #获取未提交信息
    get_info(session, uid) #获取个人信息
#    get_site(session, uid)

if __name__ == "__main__":
    login_once()
