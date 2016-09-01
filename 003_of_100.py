# -*- coding:utf-8 -*-
'''
# 第三题：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少
'''

#强制类型转换
import math
num = 1
while True:
    if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 168)-int(math.sqrt(num + 168)) == 0:
        print(num)
        break
    num += 1
#取整
num = 1
while True:
    if math.sqrt(num + 100)-math.floor(math.sqrt(num + 100)) == 0 and math.sqrt(num + 168)-math.floor(math.sqrt(num + 168)) == 0:
        print(num)
        break
    num += 1

'''
Python中的模块
https://docs.python.org/3.5/py-modindex.html
math：
math.sqrt()
math.floor()
'''

# Filename:M_002_of_100.m
%% 清空环境变量
clc
clear
%%
num = 1 ;
while(1)
    if sqrt(num + 100)-floor(sqrt(num + 100)) == 0 && sqrt(num + 168)-floor(sqrt(num + 168)) == 0       
        break
    end
    num = num + 1 ;
end








