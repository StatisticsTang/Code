# 由Ajax请求实现页面局部刷新，而在翻译框中录入文字时会自动进行Ajax请求
# 检查-Network-XHR-Payload里看From Data，就是参数data;
# 而Headers里的Request_URL就是所需的post_url
import requests
import json
if __name__ == '__main__':
    # 1.指定url,加前缀post说明url性质
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
   # 3.post请求参数处理（同get请求一致） 
    word = input("enter a word: ")
    data = {
        'kw':word
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    
    # 5.获取响应数据
    # 响应数据是一组字典对象的json数据，然而response.text是获取字符串形式的json串，可以直接用方法text作为字符串储存
    # 也可以调用.json，直接返回的是obj对象，也就是原来的字典对象。如果确认服务器响应数据是json数据才可使用，否则不行
    # 如何确认响应数据，在抓包工具中，Headers-Response Headers-Content-Type中查看
    result_text = response.json()
    print(result_text)  # 可以print查看dic_obj确认一下再持久存储，持久化可直接存入json文件
    filename = data['kw'] + '.json' # data['kw’]同word
    # fp = open('/Users/tangchencheng/Desktop/Code/Python/Result/' + filename, 'w', encoding='utf-8')也可以
    with open('/Users/tangchencheng/Desktop/Code/Python/Result/' + filename, 'w', encoding='utf-8') as fp:
        json.dump(result_text, fp, ensure_ascii=False) # 拿到的json数据中有中文，而中文不能用其编码，所以False
    
    print('over!')