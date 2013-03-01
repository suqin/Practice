/************************************************************
 *01背包问题
 *有 N 件物品和一个容量为 V 的背包。放入第 i 件物品耗费的费用是 cost[i]，
 *得到的价值是 value[i]。求解将哪些物品装入背包可使价值总和最大。
 *method1是原始算法
 *method2是经过优化过空间花费的算法
 *讲义地址 https://github.com/tianyicui/pack
 *我写的代码的地址
 ***********************************************************/



#include <stdio.h>
#define V 10
#define N 3

void method1(const int cost[],const int value[])
{
	int temp=0;
	int f[N+1][V+1];//使用二维数组存储各种情况
	
	for(int i=0;i<V;i++)
		f[0][i]=0;
	for(int i=1;i<=N;i++){
		for(int j=0;j<=V;j++){//考虑i个物品的在容量花费为j时候的情况
			temp=f[i-1][j];
			if(cost[i-1]>j) //如果当前物品放不进去则保持
				f[i][j]=temp;
			else //如果能放进去则与先前存储的情况相加后作比较,取最优解存进f
				f[i][j]=(temp>(f[i-1][j-cost[i-1]]+value[i-1])) ? temp:(f[i-1][j-cost[i-1]]+value[i-1]);
		}
	}
	for(int i=1;i<=N;i++){
		for(int j=0;j<=V;j++)
			printf("%d  ",f[i][j]);
		printf("\n");
	}
}
void method2(const int cost[],const int value[])
{
	int f[V+1];//与method比较压缩了结果数组f
	for (int i = 0; i <= V; i++)
		f[i]=0;
	for(int i=1;i<=N;i++){
		for(int j= V ;j>cost[i-1];j--){
			if(cost[i-1]>j) break;
			f[j]=(f[j]>(f[j-cost[i-1]]+value[i-1])) ? f[j]:(f[j-cost[i-1]]+value[i-1]);
		}
	}
	for(int i=0;i<=V;i++)
		printf("%d  ",f[i]);
}
int main()
{
	int cost[N] = {3,4,5};
	int value[N] = {4,5,6};
	method2(cost,value);
	return 0;
}