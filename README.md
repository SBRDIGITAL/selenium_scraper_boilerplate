# Selenium Scraper Boilerplate

## Как использовать

1. Создаём виртуальное окружение:
python.exe -m venv .venv

2. Активируем виртуальное окружение:
.venv/Scripts/activate

3. Устанавливаем зависимости:
pip install -r requirements.txt

4. Если нужна работа с прокси, создаём файл с названием "proxy_list.txt" (без ковычек) в корне проекта:
В файл помещаем данные о прокси в формате username:password:host:port
Каждый новый прокси с новой строки
Например:
stariy:perdun:123:127.0.0.1:8080
ne_stariy:ne_perdun:192.168.0.1:8000

5. Запуск main.py


## Структура проекта:
- **main.py** - основной файл запуска
- **core**:
  - **config**:
    - **settings.py** - файл настроек
  - **driver**:
    - **get_driver.py** - получение объекта браузера
    - **proxy_extension.py** - создание расширения для авторизации прокси
  - **extensions** - модуль для хранения расширений браузера
  - **scrapping** - модуль для парсинга
    - **open_url.py** - открытие ссылок
  - **utils**:
    - **random_proxy.py** - генерация случайного прокси 
    - **read_proxies_file.py** - чтение всех прокси из файла proxy_list.txt


## Зависимости:
- attrs==23.2.0
- beautifulsoup4==4.12.3
- certifi==2024.2.2
- cffi==1.16.0
- h11==0.14.0
- idna==3.7
- outcome==1.3.0.post0
- pycparser==2.22
- PySocks==1.7.1
- selenium==4.20.0
- sniffio==1.3.1
- sortedcontainers==2.4.0
- soupsieve==2.5
- trio==0.25.0
- trio-websocket==0.11.1
- typing_extensions==4.11.0
- urllib3==2.2.1
- wsproto==1.2.0
