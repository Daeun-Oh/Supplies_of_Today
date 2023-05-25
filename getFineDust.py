#-*-coding:utf-8-*-
from urllib.request import Request, urlopen
import json
import datetime


service_key = "89d61ef6b4bbaeb66f8114007e4a9c08"


def getNowAirPollution(pos_lat, pos_lon):
    # API 요청시 필요한 인수값 정의
    ow_api_url = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}".format(pos_lat, pos_lon,service_key)

    print(ow_api_url)
    # API 요청하여 데이터 받기
    request = Request(ow_api_url)
    response_body = urlopen(request).read()  # get bytes data
    # print(response_body)
    decode_data = response_body.decode('utf-8')
    print(decode_data)

    # 받은 값 JSON 형태로 정제하여 반환
    data = json.loads(decode_data)
    print(data)
    print("============================")
    print("대기질 심각 레벨 : %r" % data['list'][0]['main']['aqi'])
    print("============================")
    print("[상세정보]")
    print("초미세먼지 :", data['list'][0]['components']['pm2_5'])
    print("미세먼지 :", data['list'][0]['components']['pm10'])
    print("============================")

    unix_timestamp = data['list'][0]['dt']

    # Unix 시간을 UTC datetime으로 변환
    utc_datetime = datetime.datetime.utcfromtimestamp(unix_timestamp)

    # UTC datetime을 한국 시간대로 변환
    korea_timezone = datetime.timezone(datetime.timedelta(hours=9))  # 한국 시간대 (UTC+9)
    korea_datetime = utc_datetime.astimezone(korea_timezone)

    # 한국 시간 출력 형식
    korea_time_format = "%Y년 %m월 %d일 %p %I시 %M분 %S초"

    # 한국 시간 출력
    korea_time_str = korea_datetime.strftime(korea_time_format)
    print(korea_time_str)

    return data['list'][0]['components']['pm2_5'], data['list'][0]['components']['pm10']


#getNowAirPollution("37.5488", "126.6578")