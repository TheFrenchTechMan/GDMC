import requests

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
        return r.text.split(":")[3]

def get_latest_comment(user_id):
    data = {
        "accountID": user_id,
        "page": 0,
        "secret": "Wmfd2893gb7"
    }

    headers = {
        "User-Agent": "",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    url = "http://www.boomlings.com/database/getGJAccountComments20.php"
    r = requests.post(url, data=data, headers=headers)
    
    return r.text

print(get_user_id("TFTM"))
print(get_latest_comment(147721662))