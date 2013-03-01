Suduku = []
Suduku +=[[7,4,0,0,8,0,0,1,6]]
Suduku +=[[9,0,0,0,3,5,0,0,4]]
Suduku +=[[0,0,0,7,0,0,0,0,0]]
Suduku +=[[0,7,0,0,0,9,5,0,0]]
Suduku +=[[6,1,0,0,5,0,0,8,7]]
Suduku +=[[0,0,2,6,0,0,0,4,0]]
Suduku +=[[0,0,0,0,0,4,0,0,0]]
Suduku +=[[3,0,0,5,6,0,0,0,2]]
Suduku +=[[5,6,0,0,1,0,0,3,9]]


Value = [0,1,2,3,4,5,6,7,8,9]

#Num类用来表示在（x，y）坐标上的空格内可能的取值
class Num:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.values=set(Suduku[y])
        for i in range(0,9):
            self.values.add(Suduku[i][x])
        for i in range(0,3):
            for j in range(0,3):
                self.values.add(Suduku[i+y-(y%3)][j+x-(x%3)])
        self.values = set(Value) - self.values
    def len(self):
        return len(self.values)
    def getPos(self):
        return (self.x,self.y)
#Nums是Num的集合,initNums函数将所有能够一次确定的值填入Sudoku中
#剩下Nums集合里的值都是不能确定的
#简单的数独通过initNums就直接可以解出
def initNums(Nums)
	i=0
	while(i<9):
		for j in range(0,9):
			if Suduku[i][j] == 0 :
				temp = Num(j,i)
				if temp.len() == 1:
					Suduku[i][j] = temp.values.pop()
					i=-1
					j=0
					Nums.clear()
					break
				Nums.append(Num(j,i))
		i+=1


if __name__ == '__main__' :
	Nums = []
	initNums( Nums )
	for i in range(0,len(Suduku)):
		print(Suduku[i])