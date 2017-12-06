# -*- coding: utf-8 -*-
import os
import time
import json
import codecs

file = codecs.open('infolist.json','r','utf-8')
lines = [line.strip() for line in file] 
file.close()
i = 0
for li in lines:
    info = json.JSONDecoder().decode(li)
    for url in info['url']:
        cur_path = os.path.split(os.path.realpath(__file__))[0]
        cmd = 'cd ' + cur_path + '| scrapy crawl infodetail -a tag=' + url
        os.system(cmd)
        i = i + 1
        print(cur_path)
        print(url)
        print(i)
        time.sleep(2)
        # if i > 0:
        #     break
        
        # if i > 3:
        #     break
