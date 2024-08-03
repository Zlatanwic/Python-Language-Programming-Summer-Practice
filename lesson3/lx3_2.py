import json

def find_score():
    with open('course.txt') as course:
        rdic=json.load(course)

    no=input('请输入学号：')
    project=input('请输入想要查询的课程：')
    line=len(rdic)
    ans_dic={}
    exist_or_not=0

    for i in range(line):
        if rdic[i]['学号'] == no:
            ans_dic=dict(rdic[i])
            rdicbak=dict(rdic[i])
            exist_or_not+=1
    if exist_or_not == 0:
        #print('所查询学号不存在')
        return '所查询学号不存在'
    if project not in ans_dic['score'][0].keys() and project not in ans_dic['score'][1].keys():
        return '没找到对应学号的'+project+'成绩'

    else:
        ans_dic['score']=[{'学期': '2023上'},{'学期': '2023下'}]
        if project in rdicbak['score'][0].keys():
            ans_dic['score'][0][project]=rdicbak['score'][0][project]
        else:
            del ans_dic['score'][0]
        if project in rdicbak['score'][1].keys():
            ans_dic['score'][1][project]=rdicbak['score'][1][project]
        else:
            del ans_dic['score'][1]

        return ans_dic

if __name__=='__main__':
    print(find_score())