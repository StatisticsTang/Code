#UA：User-Agent（请求载体的身份标识）
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
#说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标识不是基于某一款浏览器的，则表示该请求
#为不正常的请求（爬虫），则服务器端就很有可能拒绝该次请求。

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests

if __name__ == '__main__':
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    url = 'https://www.baidu.com/s?'  # wd可以是中文，但复制过来会乱码，需手动修改
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word: ')  # 使字典是动态的，需用input
    param = {
        'wd':kw
    }
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    filename = kw + '.html'
    with open('/Users/tangchencheng/Desktop/Code/Python/Result/' + filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    
    print(filename,'保存成功！')