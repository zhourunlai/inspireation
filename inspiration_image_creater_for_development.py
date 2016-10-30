# coding:utf-8

import os
import urllib2
import urllib
import re
import random
import json

import jieba
import jieba.analyse


def associate_others(query):
    gjc = urllib.quote(query)
    url = "http://sug.so.360.cn/suggest/word?callback=suggest_so&encodein=utf-8&encodeout=utf-8&word=" + gjc
    headers = {
        "GET": url,
        "Host": "sug.so.360.cn",
        "Referer": "http://www.so.com/",
        "User-Agent": "sMozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17",
    }

    # 特别提示，下面这个list中的代理ip可能失效，请换上有效的代理ip
    # iplist = ['27.24.158.153:81', '46.209.70.74:8080', '60.29.255.88:8888']
    # ip = random.choice(iplist)
    # proxy_support = urllib2.ProxyHandler({'http': 'http://' + ip})
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)
    req = urllib2.Request(url)

    for key in headers:
        req.add_header(key, headers[key])

    html = urllib2.urlopen(req).read()

    ss = re.findall("\"(.*?)\"", html)
    # for item in ss:
    #     print item
    return ss


def find_element(query):
    # query = urllib.unquote(query)
    if '树' in query:
        random_num = random.randint(1, 26)
        path = 'element/shu' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(350, 400)
        return path, x, y
    if '草' in query:
        random_num = random.randint(1, 5)
        path = 'element/cao' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(400, 460)
        return path, x, y
    if '山' in query:
        random_num = random.randint(1, 3)
        path = 'element/shan' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(300, 400)
        return path, x, y
    if '云' in query:
        random_num = random.randint(1, 5)
        path = 'element/yun' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(50, 150)
        return path, x, y
    if query.find('太阳') != -1:
        random_num = random.randint(1, 5)
        path = 'element/taiyang' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(30, 80)
        return path, x, y
    if query.find('海水') != -1:
        random_num = random.randint(1, 2)
        path = 'element/haishui' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(300, 400)
        return path, x, y
    if query.find('房子') != -1:
        random_num = random.randint(1, 1)
        path = 'element/fangzi' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(300, 400)
        return path, x, y
    if query.find('植物') != -1:
        random_num = random.randint(1, 4)
        path = 'element/zhiwu' + str(random_num) + '.svg'
        x = random.randint(0, 460)
        y = random.randint(300, 400)
        return path, x, y
    return 'element/zhiwu1.svg'


def main(content):
    # content = '我想要一幅充满树和草的世界的画'
    tags = jieba.analyse.extract_tags(content, topK=1)
    for item in tags:
        query = item.encode("utf-8")
        path, x, y = find_element(query)
        return query, path

# if __name__ == '__main__':
#     main()
