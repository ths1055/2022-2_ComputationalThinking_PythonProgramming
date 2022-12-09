def read_file(fileName):
    student_data=[]
    f=open(fileName,'r')
    for i in f:
        student_name,score_kor,score_eng,score_math,score_sci=i.split()
        student_data_temp=[student_name,int(score_kor),int(score_eng),int(score_math),int(score_sci)]
        student_data.append(student_data_temp)
    f.close()
    return student_data

def write_file(fileName,dataFile):
    f=open(fileName,'w')
    f.write('%5s  |%5s%5s%5s%5s%6s%6s\n'%('name','kor','eng','math','sci','sum','avg'))
    f.write('-----------------------------------------\n')
    for i in range(len(dataFile)):
        f.write("%4s   : %4d,%4d,%4d,%4d,%5d,%6.2f\n"%(dataFile[i][0],dataFile[i][1],dataFile[i][2],dataFile[i][3],dataFile[i][3],dataFile[i][3],dataFile[i][3]))
    f.close()

def cal_score(data_file):
    sum_kor=sum_eng=sum_math=sum_sci=0
    studentNumber=len(data_file)
    for i in range(studentNumber):
        sum_score=data_file[i][1]+data_file[i][2]+data_file[i][3]+data_file[i][4]
        sum_kor+=data_file[i][1];sum_eng+=data_file[i][2];sum_math+=data_file[i][3];sum_sci+=data_file[i][4]
        data_file[i].append(sum_score);data_file[i].append(sum_score/4)
    avg_kor = sum_kor / studentNumber
    avg_eng = sum_eng / studentNumber
    avg_math = sum_math / studentNumber
    avg_sci = sum_sci / studentNumber
    return avg_kor, avg_eng, avg_math, avg_sci

def main():
    students=read_file('student_records.txt')
    for n in students:
        print(n)
    avg_kor,avg_eng,avg_math,avg_sci=cal_score(students)
    print('\nAfter calculate_scores(students)')
    print('==========================================')
    print('%5s  |%5s%5s%5s%5s%6s%6s'%('name','kor','eng','math','sci','sum','avg'))
    print('-------+---------------------------------')
    for i in range(len(students)):
        print("%4s   : %4d,%4d,%4d,%4d,%5d,%6.2f"%(students[i][0],students[i][1],students[i][2],students[i][3],students[i][3],students[i][3],students[i][3]))
    print('==========================================\n')
    write_file('output.txt',students)

    print("\nAverage score of each class :")
    print("Kor_avg = {:5.2f}".format(avg_kor))
    print("Eng_avg = {:5.2f}".format(avg_eng))
    print("Math_avg = {:5.2f}".format(avg_math))
    print("Sci_avg = {:5.2f}".format(avg_sci))
    
if __name__ == "__main__":
    main()