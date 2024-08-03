import xlrd
import lx2_1

def table_merge(list1,list2):
    for i in range(0,len(list2)):
        del list1[i][0]
        list1[i].insert(0, list2[i][3])
        list1[i].insert(0, list2[i][2])
        list1[i].insert(0, list2[i][1])
        list1[i].insert(0, list2[i][0])
    for i in range(len(list2),len(list1)):
        del list1[i][0]
        list1[i].insert(0, list2[i-len(list2)][3])
        list1[i].insert(0, list2[i-len(list2)][2])
        list1[i].insert(0, list2[i-len(list2)][1])
        list1[i].insert(0, list2[i-len(list2)][0])
    return list1

if __name__=='__main__':
    list_end=table_merge(lx2_1.read_book('score.xls',0)[1],lx2_1.read_book('score.xls',1)[1])
    for i in range(len(list_end)):
        print(list_end[i])