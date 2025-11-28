import requests

def get_ip_info():
    print("正在获取 IP 信息...")
    try:
        res = requests.get("https://ipinfo.io/json")
        print(res.text)
    except:
        print("获取 IP 信息失败")
