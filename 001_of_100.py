'''
����1��
��Ŀ����1��2��3��4�����֣�����ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�
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
# Matlab �ļ�������������ĸ��ͷ
%% ��ջ�������
clc
clear
%% ѭ���ж�
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
% &��&&�����������߼�������������ʾ�߼��루and��
% &&�����ж�·�Ĺ��ܣ��������һ�����ʽΪfalse�����ټ���ڶ������ʽ
% &����������λ���������&���������ߵı��ʽ����boolean����ʱ��&��ʾ��λ�����������ͨ��ʹ��0x0f����һ����������&���㣬����ȡ�����������4��bitλ�����磬0x31 & 0x0f�Ľ��Ϊ0x01            
% Matlabλ�� bitand(a1,a2)      [   a=bitand(7,3)   a = 3  ]


# Filename:J_001_of_100.java
# Java �ļ�������������ĸ��ͷ

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



