import json
import requests
from datetime import datetime
import logging
import os

# 函数：获取 API 密钥
def get_api_keys():
    api_keys = []
    while True:
        key = input("请输入 API 密钥（输入'q'退出）：")
        if key == 'q':
            break
        api_keys.append(key)
    return api_keys

# 函数：将 API 密钥写入单独的 JSON 文件
def write_api_keys_to_json(api_keys):
    try:
        for index, key in enumerate(api_keys):
            filename = f"{key[:6]}.json"
            data = {"api_key": key}
            with open(filename, 'w') as json_file:
                json.dump(data, json_file)
    except Exception as e:
        print(f"写入 JSON 文件时发生错误：{e}。请检查文件权限或路径是否正确。")

# 函数：从多个 JSON 文件读取 API 密钥
def read_api_keys_from_json():
    api_keys = []
    files = [f for f in os.listdir() if f.endswith('.json')]
    for filename in files:
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                api_keys.append(data["api_key"])
        except Exception as e:
            print(f"读取 {filename} 时发生错误：{e}。请检查文件是否存在或格式是否正确。")
    return api_keys

# 函数：验证输入
def validate_input(prompt, validator):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print("输入错误，请重新输入。")

# 函数：获取天气数据
def get_weather_data(api_key, query_type, query_value):
    if query_type == "jw":
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={query_value[1]}&lon={query_value[0]}&APPID={api_key}&lang=zh_cn&units=metric"
    elif query_type == "dm":
        url = f"http://api.openweathermap.org/data/2.5/weather?q={query_value}&APPID={api_key}&lang=zh_cn&units=metric"
    else:
        return None

    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return json.loads(resp.text)
        elif resp.status_code == 401:
            logging.error(f"API 密钥 {api_key} 无效。")
            print("API 密钥无效，请检查并重新输入。")
            return None
        else:
            print(f"获取天气信息失败，状态码：{resp.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"网络请求发生错误：{e}。请检查网络连接或 API 服务是否正常。")
        return None
    except json.JSONDecodeError:
        print("无法解析响应数据。")
        return None

# 函数：保存天气信息到文件
def save_weather_info_to_file(data):
    now = datetime.now()
    date_str = now.strftime('%Y%m%d')
    location_name = data['name']
    filename = f"{date_str}_{location_name}.txt"
    suffix = 'a'
    while True:
        try:
            with open(filename, 'x', encoding='utf-8') as file:
                file.write(f"位置：{location_name}\n")
                file.write(f"经纬度：({data['coord']['lon']}, {data['coord']['lat']})\n")
                file.write(f"主要天气：{data['weather'][0]['main']}\n")
                file.write(f"当前气温：{data['main']['temp']}\n")
                file.write(f"体感温度：{data['main']['feels_like']}\n")
                file.write(f"最低气温：{data['main']['temp_min']}\n")
                file.write(f"最高气温：{data['main']['temp_max']}\n")
                file.write(f"日出时间：{datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"日落时间：{datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"气压：{data['main']['pressure']}\n")
                file.write(f"湿度：{data['main']['humidity']}\n")
                file.write(f"海平面气压：{data['main']['sea_level']}\n")
                file.write(f"地面气压：{data['main']['grnd_level']}\n")
                file.write(f"可见度：{data['visibility']}\n")
                file.write(f"风速：{data['wind']['speed']}\n")
                file.write(f"风向：{data['wind']['deg']}\n")
                file.write(f"阵风速度：{data['wind']['gust']}\n")
                file.write(f"云量占比：{data['clouds']['all']}\n")
            break
        except FileExistsError:
            filename = f"{date_str}_{location_name}_{suffix}.txt"
            suffix = chr(ord(suffix) + 1)

# 函数：读取并显示天气信息文件内容
def read_and_display_weather_info_from_file():
    # 获取当前日期
    now = datetime.now()
    date_str = now.strftime('%Y%m%d')
    files = [f for f in os.listdir() if f.startswith(f"{date_str}_") and f.endswith('.txt')]
    if not files:
        print("没有找到相关的天气信息文件。")
        return
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"文件内容：{filename}")
            print(file.read())
            print()

# 函数：判断是否为浮点数
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    
    # 获取 API 密钥并写入单独的 JSON 文件
    api_keys = get_api_keys()
    write_api_keys_to_json(api_keys)

    # 尝试从多个 JSON 文件读取 API 密钥
    api_keys = read_api_keys_from_json()
    if not api_keys:
        print("未从 JSON 文件找到 API 密钥，请手动输入。")
        apikey = input("请输入 API 密钥：")
    else:
        apikey = ''
        data = None  # 初始化 data 变量
        for key in api_keys:
            if key:  # 防止空字符串
                data = get_weather_data(key, mode, query_value)
                if data is not None:
                    apikey = key  # 如果找到了有效的 api_key
                    break
        # 如果所有存储的 API 密钥均无效
        if data is None:
            print("所有存储的 API 密钥均无效，请检查或重新输入。")
            apikey = input("请输入 API 密钥：")
    
    # 获取查询方式
    print("查询方式：\n- jw：按经纬度查询，需输入经度和纬度值。\n- dm：按地名查询，输入地名拼音，可搜到县级地名。")
    mode = validate_input("请输入查询方式：", lambda x: x in ["jw", "dm"])

    # 获取查询值
    if mode == "jw":
        lon = validate_input("请输入经度：", lambda x: isfloat(x))
        lat = validate_input("请输入纬度：", lambda x: isfloat(x))
        query_value = (lon, lat)
    elif mode == "dm":
        place = input("请输入地名拼音：")
        query_value = place

    # 获取天气数据
    data = get_weather_data(apikey, mode, query_value)

    # 保存天气信息到文件
    if data:
        save_weather_info_to_file(data)

    # 读取并显示所有天气信息文件内容
    read_and_display_weather_info_from_file()
 
