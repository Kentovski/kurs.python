Отделенный от основного проекта, демон Scrapy.
Чтобы запустить демона:
1) Активируем виртуальное окружение в папке .env2
sh```
source .env2/bin/activate
```
2) Запускаем демона из консоли, командой: 
sh```
scrapyd
```
3) Даем задания демону из любой консоли.
Основные команды для запуска пауков:
sh```
curl http://localhost:6800/schedule.json -d project=parsers -d spider=yandex -d django_task_id=1 -d query=cat -d pages=2
curl http://localhost:6800/schedule.json -d project=parsers -d spider=google -d django_task_id=1 -d query=cat -d pages=2
curl http://localhost:6800/schedule.json -d project=parsers -d spider=instagram -d django_task_id=1 -d query=cat -d pages=2
```