
'''
����4��
��Ŀ������ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿
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
���õ�ǰ�����ʱ�� ��ȥ �����ʱ�� ���������
'''

# Filename:M_004_of_100.m
%% ��ջ�������
clc
clear
%% ����ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿
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
% fix()      ��βȡ��
% floor()    ��˹ȡ��

%% % Matlab ����ʱ�� ���� û��͸ Ҫ����˵����
% Matlab�ṩ�������ڸ�ʽ�������ַ����硯1996-10-02����������������729300��0000��1��1��Ϊ1���Լ����������� 1996 10 2 0 0 0������Ϊ������ʱ���롣
% ���õ����ڲ�������
% datestr(d,f) ����������ת��Ϊ�ַ���
%        datenum(str,f) ���ַ���ת��Ϊ��������
%        datevec(str) �����ַ���ת������
%        weekday(d) ����������
%        eomday(yr,mth) ����ָ���·����һ��
%        calendar(str) ������������
%         clock ��ǰ���ں�ʱ�����������
%        date ��ǰ�����ַ���
%        now ��ǰ���ں�ʱ���������





