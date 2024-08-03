def tablem(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(str(i*j)+" ",end=' ')
        print('\n')

if __name__=='__main__':
    n=int(input("请输入乘法表阶数"))
    tablem(n)