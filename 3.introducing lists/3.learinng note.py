bicycles=['honda','yamaha','suzuki']
del bicycles[1]
print(bicycles)
# 删除元素yamaha

bicycles.insert(1,'yamaha')
print(bicycles)
# 插入元素yamaha

first_owned=bicycles.pop()
print(first_owned)
# 弹出并打印最后一个元素suzuki

print('The fisrt bike I onwed was a '+first_owned)
print('The fisrt bike I onwed was a '+first_owned.title())
print(bicycles)
# ['honda', 'yamaha']

# 删除特定元素
bicycles.remove('yamaha')
print(bicycles)
# ['honda']

#append每次只能写入1个元素
bicycles.append('yamaha')
bicycles.append('suzuki')
print(bicycles)
#['honda', 'yamaha', 'suzuki']

# 使用sort()对列表进行永久性排序
#按字母顺序排序
nogi = ['hashimoto', 'hori', 'nishino', 'ikuta']
nogi.sort()
print(nogi)
#['hashimoto', 'hori', 'ikuta', 'nishino']

#按字母顺序反序排序
nogi.sort(reverse=True)
print(nogi)
#['nishino', 'ikuta', 'hori', 'hashimoto']

# 使用sorted()对列表进行临时排序
nogi = ['hashimoto', 'hori', 'nishino', 'ikuta']
print("Here is a sorted list:" + str(sorted(nogi)))
# Here is a sorted list: ['hashimoto', 'hori', 'ikuta', 'nishino']

#\n \t等转义字符仅可用于字符串中
print("Here is a sorted list:\n" + str(sorted(nogi)))
print("Here is a sorted list:\t" + str(sorted(nogi)))
print("Here is a sorted list:\n\t" + str(sorted(nogi)))

print(nogi)
#['hashimoto', 'hori', 'nishino', 'ikuta']
sorted(nogi, reverse=True)
#['nishino', 'ikuta', 'hori', 'hashimoto']
print(sorted(nogi, reverse=True))
#['nishino', 'ikuta', 'hori', 'hashimoto']

print(nogi)
#['hashimoto', 'hori', 'nishino', 'ikuta']
nogi
#['hashimoto', 'hori', 'nishino', 'ikuta']

for idol in nogi:
    print(idol)

