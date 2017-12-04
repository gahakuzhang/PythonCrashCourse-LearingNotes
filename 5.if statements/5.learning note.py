# 5.2 条件测试
# 5.2.2检查是否相等时不考虑大小写
# 大小写无关紧要，只想检查变量的值
# 函数lower不会修改存储在变量audi中的值
car='Audi'
car.lower()=='audi'
car

# 5.2.3检查是否不相等，使用!=
requested_topping='mushrooms'
if requested_topping!='anchovies':
    print('Hold the anchovies!')

# 5.2.4比较数字
age=18
age==19
age!=19:
age<19
age<=19

# 5.2.5 用and和or检查多个条件

# 5.2.6检查特定值是否在列表中 in
requested_topping=['mushrooms','onions','pineapple']
'mushrooms' in requested_topping

# 5.2.7检查特定值是否在列表中 not in
banned_users=['nanamin','miona','nachan']
user='maiyan'
if user not in banned_users:
    print(user.title()+', you can reponse if you wish')

# 5.2.8布尔表达式


# 5.3 if语句
# 5.3.3 if-elif-else结构
age=12
if age<4:
    print('Your admission cost is $0.')
elif age<18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is 10.')
# 简洁的写法
age=12
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print('Your admission cost is $'+str(price)+'.')

# 5.3.4使用多个elif代码块
# 5.3.5使用elif代码块代替else代码块

# 5.3.6测试多个条件
requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print('Adding mushrooms.')
if 'pepperoni' in requested_topping:
    print('Adding pepperoni.')
if 'extra cheese' in requested_topping:
    print('Adding extra cheese.')
#运行多个代码块时不能使用if-elif-else结构，因为if一旦通过将跳过if-elif-else结构余下的测试
#运行多个代码块时需要使用一系列独立的if语句


# 5.4 使用if语句处理列表
# 5.4.1 检查特殊元素
requested_toppings=['mushrooms','greenpeppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='greenpeppers':
        print('Sorry, we are out of '+str(requested_topping)+'now.')
    else:
        print('Addinig'+requested_topping.tilte()+'.')
print('\nFinished making your pizza!')

# 5.4.2 确定列表是否为空
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Addinig '+requested_topping+'.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

# 5.4.3 使用多个列表
avaible_toppings=['mushrooms','olives','green peppers',
                  'pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaible_toppings:
        print('Adding '+requested_topping+'.')
    else:
        print('Sorry, we don\'t have '+requested_topping+'.')
print('\nFinished making your pizza!')
