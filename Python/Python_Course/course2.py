# 用[]表示列表，用逗号分隔其中的元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素，指出列表名称+元素的索引
print(bicycles[0])

# 添加title()让字母大写
print(bicycles[0].title())

# 索引指定为-1访问倒数第一和倒数第二个列表元素
print(bicycles[-1])
print(bicycles[-2])

# 可使用列表中的各个值，并创建一条消息
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " +bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表末尾添加元素
motorcycles.append('giant')
print(motorcycles)

# 创建空列表，使用append语句添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中插入元素，需要指定新元素的索引和值
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 用del在列表中删除元素，需要指定索引
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# 可以利用pop删除元素，默认为列表末尾，可以输入索引弹出特定值
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()  # 弹出一个值并储存到变量popped_motorcycles中
print(motorcycles)  # 弹出后的值被删除,不再在列表中了
print(popped_motorcycles)

# 利用pop指出最后购买的哪款摩托车
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycles I owned was a " + last_owned.title() + ".")

# 也可以用pop删除列表中任何位置的元素，只需要指定索引
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycles I owned was a " + first_owned.title() + ".")

# 如果要删除一个元素且不再使用它，就用del，如果删除后还要继续使用，就用pop

# 如果删除时不知道位置，只知道元素的值，用remove，注意remove只删除第一个指定的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# 使用remove删除元素时，也可接着使用它的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive to me.")
# 'ducati'虽然已经删除，但还储存在变量too_expensive中

# 用sort对列表进行永久性排序(按字母)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)  # 字母倒序
print(cars)
# 用 sorted对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)  # 核实顺序没有被永久改变
print(sorted(cars, reverse=True))  # 也可按字母倒序
print(cars)

# 反转列表元素顺序，可使用reverse，注意：不是反转字母顺序
# 方法reverse() 永久性地修改列表元素的排列顺序， 但可随时恢复到原来的排列顺序， 为此只需对列表再次调用reverse() 即可
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# 确定列表长度使用len,当索引错误时可用len查看列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
