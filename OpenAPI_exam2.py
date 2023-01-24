from bs4 import BeautifulSoup
import urllib.request as req

key = '인증키'
contentType = 'xml'
startIndex = '1'
endIndex = '5'
url = 'https://openapi.seoul.go.kr:8088/'+key+'/'+contentType+'/LampScpgmtb/'+startIndex+'/'+endIndex+'/'
#http://openapi.seoul.go.kr:8088/(인증키)/xml/LampScpgmtb/1/5/

savename = 'C:/workspace/edu.xml'
req.urlretrieve(url, savename)

xml = open(savename, 'r', encoding = 'utf-8').read()
soup = BeautifulSoup(xml, 'xml')

pjList = []
for itemList in soup.find_all('row') :
    up_nm = itemList.find('UP_NM').string
    up_nm = '없음' if up_nm is None else up_nm
    pgm_nm = itemList.find('PGN_NM').string
    pgm_nm = '없음' if pgm_nm is None else pgm_nm
    target_nm = itemList.find('TARGET_NM').string
    target_nm = '없음' if target_nm is None else target_nm
    u_price = itemList.find('U_PRICE').string
    u_price = '없음' if u_price is None else u_price
    pjList.append((up_nm, pgm_nm, target_nm, u_price))
print('[서울 청소년수련관 강좌 리스트]')
for up_nm, pgm_nm, target_nm, u_price in pjList :
    print(up_nm+', '+pgm_nm+', '+target_nm+', '+str(u_price))