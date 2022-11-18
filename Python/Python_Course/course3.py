# 用for循环遍历链表
# 从列表中取出每一个名字储存在变量magician中并打印出来
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 对每个魔术师都打印一条个性化消息
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    # 每次迭代后都插入一个空行，整洁地显示每个魔术师的消息编组
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    # 如果第二条print语句没有缩进，因此它只在循环结束后执行一次。由于变量magician的终值为'carolina'，
    # 因此只有她收到了消息“looking forward to the next trick”

# 在for循环后面，没有缩进的代码都只执行一次，而不会重复执行
print("Thank you, everyone. That was a great magic show!")

# 使用函数range生成一系列数字
for value in range(1, 5):  # range左闭右开
    print(value)
# 使用range创建数字列表：将range作为list的参数
numbers = list(range(1, 6))
print(numbers)
# 第三个参数指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 将前10个数的平方加入到一个列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 为使代码简介，可不使用临时变量square
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 对数字列表进行简单统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# 列表解析将for循环和创建新元素的代码合并成一行,并自动附加新元素
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 通过切片可以得到列表的子集，或者[:]得到列表的拷贝。name[start:end],start默认为0,end默认为结束
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
# 如果没有指定第一个索引则默认从头开始
print(players[:4])
# 同理
print(players[2:])
# 输出最后三名队员
print(players[-3:])

# 遍历列表内部分元素，可在for循环中使用切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 为了证明确实有两个列表，分别添加一种不同的食品
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# 如果只是简单地将my_foods赋值给friend_foods，就不能得到两个列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# 定义元祖，使用圆括号，元祖不可修改
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 尝试修改
dimensions = (200, 50)
dimensions[0] = 250

# 可以像遍历列表一样，使用for遍历元祖的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 虽然不能修改元祖的值，但是可以给储存元祖的变量赋值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)