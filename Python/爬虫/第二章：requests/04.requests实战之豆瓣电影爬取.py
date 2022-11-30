# 爬取电影信息，也是局部信息，也会用到数据解析，但也跟百度翻译类似，可以通过Ajax请求，获取json形式电影详情数据
# 判断是否为Ajax请求，发起请求后地址有没有变，如果变了则不是Ajax请求
# 当滚轮拖动到底部时，发起了Ajax请求，地址没变，但加载出了一批新的电影数据，通过抓包工具XHR验证（先打开抓包工具，再滑动滚轮）
# 捕获到ajax请求所对应的数据包，点开可查看url和Request_Method(Get或Post)
# 在payload-Query_string_Parameters可查看携带的参数
# 在Header-Content_Type中确定数据类型为json,Resonpse中可查看详情数据
import requests
import json 

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list?'  # url携带了参数，需在指定时删去，要使用字典的方式进行封装
    # 参数地址栏有，string_Parameters中也有，直接粘贴后者中的参数
    param = {
        'type': '24',  # 键和值都需加引号转换位字符串
        'interval_id': '100:90',
        'action': '',  # 没有值的情况应添加引号
        'start': '1',  # 从库中第几部电影去取，索引可能从0开始，为1时取到第二部电影
        'limit': '20',  # 一次取出的个数
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()  # 查看response发现是列表格式，命名前缀为list
    filename = 'douban.json'
    with open('/Users/tangchencheng/Desktop/Code/Python/Result/' + filename, 'w', encoding='utf-8') as fp:
        json.dump(list_data, fp, ensure_ascii=False)

    print("over!")

    # 完毕之后打开生成的json文件，复制结果到json校验格式化工具中查看