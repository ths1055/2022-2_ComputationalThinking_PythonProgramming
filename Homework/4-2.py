student=[
    ('Kim, S.C.', 12001234, 'CE', 4.10), 
    ('Choi, Y.B.', 119003234, 'EE', 3.78), 
    ('Hong, C.H.', 21001547, 'ICE', 4.13), 
    ('Yoon, J.H.', 17002571, 'ME',3.55), 
    ('Lee, S.H.', 20003257, 'ICE', 4.45), 
    ('Kim, H.Y.', 19001234, 'CE', 4.17), 
    ('Lee, J.K',18003234, 'EE', 3.78), 
    ('Park, S.Y.', 21001643, 'ICE', 4.13), 
    ('Jang, S.H.', 19002567, 'ME', 3.35), 
    ('Yeo, C.S', 20005243, 'CE', 4.45)
]
for x in range(len(student)):
    print('student[%2d]  : name(%s), st_id(%d), major(%-3s, GPA(%5.2f))'%(x,student[x][0],student[x][1],student[x][2],student[x][3]))
stu_min=0
stu_init=0
for i in range(len(student)):#별도설정이 없는경우 이름순으로 오름차순 정렬
    for j in range(1+i,len(student)):
        if student[stu_min][0] > student[j][0]:
            stu_min=j
    student[stu_min],student[i]=student[i],student[stu_min]
    stu_min=stu_init+1
    stu_init+=1
print()
for x in range(len(student)):
    print('student[%2d]  : name(%s), st_id(%d), major(%-3s, GPA(%5.2f))'%(x,student[x][0],student[x][1],student[x][2],student[x][3]))
stu_min=0
stu_init=0
for i in range(len(student)):
    for j in range(1+i,len(student)):
        if student[stu_min][3] < student[j][3]:
            stu_min=j
        elif student[stu_min][3] == student[j][3]:
            if student[stu_min][0] > student[j][0]:
                stu_min=j
    student[stu_min],student[i]=student[i],student[stu_min]
    stu_min=stu_init+1
    stu_init+=1
print()
for x in range(len(student)):
    print('student[%2d]  : name(%s), st_id(%d), major(%-3s, GPA(%5.2f))'%(x,student[x][0],student[x][1],student[x][2],student[x][3]))