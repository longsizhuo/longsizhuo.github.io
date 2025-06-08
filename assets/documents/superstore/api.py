import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=SGD&amount=1"
payload = {}
headers = {
    "apikey": "2Okp4TzXM6k03WdKNGF5UJPXKkA68faM"
}
r = requests.request("GET", url, headers=headers, data=payload)  # 响应API
# 查看响应结果
print("Status code:", r.status_code)
# 返回内容为json格式文件
# 将API响应存储在一个变量中
# json()函数仅解码json格式返回
response_dict = r.json()
# print(response_dict)
# 处理结果  获得响应字典
# 探索有关仓库的信息  response_dict字典的嵌套
# print(response_dict['info']['rate'])

f = open("summary_report.txt", "w")
head = [
    "=================================================\n"
    "SINGAPORE TO US DOLLAR EXCHANGE RATE IN REAL TIME\n"
    "=================================================\n"
]
f.writelines(head)
f.writelines([str(response_dict['info']['rate'])+"\n"])
f.close()
print("over")
