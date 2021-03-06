#4.1.3 for循环结束后执行操作
idols=['nanamin','miona','nachan','maiyan']
for idol in idols:
    print(idol.title()+',ganbare!')
print('Arigatou,minna!')

#4.3.1 创建数值列表，使用函数range()
numbers=list(range(1,5))
print(numbers)
# [1,2,3,4]
# 执行到第二个数字停止

even_numbers=list(range(2,12,2))
print(even_numbers)
#结果[2,4,6,8,10]

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)print(squares)

#4.3.4 List Comprehensions 列表解析
squares=[value**2 for value in range(1,11)]
print(squares)
# **表示乘方

#4.4.1 Slicing a list 切片
idols=['nanamin','miona','nachan','maiyan','rentan','yuki']
print(idols[1:4]) #从1(第2个元素)打印到3(第4个元素)，即['miona', 'nachan', 'maiyan']。4意味着终止于4。
print(idols[:4]) #从头打印到4(第5个元素)之前(即3，第4个元素)，['nanamin', 'miona', 'nachan', 'maiyan']
print(idols[2:]) #从第3个打印到最后，['nachan', 'maiyan', 'rentan', 'yuki']
print(idols[-2:]) #从倒数第2个打印到最后，['rentan', 'yuki']
print(idols[0:3])

# 《利用python进行数据分析第2版》第3章
# In [73]: seq = [7, 2, 3, 7, 5, 6, 0, 1]
# In [74]: seq[1:5]
# Out[74]: [2, 3, 7, 5]
# 切片也可以被序列赋值：
# In [75]: seq[3:4] = [6, 3]
# In [76]: seq
# Out[76]: [7, 2, 3, 6, 3, 5, 6, 0, 1]
# 切片的起始元素是包括的，不包含结束元素。因此，结果中包含的元素个数是stop - start。
# 负数表明从后向前切片：
# In [79]: seq[-4:]
# Out[79]: [5, 6, 0, 1]
# In [80]: seq[-6:-2]
# Out[80]: [6, 3, 5, 6]


#4.4.2 Looping through a slice 遍历切片
idols=['nanamin','miona','nachan','maiyan','rentan','yuki']
print('Here are my favorite three members in this group:')
for idol in idols[:3]:
    print(idol.title())
#4.4.3 copying a list 复制列表-使用切片
my_idols=['nanamin','rentan','yuki']
yc_idols=my_idols[:]
my_idols.append('miona')
yc_idols.append('kazumin')
print('My favorite members are:')
print(my_idols)
print('\nyc\'s favorite members are:')
print(yc_idols)
#4.4.3 copying a list 复制列表-不使用切片
my_idols=['nanamin','rentan','yuki']
#此路不通
yc_idols=my_idols
my_idols.append('miona')
yc_idols.append('kazumin')
print('My favorite members are:')
print(my_idols)
print('\nyc\'s favorite members are:')
print(yc_idols)

#4.4 “操作列表”学习了如何切片、遍历切片以及在是否使用切片的情况下复制列表

#4.5 Tuples元组
#元组使用()而非[]，其中的元素不可修改
#4.5.1 defining a tuple 定义元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=250将报错，因为tuples中的元素不能修改

#4.5.3 writing over a tuple 修改元组变量
dimensions=(200,50)
print('original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
#不能修改元组的元素，但是可以给元组变量赋新值
