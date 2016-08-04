'''
程序1】
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

# Filename:001_of_100.py
cnt = 0#count the sum of result
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print (i*100+j*10+k)
                cnt+=1
print (cnt)

# Filename:M_001_of_100.m
# Matlab 文件命名必须以字母开头
%% 清空环境变量
clc
clear
%% 循环判断
sum = 0;
for i = 1:4
    for j = 1:4
        for k = 1:4
            if (i ~= j && j ~= k && i ~= k)
                sum = sum + 1;
            end
        end
    end
end
% &和&&都可以用作逻辑与的运算符，表示逻辑与（and）
% &&还具有短路的功能，即如果第一个表达式为false，则不再计算第二个表达式
% &还可以用作位运算符，当&操作符两边的表达式不是boolean类型时，&表示按位与操作，我们通常使用0x0f来与一个整数进行&运算，来获取该整数的最低4个bit位，例如，0x31 & 0x0f的结果为0x01            
% Matlab位与 bitand(a1,a2)      [   a=bitand(7,3)   a = 3  ]


# Filename:J_001_of_100.java
# Java 文件命名必须以字母开头

package one_of_100;
public class J_001_of_100 {
	public static void main(String[] args){
		int sum = 0 ;
		for (int i = 1;i<5;i++){
		    for ( int j = 1;j<5;j++){
		    	for (int k = 1;k<5;k++){
		            if (i != j && j != k && i != k)
		                sum = sum + 1;
		    	}
		    }
		}
		System.out.println(sum);
	}
}



