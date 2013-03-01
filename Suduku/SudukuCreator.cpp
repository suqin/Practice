#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <memory.h>
short val[9] = {1,2,3,4,5,6,7,8,9};  
short Sudoku[9][9];  
  
int MaxTime = 10;  
void _swap(int row,short from_pos,short to_pos)  
{  
    short temp;  
    temp = Sudoku[row][from_pos];  
    Sudoku[row][from_pos] = Sudoku[row][to_pos];  
    Sudoku[row][to_pos]=temp;  
}  
bool colSucceed(short row,short col)  
{  
    if (row == 0)  
        return true;  
    for(int i=0;i<row;i++)  
    {  
        if(Sudoku[i][col] == Sudoku[row][col])  
        {  
            return false;  
        }  
    }  
    return true;  
}  
bool matSucceed(short row,short col)  
{  
    int i;  
    if(row == 0)  
        return true;  
    short x,y;  
    x = col%3;  
    y = row%3;  
    for(i=row-y;i<row;i++)  
    {  
        for(int j=col-x;j<col-x+3;j++)  
        {  
            if(Sudoku[i][j] == Sudoku[row][col])  
                return false;  
        }  
    }  
    for(int j=col-x;j<col;j++)  
    {  
        if(Sudoku[i][j] == Sudoku[row][col])  
                return false;  
    }  
    return true;  
}  
void initRow(short row)  
{  
    int col = 0;  
    int repeat = 0;  
    memcpy(Sudoku[row],val,sizeof(short)*9);//复制val数组  
    for(int i = 0; i<MaxTime;i++)  
    {  
        _swap(row,rand()%9,rand()%9);//随机交换Maxtime次  
    }  
    if(row == 0)//如果是第一行不做下面的判断  
        return ;  
    for(int col = 0;col<9;col++)  
    {  
        while(!colSucceed(row,col)||!matSucceed(row,col))  
        {  
            _swap(row,col,col+(rand()%(9-col)));  
            repeat++;//重复次数自增  
            if(repeat>MaxTime)//防止死锁  
            {  
                _swap(row,col,rand()%9);  
                col = -1;  
                break;  
            }  
        }  
        repeat=0;//repeat set 0  
    }  
}  
int main()
{  
    int count = 0;  
    memset(Sudoku,0,sizeof(short)*9*9);  
    srand( time(NULL) );  
      
    while(count < 9)  
    {  
        initRow(count);  
        count++;  
    }  
    for(int i=0;i<9;i++)  
    {  
        for(int j=0;j<9;j++)  
            printf("%d    ",Sudoku[i][j]);  
        printf("\n");  
    }  
    return 0;  
}