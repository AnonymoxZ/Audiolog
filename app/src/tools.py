# utils functions and validators
import requests
import unicodedata

def confirm_request(url:str) -> bool:
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return True
        else:
            return False
    except Exception as err:
        print(f'ERROR confirm_request(url:str): {err}')
