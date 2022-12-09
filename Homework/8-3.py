import pandas as pd

data_table = pd.read_excel("student_scores.xlsx")
print("data_table = \n", data_table)
data_table_tmp = data_table.loc[:, ['Eng', 'Kor', 'Math', 'Sci']]

average_student_row = data_table_tmp.mean(1) # mean with axes 1 (row, student) mean-> 평균
data_table.loc[:, 'Avg'] = average_student_row #일반 리스트와는 다르게 그냥 던져넣어도 자동정렬됨.

data_table_tmp = data_table.loc[:, ['Eng', 'Kor', 'Math', 'Sci', 'Avg']]
average_kind = data_table_tmp.mean() # mean with axes 0 (column, class)
print("\naverages_per_class =")
print(average_kind)

data_table_sorted = data_table.sort_values(by='Avg', ascending=False)
data_table_sorted.loc[len(data_table_sorted), ['Eng', 'Kor', 'Math', 'Sci', 'Avg']]=average_kind#loc은 여러개 가능 at은 하나만 지정
data_table_sorted.at[len(data_table_sorted)-1, 'st_name'] = 'Total_Avg'

print("\ndata_table_sorted_with_avg =")
print(data_table_sorted)
print("Writing data_table to excel file")

with pd.ExcelWriter("processed_scores.xlsx") as excel_writer:#직접 코드쳐서 끝내지 않아도 지가 알아서 끝냄
    data_table_sorted.to_excel(excel_writer, sheet_name='Student Records')