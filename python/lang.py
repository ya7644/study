#!/usr/bin/python
#coding=utf-8


str2='abc';
print(len(str2));

str2="I\'s Micky";
print(len(str2));

str2="It\'s a \"pen\"";
print(len(str2));

str2="我爱中国";
print(len(str2));

num = 12;
print(len(str2));

num= 0.9991
print(len(str2));

num = 10/3;
print(len(str2));

num = 9/3;
print(num);

num = 10//3;
print(num);

num = 10%3;
print(num);

num = 10/3;
print('%2s'%num);

#运行失败
num = ord('中');
print(num);

k = 'Abc';
print (len(k));

k = b'Abc';
print(k);

k = "中文".encode('utf-8');
print(k);


arr = [1,2,2];
print(arr)

arr_tuple = (1,2,3)
print(arr_tuple);

arr_tuple=(1)
print(arr_tuple);


arr_tuple=(1,)
print(arr_tuple);

arr_tuple = (1,2,3,[2,4])
#arr_tuple[1] = 4;
arr_tuple[3][0] = 4;
print(arr_tuple);