# coding: UTF-8
"""
题目：给出一个数组a和一个数字sum，要求用a里的数字用加法凑成sum

使用随机化算法求解
1 每次将数组a[0]与后面随机位置上的一个数字交换
2 i=0
3 sum-=a[i]
    3.1 sum == 0 得到解，输出并退出
    3.2 sum < 0 返回1
    3.3 sum > 0 i+=1 返回3
"""
from random import randint
MAX = 1e9 #最大尝试次数
count = 0 #尝试计数
a=[]      
sum=int(raw_input("要求的和:"))
N=int( raw_input("加数的个数"))
for i in range(0, N):
    a.append(int( raw_input("第%d个数字" %i)))
le=a.__len__()
while True:
    if count >= MAX:
        print ("no resault")
        exit()
    temp=sum
    s=randint(1, le-1)
    a[0]^=a[s]
    a[s]^=a[0]
    a[0]^=a[s]
    i=0
    while temp > 0:
        if i >= le:
            print ("2no resault")
            exit()
        temp-=a[i]
        i += 1
    if temp == 0:
        print ("运算次数:%d" %count)
        print ("解集:")
        for j in range(0, i):
            print (a[j])
        exit()
    count+=1
