# 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 字典是一系列键-值对，每个键都与一个值相关联，你可以使用键来访问与之相关联的值
# 在字典中，储存多少个键-值对都可以

# 访问字典中与键相关的值，可依次指定字典名和放在方括号内的键
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
# 当击杀了这个外星人，就可以使用下面代码确定玩家应获得多少分
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")

'''
可利用关键字代替索引的方法访问字典
字典是一种动态结构，可随时添加键-值对
要添加键-值对，可依次指定字典名、用方括号括起的键和相应的值
键-值对的排列顺序可能与添加顺序不同，python不关心键-值对的添加顺序，而只关心键和值之间的关联关系
'''

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0  # 给外星人出现的位置添加坐标 
alien_0['y_position'] = 25
print(alien_0)

# 在空字典中添加键-值对，有时是为了方便，有时必须这样做
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# 修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#例子
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# 向右移动外星人，据外星人当前速度决定其讲移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3

# 新位置等于原位置加增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position:" + str(alien_0['x_position']))

# 通过修改字典中的值，可以改变外星人的行为，如：
alien_0['speed'] = 'fast'

# 删除键值对
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)

# 由类似对象组成的字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',  # 在最后一个键-值对后也加上逗号，为以后在下一行添加键-值对做好准备
    }  # 括号与键对齐

# 给定被调查者名字，即可使用这个字git 典获取他喜欢的语言
print("Sarah's favorite language is " + 
    favorite_language['sarah'].title() +
    ".")

# 遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
# 使用了字典名和方法items()；返回顺序和储存顺序有可能不同
for key, value in user_0.items():  # 可以使用任何名称，如k，v
    print("\nKey: " + key)
    print("Value: " + value)

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }  

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 在不需要值时，用keys遍历字典中所有的键
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }  

for name in favorite_language.keys():  # 遍历字典时默认遍历键，因此不加keys()，输出将不变
    print(name.title())

#指出两位朋友喜欢的语言
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 

friend = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    if name in friend:
        print("  Hi " + name.title() + ", I see your favorite language is " + favorite_language[name].title() + "!")

#还可以用keys()确定某人是否接受了调查
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 

if 'eric' not in favorite_language.keys():
    print("Eric, please take our poll!")

# 按顺序遍历字典中的所有键：在for循环中用sorted()排序
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 

for name in sorted(favorite_language.keys()):  # sorted不影响原字典
    print(name.title() + ", thank you for taking the poll.")

# 在不需要键时，用values遍历字典中所有的值
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 

print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

# 想提取不重复的值，可使用集合(set)，集合类似列表但每个值都是唯一的
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 

print("The following languages have been mentioned:")
for language in set(favorite_language.values()):
    print(language.title())

# 嵌套：字典嵌套列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 例子
aliens = []  # 创建一个用于储存外星人的空列表

for alien_number in range(30):  # 创建30个绿色外星人
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:  # 显示前五个
    print(alien)
print("Total number of aliens: " + str(len(aliens)))  # 显示创建了多少个外星人

# 随着游戏进行，将前三个外星人改为黄色、速度为中等、值10个点
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

for alien in aliens[0:3]:  # 继续添加elif将黄色外星人改成红色
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15

for alien in aliens[:5]:
    print(alien)

# 在字典中储存列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#例子
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) >= 2:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    elif len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is: " + language.title())

#在字典中储存字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())