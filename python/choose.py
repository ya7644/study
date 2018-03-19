# -*- coding: utf-8 -*-

# age = input('age:')
# if age > 20:
# 	print('>20')
# elif age<20:
# 	print('<20')
# else:
# 	print('noting')


# 计算BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# height = int(input('height:'))
# weight = int(input('weight:'))
# height = height/100

# bmi = float(weight) / (height*height)

# if bmi < 18.5:
# 	print('过轻')
# elif bmi > 18.5 and bmi <25:
# 	print('正常')
# elif bmi > 25 and bmi <28:
# 	print('过重')
# elif bmi > 28 and bmi <32:
# 	print('肥胖')
# else:
# 	print('过于肥胖')
	
# end_num = int(input('请输入您想要统计的数的范围:'))
# lists = ('red','black','white')
# sum_item = 0
# for i in range(1,end_num+1):
# 	sum_item += i
# print(sum_item)
# 
# start_num = 1
# end_num = 100
# sum_item = 0

# while start_num<(end_num+1):
# 	sum_item +=start_num
# 	start_num +=2;
# print(sum_item)
# 
# L = ['Bart', 'Lisa', 'Adam']
# for li in L:
# 	print('hello,'+li)
	
# sum_item = 0
# for i in range(1,100):
# 	if i < 10:
# 		continue
# 	sum_item += i
# print(sum_item)

#dict
# scores = {'Micky':20,'Mack':60,'kitty':100}
# print(scores['Micky'])
# print('Micky' not in scores)
# print(scores.get('Micky2',22))
# scores.pop('Micky')
# print(scores)

#set 
scores = set([1,2,3])
scores.add(4)
scores = set([1,2,3,4,4,4])
scores.remove(4)
print(scores)
