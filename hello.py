# -*- coding: utf-8 -*-

import requests ##导入requests

#name = input('please enter your name: ')
#print('hello,', name)


UserAgent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
Referer= "http://www.mzitu.com/"
#Accept="image/webp,image/apng,image/*,*/*;q=0.8"
#AcceptEncoding="gzip, deflate"
#AcceptLanguage="en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
#Connection="keep-alive"
#Host="i.meizitu.net"

#headers = {"User-Agent":UserAgent,"Referer":Referer,"Accept":Accept,"Accept-Encoding":AcceptEncoding,"Accept-Language":AcceptLanguage,"Connection":Connection,"Host":Host}
headers = {"User-Agent":UserAgent,"Referer":Referer}
img_url="http://i.meizitu.net/2018/04/15b02.jpg"
img = requests.get(img_url,headers=headers)
f = open('3.jpg', 'ab')  ##写入多媒体文件必须要 b 这个参数！！必须要！！
f.write(img.content)  ##多媒体文件要是用conctent哦！
f.close()