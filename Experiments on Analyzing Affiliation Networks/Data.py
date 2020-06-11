import pandas as pd
import methods

csv_data = pd.read_csv("./list1.csv", error_bad_lines=False, skiprows=None)
csv_data = csv_data.values
date_list = methods.Data_process.generate_row_list(csv_data)
people_list = methods.Data_process.generate_col_list(csv_data)
relation_list = methods.Data_process.generate_relation_lsit(csv_data)
all_list = people_list + date_list
list_D = ['Node', 'No. of Ties', 'Normalized Degree', 'Normalized Closeness', 'Normalized Betweenness',
          'Normalized Eigenvector']
'''evaluation quantity'''
print(people_list, '\n', date_list, '\n', relation_list)

'''
Data Visualization

people_list = ['FLORA', 'OLIVIA', 'MYRNA', 'HELEN', 'KATHERINE', 'NORA', 'SYLVIA', 'VERNE', 'DOROTHY',
               'PEARL', 'RUTH', 'EVELYN', 'THERESA', 'LAURA', 'BRENDA', 'FRANCES', 'ELEANOR', 'CHARLOTTE']

date_list = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14']

relation_list = [('FLORA', 'E9'), ('FLORA', 'E11'),
                 ('OLIVIA', 'E9'), ('OLIVIA', 'E11'),
                 ('MYRNA', 'E8'), ('MYRNA', 'E9'), ('MYRNA', 'E10'), ('MYRNA', 'E12'),
                 ('DOROTHY', 'E8'), ('DOROTHY', 'E9'),
                 ('HELEN', 'E7'), ('HELEN', 'E8'), ('HELEN', 'E10'), ('HELEN', 'E11'), ('HELEN', 'E12'),
                 ('NORA', 'E6'), ('NORA', 'E7'), ('NORA', 'E9'), ('NORA', 'E10'), ('NORA', 'E11'), ('NORA', 'E12'),
                 ('NORA', 'E13'), ('NORA', 'E14'),
                 ('SYLVIA', 'E7'), ('SYLVIA', 'E8'), ('SYLVIA', 'E9'), ('SYLVIA', 'E10'), ('SYLVIA', 'E12'),读取xlsx文件报错IndexError: list index out of range
                 ('SYLVIA', 'E13'), ('SYLVIA', 'E14'),
                 ('KATHERINE', 'E8'), ('KATHERINE', 'E9'), ('KATHERINE', 'E10'), ('KATHERINE', 'E12'),
                 ('KATHERINE', 'E13'), ('KATHERINE', 'E14'),
                 ('VERNE', 'E7'), ('VERNE', 'E8'), ('VERNE', 'E9'), ('VERNE', 'E12'),
                 ('RUTH', 'E5'), ('RUTH', 'E7'), ('RUTH', 'E8'), ('RUTH', 'E9'),
                 ('PEARL', 'E6'), ('PEARL', 'E8'), ('PEARL', 'E9'),
                 ('ELEANOR', 'E5'), ('ELEANOR', 'E6'), ('ELEANOR', 'E7'), ('ELEANOR', 'E8'),
                 ('FRANCES', 'E3'), ('FRANCES', 'E5'), ('FRANCES', 'E6'), ('FRANCES', 'E8'),
                 ('CHARLOTTE', 'E3'), ('CHARLOTTE', 'E4'), ('CHARLOTTE', 'E5'), ('CHARLOTTE', 'E7'),
                 ('BRENDA', 'E1'), ('BRENDA', 'E3'), ('BRENDA', 'E4'), ('BRENDA', 'E5'), ('BRENDA', 'E6'),
                 ('BRENDA', 'E7'), ('BRENDA', 'E8'),
                 ('THERESA', 'E2'), ('THERESA', 'E3'), ('THERESA', 'E4'), ('THERESA', 'E5'), ('THERESA', 'E6'),
                 ('THERESA', 'E7'), ('THERESA', 'E8'), ('THERESA', 'E9'),
                 ('LAURA', 'E1'), ('LAURA', 'E2'), ('LAURA', 'E3'), ('LAURA', 'E5'), ('LAURA', 'E6'), ('LAURA', 'E7'),
                 ('LAURA', 'E8'),
                 ('EVELYN', 'E1'), ('EVELYN', 'E2'), ('EVELYN', 'E3'), ('EVELYN', 'E4'), ('EVELYN', 'E5'),
                 ('EVELYN', 'E6'), ('EVELYN', 'E8'), ('EVELYN', 'E9'), ]
'''

'''
xlsx_data= []
xlsx_data = pd.read_excel("./SocapForm-Ieiri_ver3.xlsx", sheet_name='DataLabel')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
pd.set_option('max_colwidth',1000)
xlsx_data = np.array(xlsx_data)
print(xlsx_data)
'''