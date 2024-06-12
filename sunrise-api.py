import requests
import datetime

MyLat=10.786999
MyLang=79.137825
parameters={
    'lat':MyLat,
    'lng':MyLang,
    "formatted":0
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
data=response.json()
print(data)
sunrise=data['results']['sunrise'].split("T")[1].split(":")[0]
sunset=data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now=datetime.datetime.now()
print(time_now.hour)
response.raise_for_status()
