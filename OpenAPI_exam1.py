from bs4 import BeautifulSoup
import urllib.request as req

busNum = '360'
key = '인증키'
url1 = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRoutelist?serviceKey='+key+'&strSrch='+busNum
savename = 'C:/workspace/businfo.xml'
req.urlretrieve(url1, savename)

xml = open(savename, 'r', encoding = 'utf-8').read()
soup = BeautifulSoup(xml, 'xml')

busRouteId = None
for itemList in soup.find_all('itemList') :
    busRouteId = itemList.find('busRouteId').string
    busRouteNm = itemList.find('busRouteNm').string
    if busRouteNm == busNum :
        break

url2 = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStationByRoute?ServiceKey='+key+'&busRouteId='+busRouteId

savename = 'C:/workspace/buspos.xml'
req.urlretrieve(url2, savename)

xml = open(savename, 'r', encoding = 'utf-8').read()
soup = BeautifulSoup(xml, 'xml')

busPos = []
for itemList in soup.find_all('itemList') :
    gpsY = itemList.find('gpsY').string
    gpsX = itemList.find('gpsX').string
    
    busPos.append((gpsY, gpsX))
    
print('[' + busNum + ' 번 버스의 운행 위치 ]')
if len(busPos) != 0 :
    print(busNum + '번 버스 ' + str(len(busPos))+'대 운행 중...')
    for lat, lng in busPos :
        print(lat+','+lng)
else :
    print('현재 운행 중인 '+busNum+'번 버스가 없어요...')