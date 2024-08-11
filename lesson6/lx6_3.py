import xlrd
import pandas as pd

class St_lesson():
    def __init__(self,st_id):
        work_book = xlrd.open_workbook('xuanke.xls')
        work_sheet=work_book.sheets()[0]
        #st_no=work_sheet.col_values[0]
        num_of_row = work_sheet.nrows
        sh_contend = []
        # print(sh_title)
        self.st_no=st_id
        for i in range(1, num_of_row):
            sh_contend.append(work_sheet.row_values(i))
        for i in range(1, num_of_row - 1):
            sh_contend[i][0] = str(int(sh_contend[i][0]))
        st_xuan=[]

        work_sheet2=work_book.sheets()[1]
        key=[]
        key=work_sheet2.row_values(0)

        for i in range(1, num_of_row-1):
            if sh_contend[i][0] == st_id:
                self.st_name=sh_contend[i][1]
                self.st_py=sh_contend[i][2]
                self.st_sex=sh_contend[i][3]
                st_xuan=work_sheet2.row_values(i+1)
                #print(st_xuan)
                st_dict=dict(zip(key,st_xuan))

        #print(key)
        #print(sh_contend)
        #print(st_dict)
        self.st_course_list=[]
        for key,value in st_dict.items():
            if value=='√':
                self.st_course_list.append(key)
        work_sheet3=work_book.sheets()[2]
        self.st_schedule_list=[]
        for i in range(5):
            self.st_schedule_list.append(work_sheet3.row_values(i))
        #print(self.st_schedule_list)
        #print(self.st_course_list)
        for i in range(1,5):
            for j in range(1,6):
                self.st_schedule_list[i][j]=self.st_schedule_list[i][j].split(',')
        for i in range(1,5):
            for j in range(1,6):
                #print(self.st_schedule_list[i][j])
                rlist=list(self.st_schedule_list[i][j])
                for each in rlist:
                    if each not in self.st_course_list:
                        #print(each)
                        self.st_schedule_list[i][j].remove(each)


        #print(self.st_schedule_list)
        for i in range(1,5):
            for j in range(1,6):
                self.st_schedule_list[i][j]=','.join(self.st_schedule_list[i][j])

        #print(self.st_schedule_list)



    def display_schedule(self):
        print("学号："+self.st_no+' 姓名：'+self.st_name+'的课表')
        #print(self.st_schedule_list)
        for row in self.st_schedule_list:
            for str in row:
                print(f'{str:<20}',end='')
            print('\n')

    def check_conflict(self):
        for i in range(1,5):
            for j in range(1,6):
                self.st_schedule_list[i][j]=self.st_schedule_list[i][j].split(',')
        conflict_list={}
        for i in range(1,5):
            for j in range(1,6):
                if len(self.st_schedule_list[i][j])>1:
                    conflict_list[self.st_schedule_list[i][0]+self.st_schedule_list[0][j]]=self.st_schedule_list[i][j]
        print(self.st_name+'的选课冲突有:',end='')
        print(conflict_list)


lk=St_lesson('2353113')
#lk.print_inf()
lk.display_schedule()
lk.check_conflict()