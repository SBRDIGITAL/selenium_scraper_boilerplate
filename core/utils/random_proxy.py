from random import choice


def get_random_proxy(proxy_list:list[str]) -> str|None:
    """
    ## Возвращает случайно выбранную прокси

    ### Args:
        - proxy_list:list[str] — список строк прокси, минимум 1 элемент
    
    ### Return:
        - result:str|None = None(По умолчанию) или если нет прокси
    """

    result:str|None = None
    if proxy_list:
        result = choice(proxy_list)
    
    return result