import crawling
import folium
import json
import mpu


# 지도 초기 화면 어떻게 보여줄지 설정 (위치, 확대, 가로/세로 길이 등)
map = folium.Map(location=[36.501, 127.870], zoom_start=7, height = '100%')

for site in sites:
# 위도, 경도 파악
    site_geodata = geolocator.geocode(site)
    site_loc = [site_geodata.latitude, site_geodata.longitude]
           
        # 지도에 마커 찍기
    folium.Marker(location=site_loc, popup=site).add_to(map)

map
