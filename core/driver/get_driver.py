import traceback

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions

from core.driver.proxy_extension import proxies_ext
from core.utils.random_proxy import get_random_proxy
from core.utils.read_proxies_file import read_proxy_list



def get_driver(headless: bool = False) -> Chrome:
    """
    ## Получает объект Chrome из selenium.webdriver, открывает окно на весь экран.\
    Объект подключается к прокси, если read_proxy_list вернул не пустой список

    ### Args:
        - headless: bool = False(По умолчанию) - режим работы браузера с окном или без

    ### Return:
        - WebDriver(Chrome) Controls the ChromeDriver and allows you to drive the browser
    """

    options = ChromeOptions()
    options.add_argument("--start-maximized")
    
    if headless:
        options.add_argument("--headless")  # Запуск в режиме headless
        options.add_argument("--disable-gpu")  # Отключение использования GPU


    proxy_list:list[str] = read_proxy_list()  # Получаем все прокси
    proxy:str = get_random_proxy(proxy_list)  # Получаем рандомную прокси

    if proxy:  # С прокси
        print('[INFO] ЗАПУСК БРАУЗЕРА БУДЕТ С ПРОКСИ')
        proxy_split:list[str] = proxy.split(":")
        username, password, host, port = proxy_split
        
        try:  # Подключаем расширение с проксёй
            proxies_extension:str = proxies_ext(username, password, host, port)
            options.add_extension(proxies_extension)

        except:
            traceback.print_exc()
        
        finally:
            driver = Chrome(options=options)

    else:  # Без прокси
        print('[INFO] ЗАПУСК БРАУЗЕРА БЕЗ ПРОКСИ')
        driver = Chrome(options=options)

    return driver
