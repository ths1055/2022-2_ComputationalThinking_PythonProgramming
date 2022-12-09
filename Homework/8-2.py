from Class_Mtrx import*

def fgetMtrx(name, f_in):
    str_line=f_in.readline()
    row,col=map(int,str_line.split())
    L_A=[]
    for i in range(row):
        L_row=list(map(float,f_in.readline().split()))
        for j in range(col):
            L_A.append(L_row[j])
    return Mtrx(name,row,col,L_A)

if __name__ == "__main__":
    fin = open("matrix_data.txt", "r")
    fout = open("result.txt", "w")
    mA = fgetMtrx("mA", fin); print(mA); fout.write("{}".format(mA))
    mB = fgetMtrx("mB", fin); print(mB); fout.write("{}".format(mB))
    mC = fgetMtrx("mC", fin); print(mC); fout.write("{}".format(mC))
    fin.close()
    mD = mA + mB
    mD.setName("mD = mA + mB")
    print(mD); fout.write("{}".format(mD))
    mE = mA - mB
    mE.setName("mE = mA - mB")
    print(mE); fout.write("{}".format(mE))
    mF = mA * mC
    mF.setName("mF = mA * mB")
    print(mF); fout.write("{}".format(mF))
    fout.close()