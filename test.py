import random as rnd
import string
from reqs import *

def verify_account(username):
    acc_id = get_account_id(username)
    if acc_id is None:
        return None
    
    text = "".join([rnd.choice(string.ascii_letters) for _ in range(16)])
    print(f"Please post \"{text}\" as a comment in your Geometry Dash profile to verify ownership. Press Return when done.")
    input()
    comment = get_latest_comment(acc_id)
    print(comment)
    if text == comment:
        print("Ownership verified! You can now delete the comment.")
    else:
        print("huh")

verify_account("TFTM")