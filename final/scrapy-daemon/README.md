# Parser: Scrapyd
Чтобы запустить демона:
0) Ставим необходимые библиотеки:
```sh
sudo apt-get install libxml2-dev libxslt-dev 
```
1) создаем виртуальное окружение **Python2** в папке scrapy-daemon/ и устанавливаем зависимости из файла requirements.txt
```sh
virtualenv --python=python2 .env
source .env/bin/activate
pip install -r requirements.txt
```
2) Запускаем демона из консоли, командой: 
```sh
scrapyd
```
3) Даем задания демону из любой консоли.
Основные команды для запуска пауков:
```sh
curl http://localhost:6800/schedule.json -d project=parsers -d spider=yandex -d django_task_id=1 -d query=cat -d pages=2
curl http://localhost:6800/schedule.json -d project=parsers -d spider=google -d django_task_id=1 -d query=cat -d pages=2
curl http://localhost:6800/schedule.json -d project=parsers -d spider=instagram -d django_task_id=1 -d query=cat -d pages=2
```