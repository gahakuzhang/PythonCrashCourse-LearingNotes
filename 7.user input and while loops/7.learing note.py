#7.1 input工作原理
#input()让程序暂停，用户输入按回车后继续运行。输入存储在变量中。
#input()的参数是向用户的提示
message=input('Tell me sth, and I will repeat it back to u: ')
print(message)
#7.1.1
#提示超过一行时，可以将提示存在变量中
#+=在字符串末尾增加字符串，作用等于prompt=prompt+"\nWhat's your first name? "
prompt="If you tell us who you are, we can personalize the messages you see."
prompt+="\nWhat's your first name? "
name=input(prompt)
print("\nHello！"+name+"!")

#7.1.2 使用int()获得数值输入
height=input("How tall are you, in inches? ")
height=int(height)
if height>=36:
    print("You are tall enough!")
else:
    print("\nYou will be able to ride when you are a little older.")

#7.1.3 求模运算符%，相除后返回余数
number=input("Enter a number, and I'll tell you if it's even or odd: ")
number=int(number)
if number%2==0:
    print("The number "+number+" is even")
else:
    print("The number "+number+" is odd")

#7.2 while loops
#7.2.1 counting
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1
#current_number+=1是current_number=current_number+1的简写

#7.2.2 letting the user choose when to quit
#充分理解程序运行的顺序
prompt="\nTell me something, and I will repeat it back to u: "
prompt+="\nEnter 'quit' to end of this program. "
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
#首次执行while时，因为用户还没有输入，无法比较。因此先定义一个空字符串进行比较
#输入quit后，停止执行while循环
#错误示例，以下程序会进入死循环
#同时input的位置也是错的，创建多行字符串的时候不应写入input()
#prompt=input("\nTell me something, and I will repeat it back to u: ")
#prompt+="\nEnter 'quit' to end of this program. "
#while prompt!='quit':
    #print(prompt)

#7.2.3 using a flag 标志
# 注意True和False首字母要大写
#这个例子中flag为active
prompt="\nTell me something, and I will repeat it back to u: "
prompt+="\nEnter 'quit' to end of this program. "
active=True
while active:
    message = input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

#7.2.4 using break to exit a loop
#while True开头的循环会的不断运行，直到遇到break
#break不执行余下的代码并退出整个循环
prompt="\nPlease enter the name of cities you have visited: "
prompt+="\n(Enter 'quit' when you are finished.) "
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")

#7.2.5 using continue in a loop
#满足if条件时执行continue语句，忽略剩下的代码返回代码的开头
#不满足时继续执行余下的代码
#break不执行余下的代码并退出整个循环
current_number=0
while current_number<10:
    current_number+=1
    if current_number % 2==0:
        continue
    print(current_number)

#7.2.6 avoiding infinite loops
#Ctrl+C关闭终端窗口(例如Pycharm里的Python Console)
#务必对每个while循环进行测试

#7.3 using a while loop with lists and dictionaries
#7.3.1 moving items from a list to another
#for循环中不应修改列表
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#while unconfirmed_users: 不断循环，直到unconfirmed_users变成空的

#7.3.2 removing all instances of specific values from a list
#pets
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#7.3.3 filling a dictionary with user input
#mountains_poll
# responses[name]=response 添加键值对
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input("which mountain would you like to climb someday? ")
    responses[name]=response
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        polling_active=False
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would like to climb "+response+".")




