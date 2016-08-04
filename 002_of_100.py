
# Filename:002.py
'''
i = int(raw_input('Enter the profit:'))

Traceback (most recent call last):
    i = int(raw_input('Enter the profit:'))
NameError: name 'raw_input' is not defined

原因是从版本3.0 开始去掉了raw_input 函数,改用input
'''
i = int(input('Enter the profit:'))

#i = 1200000
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
      #  print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print (r)


# Filename:M_002_of_100.m
%% 清空环境变量
clc
clear

%%
i = input('Please input I :');
sum = 0;
if i < 100000
    sum = sum + i*0.1;
elseif i < 200000 
    sum = sum + 10000 + (i-100000)*0.075;
elseif i < 400000
    sum = sum + 17500 + (i-200000)*0.05;
elseif i < 600000
    sum = sum + 27500 + (i-400000)*0.03; 
elseif i < 1000000
    sum = sum + 33500 + (i-600000)*0.015;
elseif i >= 1000000
    sum = sum + 39500 + (i-1000000)*0.01;
end


# Filename:J_002_of_100.java

package one_of_100;
import java.io.*;

public class J_002_of_100 {
	public static void main(String[] args)throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        String str = null; 
        System.out.println("Please input I value:"); 
        str = br.readLine();
        int i=Integer.parseInt(str);
		int sum = 0 ;
			
			if (i < 100000)
			    sum = (int) (sum + i*0.1);
			else if (i < 200000 )
			    sum = (int) (sum + 10000 + (i-100000)*0.075);
			else if (i < 400000)
			    sum = (int) (sum + 17500 + (i-200000)*0.05);
			else if (i < 600000)
			    sum = (int) (sum + 27500 + (i-400000)*0.03); 
			else if (i < 1000000)
			    sum = (int) (sum + 33500 + (i-600000)*0.015);
			else if (i >= 1000000)
			    sum = (int) (sum + 39500 + (i-1000000)*0.01);
			
		System.out.println(sum);
	}
}



