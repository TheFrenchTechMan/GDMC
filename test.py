import json
import os
import random as rnd
import string
from reqs import *

CODES_FILE_LOCATION = os.path.join(os.getcwd(), "codes.json")

def create_code(username):
    acc_id = get_account_id(username)
    if acc_id is None:
        return None
    
    text = "".join([rnd.choice(string.ascii_letters) for _ in range(16)])
    
    if not os.path.exists(CODES_FILE_LOCATION):
        with open(CODES_FILE_LOCATION, "x") as f:
            json.dump([], f, indent=4)
    
    with open(CODES_FILE_LOCATION, "r+") as f:
        data = json.load(f)
        print(data)
        users = []
        for dict in data:
            users.append(dict["username"])
        if username not in users:
            data.append({
                "username": username,
                "code": text
            })
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=4)
        else:
            text = next((d for d in data if d.get("username") == username), None)["code"]
    
    print(f"Please post \"{text}\" as a comment on your Geometry Dash profile to verify ownership. Press Return when done.")

def verify_code(username: str) -> bool:
    acc_id = get_account_id(username)
    comment = get_latest_comment(acc_id)
    with open(CODES_FILE_LOCATION, "r") as f:
        data = json.load(f)
        code = next((d for d in data if d.get("username") == username), None)["code"]
    print(comment)
    if code == comment:
        return True
    else:
        return False


create_code("TFTM")
input()
print(verify_code("TFTM"))