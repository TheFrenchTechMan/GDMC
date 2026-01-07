import base64
import requests
from utils import tuples_to_dict

def get_user_id(username):
    data = {
        "str": username,
        "secret": "Wmfd2893gb7"
    }
    
    headers = {
        "User-Agent": "",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    url = "http://www.boomlings.com/database/getGJUsers20.php"
    r = requests.post(url=url, data=data, headers=headers)
    
    if r.status_code == 403:
        return None
    else:
        return tuples_to_dict(r.text.split(":"))["16"] #Key 16 is AccountID

def get_latest_comment(account_id):
    data = {
        "accountID": account_id,
        "page": 0,
        "secret": "Wmfd2893gb7"
    }

    headers = {
        "User-Agent": "",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    url = "http://www.boomlings.com/database/getGJAccountComments20.php"
    r = requests.post(url, data=data, headers=headers)
    
    return base64.b64decode(r.text.split("~")[1]).decode()

print(get_user_id("TFTM"))
print(get_latest_comment(13896382))