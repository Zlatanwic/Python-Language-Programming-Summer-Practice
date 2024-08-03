import json

def find_word():
    with open('course.txt') as course:
        data=json.load(course)
    kw=input('请输入要查询的关键字')
    ans=[]
    for i in range(len(data)):
        json_i=json.dumps(data[i],ensure_ascii=False)
        if kw in json_i:
            dict_i=json.loads(json_i)
            ans.append(dict_i)
    if ans:
        print("共找到"+str(len(ans))+"条数据")
        print(ans)
    else:
        print('未找到任何数据')

if __name__=='__main__':
    find_word()