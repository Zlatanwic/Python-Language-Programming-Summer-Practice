import json
import lx2_1
import lx2_2

def excel_to_json():
    mix_list=lx2_2.table_merge(lx2_1.read_book('score.xls',0)[1],lx2_1.read_book('score.xls',1)[1])
    key = ['学号', '姓名', '英文姓名', '性别', '学期', '英语', '高程', '物理', '高数', '摄影']
    ans_list=[]
    line=len(mix_list)
    for i in range(line):
        person={}
        if mix_list[i][4] == '2023上':
            for j in range(3):
                if mix_list[i][j]:
                    person[key[j]]=mix_list[i][j]
        score=[]
        dic1={}
        dic2={}
        if mix_list[i][4] == '2023上':
            dic1['学期']='2023上'
            for k in range(5,10):
                if mix_list[i][k]:
                    dic1[key[k]]=mix_list[i][k]
            #print(dic1)
            score.append(dic1)
        elif mix_list[i][4]=='2023下':
            dic2['学期'] = '2023下'
            for k in range(5, 10):
                if mix_list[i][k]:
                    dic2[key[k]] = mix_list[i][k]
            #print(dic2)
            ans_list[i-59]['score'].append(dic2)
            score.append(dic2)

        person['score']=score
        if mix_list[i][4] == '2023上':
            ans_list.append(person)

    #for i in range(line):



    #for i in range(59,line-1):
        #del ans_list[i]
    for i in range(len(ans_list)):
        print(ans_list[i])
    #print(ans_list)
    json_list=json.dumps(ans_list,ensure_ascii=False)
    with open('course.txt','w') as course:
        course.write(json_list)
    #return json_list

#print(excel_to_json())
if __name__=='__main__':
    excel_to_json()