#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'  # 删除掉op=keyword
    param = {
        'op': 'keyword',  # 位于Query String Parameters
        'cname': '',  # 注意复制过来时都要加引号和逗号
        'pid': '',
        'keyword': '南京',  # 城市可以设置为动态的参数
        'pageIndex': '1',  # 不同城市的页数不一样，因此也可以设为动态的
        'pageSize': '10',  # 每页显示的数据条数
    }
    headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = requests.post(url=url, params=param, headers=headers)
    result = response.text  # Content-Type是text数据类型 
    filename = 'KFC.html'  # 文件名要加引号，并且后缀不是text，应为html
    with open('/Users/tangchencheng/Desktop/Code/Python/Result/' + filename, 'w', encoding='utf-8') as fp:
        fp.write(result)
    print("over!")