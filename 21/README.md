# Домашнее задание: "Автомагазин с API"

Главная страница API доступна по адресу: http://127.0.0.1:8000/api/

Запрос на добавление данных выполняется таким образом в Python консоли:
```sh
import requests
requests.post('http://127.0.0.1:8000/api/auto/',data={"manufacturer": 2,"name": "6 Gran Turismo","body": "hatchback","fuelType": "diesel","fuelRate": 6.6,"engineVolume": 1.5,"enginePower": 6,"gearbox": "auto","year": "2016-01-01"}, auth=('admin', 'adminadmin'))
```