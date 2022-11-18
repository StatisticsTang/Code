names = ['tcc', 'czx', 'scx', 'lyq']
for i in range(0, 4):
    message = "Hello " + names[i] + ", how have you been recently？"
    print(message)

brand = ['giant', 'benz', 'honda']
traffic = ['bicycle', 'car', 'motorcycle']
for i in range(0, 3):
    message = "I would like to own a " + brand[i].title() + " " +traffic[i] + "."
    print(message)

invitation = ['czx', 'scx', 'lyq']
len(invitation)
for i in range(0, 3):
    message = invitation[i] + ", would you like to come to the party?"
    print(message)
print(invitation[0] + " cannot come")
invitation[0] = 'lbb'
for i in range(0, 3):
    message = invitation[i] + ", would you like to come to the party?"
    print(message)
print("There is a larger table.")
invitation.insert(0, 'zhangsan')
invitation.insert(2, 'lisi')
invitation.append('wangwu')
print(invitation)
print("Table won't arrive on time. Only two are invited")
for i in range(0, 4):
    new_invitation = invitation.pop()
    print(new_invitation)
    print("sorry, " + new_invitation)
print(invitation)
for i in range(0, 2):
    print(invitation[i] + ", welcome!")
del invitation[0]
print(invitation)
del invitation[0]

place = ['new york', 'london', 'tokyo', 'beijing', 'shanghai']
print(place)
print(sorted(place))
print(place)
print(sorted(place, reverse=True))
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)

the_pizza = ['roast', 'fish', 'beef']
for pizza in the_pizza:
    print("I like " + pizza + " pizza!")
print("I really love pizza")

numbers = [number for number in range(1, 21)]
print(numbers)

print(list(range(1, 21)))

million = []
for number in range(1, 1000001):
    million.append(number)
for i in range(0, 1000000): #注意这里的索引从0开始
    print(million[i])

million = [number for number in range(1,1000001)]
min(million)
max(million)

number = []
for num in range(1, 21, 2):
    number.append(num)
for i in range(0, 10): #注意这里的索引从0开始
    print(number[i])


number = list(range(3, 31, 3))
for num in range(0, 10):
    print(number[num])

number = []
for num in range(1, 11):
    number.append(num ** 3)
for i in range(0, 10):
    print(number[i])

number = [num ** 3 for num in range(1, 11)]
print(number)

print(list(num ** 3 for num in range(1, 11)))

the_pizza = ['roast', 'fish', 'beef']
friend_pizza = the_pizza[:]
the_pizza.append('fruit')
friend_pizza.append('pork')
print("My favorite pizzas are:")
for pizza in the_pizza:
    print(pizza)
print("My friend's pizzas are:")
for pizza in friend_pizza:
    print(pizza)

foods = ('egg', 'cake', 'milk', 'coffee', 'coke')
for food in foods:
    print(food)
#foods[0] = 'bread'报错
foods = ('egg', 'cake', 'milk', 'bread', 'beef')
for food in foods[3:5]:
    print(food)
for i in range(3, 5):
    print(foods[i])

car = 'subaru'
print("Is car == 'subaru? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

alien_color = 'green'

if alien_color == 'green':
    print("Get 5 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("Get 5 points.")

alien_color = 'green'

if alien_color == 'green':
    print("Get 5 points.")
else:
    print("Get 10 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("Get 5 points.")
else:
    print("Get 10 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("Get 5 points.")
elif alien_color == 'yellow':
    print("Get 10 points.")
else:
    print("Get 15 points.")

age = 15

if age < 2:
    state = 'baby'
elif age >= 2 and age < 4:
    state = 'kid'
elif age >= 4 and age < 13:
    state = 'child'
elif age >= 13 and age <20:
    state = 'teenager'
elif age >= 20 and age < 65:
    state = 'adult'
else:
    state = 'the old'

print("State is " + state + ".")

favorite_fruits = ['apples', 'bananas', 'cherries']

if 'bananas' in favorite_fruits:
    print("You really like " + favorite_fruits[1] + ".")
if 'peaches' in favorite_fruits:
    print("You really like peaches.")
if 'cherries' in favorite_fruits:
    print("You really like " + favorite_fruits[2] + ".")

list = ['admin', 'tcc', 'scx', 'czx', 'lyq']
for name in list:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name + ", thank you for logging in agian.")

current_name = ['admin', 'tcc', 'czx', 'scx', 'lyq']
new_users = ['admin', 'czx', 'zhangsan', 'lisi', 'wangwu']

for new_user in new_users:
    if new_user.lower() in current_name:
        print(new_user.title())
    else:
        print("\"" + new_user.title() + "\"" + " never be used.")
    
numbers = list(range(1, 9))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")

info = {'first_name': 'san', 'last_name': 'zhang', 'age': 20, 'city': 'nanjing'}
print(info)

rivers = {
    'nile': 'egypt',
    'yellow river': 'china',
    'changjiang': 'china',
    }
for key, value in rivers.items():
    print("The " + key + " runs through " + value + ".")

for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
    