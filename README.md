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