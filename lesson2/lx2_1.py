import xlrd
def read_book(book,num):  #这个book用来
    """参数1book用来
       参数2来决定读取该文件薄的哪个表格"""
    work_book=xlrd.open_workbook(book)
    work_sheet=work_book.sheets()[num]
    sh_title=work_sheet.row_values(0)
    num_of_row=work_sheet.nrows
    sh_contend=[]
    #print(sh_title)
    for i in range(1,num_of_row):
        sh_contend.append(work_sheet.row_values(i))
    for i in range(1,num_of_row-1):
        sh_contend[i][0]=str(int(sh_contend[i][0]))
    return sh_title,sh_contend
#print(sh_contend)

if __name__=='__main__':
    print(read_book('score.xls',0)[0])
    print(read_book('score.xls',0)[1])
    print(read_book('score.xls', 1)[0])
    print(read_book('score.xls', 1)[1])