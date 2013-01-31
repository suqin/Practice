__author__ = 'suqin'
import itertools
import random

#测试数据时随机生成的4个1~13间的整数
nums = [random.randint(1,13),random.randint(1,13),random.randint(1,13),random.randint(1,13)]
print("测试数据为:",nums)
#定义操作符集合，方便输出
opts = {0:"+",1:"-",2:"*",3:"/"}
#利用lambda表达式方便的定义函数数组
f = []
f.append(lambda x,y: x+y)
f.append(lambda x,y: x-y)
f.append(lambda x,y: x*y)
f.append(lambda x,y: x/y)
#对测试数据全排列
l=list(itertools.permutations(nums))

for m in range(len(l)):#遍历每一种数据的排列方式
    for i in range(0,f.__len__()):#列举第一个运算符
        for j in range(0,f.__len__()):
            for k in range(0,f.__len__()):
                if abs(f[k](f[j](f[i](l[m][0],l[m][1]),l[m][2]),l[m][3]) - 24) < 1E-6 :
                    print ("(((%d %s %d) %s %d) %s %d)" %(l[m][0],opts[i],l[m][1],opts[j],l[m][2],opts[k],l[m][3]))