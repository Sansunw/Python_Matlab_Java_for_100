
'''
程序4】
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
# Filename:004_of_100.py

import datetime
import time
dtstr = str(input('Enter the datetime:(20151215):'))
#dtstr = '20160901'
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
print (dt)
#                     2016-09-01 00:00:00
another_dtstr =dtstr[:4] +'0101'
print (dtstr[:4])
#                     2016
print (another_dtstr)
#                     20160101
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print (another_dt)
#                     2016-01-01 00:00:00
print (dt-another_dt)
#                     244 days, 0:00:00
print ((dt-another_dt).days)
#                     244
print (int((dt-another_dt).days) + 1)

'''
利用当前输入的时间 减去 年初的时间 （日期做差）
'''

# Filename:M_004_of_100.m
%% 清空环境变量
clc
clear
%% 输入某年某月某日，判断这一天是这一年的第几天？
i = input('Please input the datatime: (20160901): ','s');
% i = '20160901';
b= [0 31 59 90 120 151 181 212 243 273 304 334 ];
sum = 0 ;
a1 = str2num(i(1:4));
a2 = str2num(i(5:8));
if( mod(a1,4)==0)
    sum = sum+1;
end
sum = sum + b(floor(a2/100)) + mod(a2,100);
% fix()      截尾取整
% floor()    高斯取整

%% % Matlab 带的时间 方法 没看透 要用再说～～
% Matlab提供三种日期格式：日期字符串如’1996-10-02’，日期序列数如729300（0000年1月1日为1）以及日期向量如 1996 10 2 0 0 0，依次为年月日时分秒。
% 常用的日期操作函数
% datestr(d,f) 将日期数字转换为字符串
%        datenum(str,f) 将字符串转换为日期数字
%        datevec(str) 日期字符串转换向量
%        weekday(d) 计算星期数
%        eomday(yr,mth) 计算指定月份最后一天
%        calendar(str) 返回日历矩阵
%         clock 当前日期和时间的日期向量
%        date 当前日期字符串
%        now 当前日期和时间的序列数

# Filename:J_004_of_100.java
package one_of_100;
import java.io.*;
public class J_004_of_100 {
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        String str = null; 
        System.out.println("Please input the datatime: (20160901): "); 
        str = br.readLine();
       
		int sum = 0 ;
//		i = '20160901';
		int[] b= {0 ,31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334 };
		
		int a1 = Integer.parseInt((str.substring(1, 5)));
		int a2 = Integer.parseInt((str.substring(5)));
		if( a1%4==0){
		    sum = sum+1;
		}
		sum = sum + b[a2/100 - 1] +a2%100;
		System.out.println(sum);
	}
}

// IO口要有  throws IOException
Java 数组 从 0 下标开始
Java 可以直接用 / 求商  % 求余 
