import os
import traceback

from core.config.settings import proxy_file_name


def read_proxy_list(proxy_file:str = proxy_file_name) -> list[str]:
    """
    ## Считывает все прокси с каждой новой строки из .txt файла.\
    Формат строки username:password:host:port

    ### Args:
        - proxy_file_name:str = os.path.join('proxy_list.txt') - путь до файла с всеми прокси

    ### Return:
        - proxy_list:list[str] - список с проксями или без проксей
    """

    proxy_list = []  # Список если нет файла

    if os.path.exists(proxy_file):
        try:  # Получаем список с проксями
            with open(proxy_file, mode='r', encoding='utf-8') as pf:
                proxy_list:list[str] = pf.read().splitlines() 
        except:
            traceback.print_exc()

    return proxy_list
