import datetime as d
y=int(d.date.today().year)
m=int(d.date.today().month)
dd=int(d.date.today().day)
sweek="一二三四五六天"
wd=int(d.date.today().weekday())

print("今天是"+str(y)+"年"+str(m)+"月"+str(dd)+"日，星期"+sweek[wd])