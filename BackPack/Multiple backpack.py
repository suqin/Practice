__author__ = 'suqin'
#-*- code:utf-8 -*-
"""
多重背包问题
有 N 种物品和一个容量为 V 的背包。
第 i 种物品最多有 M[i]件可用
放入第 i 种物品耗费的费用是 cost[i]，
得到的价值是 value[i]。
求解将哪些物品装入背包可使价值总和最大。
得到的解存放在f[]中
"""
N = 6
V = 30
coast = [3,4,5,6,7,8]
value = [4,5,6,7,8,9]
M =     [2,2,3,2,2,1]
f = []
for i in range(0,V+1):
    f.append(0)
total = []
i = 0
while i <M.__len__():
    for j in range(0,M[i]):
        total.append(i)
    i+=1
for i in total:
    v = V
    while v > coast[i]:
        if f[v] < f[v-coast[i]]+value[i]:
            f[v] = f[v-coast[i]]+value[i]
        v-=1
print(f[V])
