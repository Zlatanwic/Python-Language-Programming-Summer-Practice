

def diamond(n,m):
    max_len=int(2*m-1)
    max_space_len=int((2*m-1-1)/2)
    for time in range(n):
        for i in range(m):
            print((max_space_len-i)*" "+(2*i+1)*"*"+(max_space_len-i)*" ")
        for i in range(m-2,-1,-1):
            print((max_space_len-i)*" "+(2*i+1)*"*"+(max_space_len-i)*" ")

if __name__=='__main__':
    n=int(input("请输入菱形个数:"))
    m=int(input("请输入菱形最大边长:"))
    diamond(n,m)