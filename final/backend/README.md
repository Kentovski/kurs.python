# Backend: Django
1) создаем виртуальное окружение в папке backend/ и устанавливаем зависимости из файла requirements.txt
```sh
virtualenv --python=python3 .env
source .env/bin/activate
pip install -r requirements.txt
```
2) Перед запуском сервера Django, следует обратить внимание на настройки в backend/exam/exam/settings.py
3) В файле: exam/agregator/fixtures/initial_data.json содержится фикстура для начальной инициализации базы данных. Загрузить ее можно следующей командой:
```sh
./manage.py loaddata initial_data.json
```