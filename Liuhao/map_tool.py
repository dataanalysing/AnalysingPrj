

import requests

##获取地理位置
##参数：经度，纬度
##返回值 ：省份，城市
def get_position(longitude, latitude):
    loc = str.format('{0},{1}',longitude,latitude)
    r = requests.get(url='http://api.map.baidu.com/geocoder/v2/',
                     params={'location': loc, 'ak': '1Ba7PoIq3PACybWOS3EYZIHpUd7ueHWT', 'output': 'json'})
    result = r.json()
    province = result['result']['addressComponent']['province']
    city = result['result']['addressComponent']['city']
    return province , city

print(get_position(31,102))




