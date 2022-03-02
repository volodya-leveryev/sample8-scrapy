# Создание набора данных путем скачивания страниц с сайта

Установка:

```
python -m venv venv
venv\scripts\activate.bat
pip install scrapy
```

Запуск краулера:

```
scrapy crawl news_ykt -O news.json
```
