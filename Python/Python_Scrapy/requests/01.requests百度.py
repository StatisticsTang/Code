#- 需求：爬取百度首页的页面数据
# 对于Java、C、C++，每次开启一个程序，都必须写一个主函数作为程序的入口，也就是我们常说的main函数
# 与Java、C、C++等几种语言不同的是，Python是一种解释型脚本语言，在执行之前不同要将所有代码先编译成中间代码
# Python程序运行时是从模块顶行开始，逐行进行翻译执行，所以，最顶层（没有被缩进）的代码都会被执行
# 所以Python中并不需要一个统一的main()作为程序的入口
# 在某种意义上讲，“if __name__==’__main__:”也像是一个标志，象征着Java等语言中的程序主入口
# 告诉其他程序员，代码入口在此——这是“if __name__==’__main__:”这条代码的意义之一。
import requests

# import文件内的if name = main不会执行，主程序内的代码if name = main会执行
if __name__ == '__main__':
    # step 1:指定url
    url = 'https://www.baidu.com/'
    # step 2:发起请求，get方法会返回一个响应对象
    response = requests.get(url=url)
    # step 3:获取响应数据，text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # step 4:持久化存储
    with open('/Users/tangchencheng/Desktop/Code/Python/Result/baidu.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print("爬取数据结束！")