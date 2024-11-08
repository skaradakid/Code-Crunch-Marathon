import requests
import json

weather = []
def get_forcast():
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=0a5c8cddaabe8569eaba97d90f2d4e8a")
    data = response.json()

    with open("data.json", 'w') as f:
        json.dump(data,f,indent=2)
    print(data)

    for x in data:
        if x == 'weather':
            for y in data[x][0]:
                if y == 'main' or y == 'description':
                    weather.append(data[x][0][y])
get_forcast()
print(weather)