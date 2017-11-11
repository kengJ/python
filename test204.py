import os
file = open('test.txt','r').readlines()
for data in file:
    print("insert into D_Gas (code,name,note) values ('"+data.replace('\n','')+"','3F3C','宿舍热水表')")
