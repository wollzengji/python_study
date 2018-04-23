# -*- coding: utf-8 -*-
import hashlib


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def login(user, password):
    md5Password=db[user]
    if md5Password==md5(password):
        return True
    return False

s=login('michael','123456');
print(s)