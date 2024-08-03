import xlrd
import lx2_1
import lx2_2

def query_by_no(no):

    mixed_list = lx2_2.table_merge(lx2_1.read_book('score.xls', 0)[1], lx2_1.read_book('score.xls', 1)[1])

    """for i in range(0,118):
        print(mixed_list[i][0])
        print(type(mixed_list[i][0]))"""
    #print(mixed_list)
    for i in range(len(mixed_list)-1):
        mixed_list[i][0]=str(mixed_list[i][0])

    for i in range(0,len(mixed_list)-1):
        if mixed_list[i][0] == no:
            #print(no+"=="+mixed_list[i][0])
            row=i
    key=['学号','姓名','英文姓名','性别','学期','英语','高程','物理','高数','摄影']
    value=[mixed_list[row][0],mixed_list[row][1],mixed_list[row][2],mixed_list[row][3],mixed_list[row][4],
           mixed_list[row][5],mixed_list[row][6],mixed_list[row][7],mixed_list[row][8],mixed_list[row][9]]
    return dict(zip(key,value))

if __name__=='__main__':
    print(query_by_no('2353113'))