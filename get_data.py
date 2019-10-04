# 버스 정류장 고유ID 검색법

'''
how to get stID + 저상버스

1. https://www.data.go.kr/subMain.jsp#/L3B1YnIvcG90L215cC9Jcm9zTXlQYWdlL29wZW5EZXZEZXRhaWxQYWdlJEBeMDgyTTAwMDAxMzBeTTAwMDAxMzUkQF5wdWJsaWNEYXRhRGV0YWlsUGs9dWRkaTozMjA1NjhiNS1jZDBmLTQyODAtOGI5Ny1iZjUxMmYxNWZlNDkkQF5wcmN1c2VSZXFzdFNlcU5vPTg5Njk3ODkkQF5yZXFzdFN0ZXBDb2RlPVNUQ0QwMQ==
getLowStationByNameList에서 정류장이름(한글) 검색

https://www.data.go.kr/subMain.jsp#/L3B1YnIvcG90L215cC9Jcm9zTXlQYWdlL29wZW5EZXZEZXRhaWxQYWdlJEBeMDgyTTAwMDAxMzBeTTAwMDAxMzUkQF5wdWJsaWNEYXRhRGV0YWlsUGs9dWRkaTo5OWQ5OGM3YS1jNWNiLTQ2YjktYWZiZS1hMTBhODA0OTc2ZGEkQF5wcmN1c2VSZXFzdFNlcU5vPTg5MjIzNDIkQF5yZXFzdFN0ZXBDb2RlPVNUQ0QwMQ==
getLowArrInfoByStIdList에 정류소ID 입력(9자리)

'''

'''
arsIS + 모든 버스
1. xls 파일 검색 혹 앞의 #1에서 받아오기

2. https://www.data.go.kr/subMain.jsp#/L3B1YnIvcG90L215cC9Jcm9zTXlQYWdlL29wZW5EZXZEZXRhaWxQYWdlJEBeMDgyTTAwMDAxMzBeTTAwMDAxMzUkQF5wdWJsaWNEYXRhRGV0YWlsUGs9dWRkaTozMjA1NjhiNS1jZDBmLTQyODAtOGI5Ny1iZjUxMmYxNWZlNDkkQF5wcmN1c2VSZXFzdFNlcU5vPTg5Njk3ODkkQF5yZXFzdFN0ZXBDb2RlPVNUQ0QwMQ==
getStationByUidItem에 정류소ID 입력(5자리)

'''

import requests
from bs4 import BeautifulSoup

key = 'Uvejg0Q58CP9PVj1Pzd1wEbLNJTJ9dvBcK7OixMGJjk96hrRbKjCaBMtDC1UomYOJiis1lROIqHO4aoFwXkj3g%3D%3D'
stID = '103000121'
arsID = '04222'
url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey={key}&arsId={arsID}"

data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

buses = soup.find_all('rtnm')
bus = []
for single_bus in buses:
    bus.append(single_bus.text)

# 이후에 올 1대
times = soup.find_all('arrmsg1')
time = []
for single_time in times:
    time.append(single_time.text)

print(bus)
print(time)


