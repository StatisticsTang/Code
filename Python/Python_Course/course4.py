# if语句简单示例
from matplotlib.style import available
from requests import request


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 注意：条件测试在终端不能直接输出True和False，必须print

# 最简单的条件测试：检查变量的值是否与特定值相等
car = 'bmw'
car == 'bmw'
car == 'audi'

# 检查相等时区分大小写
car = 'Audi'
car == 'audi'

# 如果剔除大小写影响，可将变量的值转换为小写再比较
car = 'Audi'
car.lower() == 'audi'
print(car)  # lower不会修改储存在car中的值

# 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies！")

# 比较数字
age = 18
age == 18

# 检查数字是否不等
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 用and检查多个条件
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_1 = 22
age_0 >= 21 and age_1 >= 21
# 为改善可读性，可将每个测试都分别放在一对括号内
(age_0 >= 21) and (age_1 >= 21)

# 用or检查多个条件
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
age_0 = 18
age_0 > 21 or age_1 >= 21

# 检查特定值是否包含在列表中用in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

# 检查特定值是否不包含在列表中用not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 布尔表达式，通常用于记录条件
game_active = True #游戏是否在运行：是
can_edit = False #用户是否可以编辑：否

'''
最简单的if语句只有一个测试和一个操作：
if conditional_test:
    do something
'''

age = 19
if age >= 18:
    print("You are old enough to vote!")

# 缩进的作用与for循环相同，通过测试后将执行所有缩进代码行
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else结构【依次】检查多个代码块
age = 12

if  age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 为使代码更简洁，可不在if代码块中打印门票价格，而是在if中设置价格，最后打印
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# 使用多个elif代码块,给老年人打折
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# 省略else代码块：python并不要求if-elif结构后面必须有else
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# 测试多个条件，即需要在每个条件为True时都采取相应措施
# 如果使用if-elif结构，代码将不能正确运行
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 结合for循环
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making you pizza!")

# 检查特殊元素
# 如果green peppers用完了，可在for中包含if语句
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
    
print("\nFinished making your pizza!")

# 在if语句中将列表名用在条件表达式中时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 使用多个列表
available_toppings = ['mushroom', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping +".")
    
print("Finished making your pizza!")




