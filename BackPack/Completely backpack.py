__author__ = 'suqin'
#-*- code:utf-8 -*-
"""
完全背包问题
有 N 种物品和一个容量为 V 的背包。放入第 i 件物品耗费的费用是 cost[i]，
得到的价值是 value[i]。求解将哪些物品装入背包可使价值总和最大。
得到的解存放在f[]中

"""
V = 10
N = 3
coast = [3,4,5]
value = [4,5,6]
f = []
for i in range(0,V+1):
    f.append(0)

for i in range(0,N):
    for v in range(coast[i],V+1):
        if f[v-coast[i]] +value[i] >f[v]:
            f[v]=f[v-coast[i]] +value[i]
print (f[V])
