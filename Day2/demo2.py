import requests
api_key="c5be11cd431ce5a7f2296ae92445ec5b"
city=input("enter city:")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response =requests.get(url)
print("status:",response.status_code)
weather=response.json()
print(weather)
print("temperature:",weather["main"]["temp"])
print("humidity:",weather["main"]["humidity"])
print("wind sped:",weather["wind"]["speed"])