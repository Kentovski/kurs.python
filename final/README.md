# Домашнее задание: "Агрегатор картинок"
Проект состоит из 4-х отдельных частей:
1) Front-end: выполнен на Angular 2 и находится в папке frontend.
2) Back-end: выполнен на Django и находится в папке backend.
3) Parser: выполнен на Scrapyd и находится в папке scrapy-daemon.
4) База данных: выполнен на Mysql и ни в какой папке не находится.

База данных ставится командой: 

```sh
sudo apt-get install mysql-server libmysqlclient-dev
```
В конфигах Django и Scrapyd прописаны: 
login: root
password: adminadmin
По желанию можно загрузить в базу фикстуры из папки:
```sh
backend/exam/agregator/fixtures/
```
