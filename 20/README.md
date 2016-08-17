# Домашнее задание: "Эмулятвы битвы с API"
1) Устанавливаем NodeJS и npm (если отсутствует). Подробнее здесь: https://nodejs.org/en/download/

2) Заходим в папку frontend
```sh
cd frontend
```
3) Выполняем команды по очереди
```sh
npm install
npm start
```
Должна открыться вкладка в браузера с адресом: http://localhost:3000/

4) Заходим в папку backend
```sh
cd ..
cd backend
```
5) Создаем виртуальное окружение и активируем его
```sh
virtualenv --python=python3 .env
source .env/bin/activate
```
6) Устанавливаем необходимые зависимости
```sh
pip install -r requirements.txt
```
7) Запускаем приложение
```sh
python3 battlenet_Flk.py
```
8) Переходим на вкладку с http://localhost:3000/ и проверяем работу приложения.