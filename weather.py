import requests

def get_weather(city):
    if not city:
        print("请输入城市名称")
        return

    print(f"查询天气：{city}")

    # 使用公开 API 示例
    url = f"https://wttr.in/{city}?format=3"
    try:
        res = requests.get(url)
        print(res.text)
    except:
        print("天气查询失败，请检查网络连接。")
