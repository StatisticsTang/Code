message = "Hello world"
print(message)

# 在程序中可随时修改变量的值，而python将始终记录变量的最新值
message = "Hello Python Crash Course world"
print(message)

# 存储数据时，方法lower() 很有用。很多时候，你无法依靠用户来提供正确的大小写，
# 因此需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再将其转换为最合适的大小写方式
name = "ada lovelace"
print(name.title())  # 首字母大写显示每个单词
print(name.upper())  # 将字符串大写
print(name.lower())  # 将字符串小写

# 使用+合并字符串,引号中的空格也是合并的内容
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# 合并名字并用title设置格式
print("Hello, " + full_name.title() + "!")

# 或者把整条消息储存在一个变量当中,message中的内容自动拼接为新的字符串
message = "Hello, " + full_name.title() + "!"
print(message)

# 使用制表符来添加空白，可使用字符\t
print("Python")
print("\tPython")

# 在字符串中添加换行符，可用字符\n
print("languages:\nPython\nC\nJavaScript")

# 确保字符串末尾没有空白，可使用rstrip()
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

# 要永久删除字符串的空白，必须将删除操作的结果存回到变量中
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# 剔除字符串开头的空白和两端的空白，用lstrip()和strip()
favorite_language = ' python '
favorite_language.lstrip()
favorite_language.strip()

# 在字符串中使用整数时，需要指出这个整数为字符串
age = 23
message = "Happy " + str(age) +"rd Birthday!"
print(message)