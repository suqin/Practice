#include <deque>
#include <time.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
int N = 10;//N个数
int M = 1000;//和是M
deque<int> resault;
int main()
{
  int temp;
	int firstNum;
	srand( time(NULL) );
	resault.push_back(M);
	for(;;)
	{
		if(resault.size() == N)//当结果队列不满时
			break;
		firstNum = resault[0];//取出队列第一个数
		temp = rand()%firstNum;//分解为一个随机数和一个差值，
		resault.pop_front();
		resault.push_back(temp);
		resault.push_back(firstNum-temp);//入队循环
	}
  for(int i=0;i<N;i++)
    cout<<resault[i]<< "+";
  cout<< " = "<<M;
	return 0;
}
