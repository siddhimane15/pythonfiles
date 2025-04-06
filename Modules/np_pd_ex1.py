
import pandas as pd
import numpy as np

data = np.random.rand(5,4)
print("Table:")
print(data)

data_frame = pd.DataFrame(data, columns=['A','B','C','D'])
print(data_frame)
data_frame['E']=None

column1 = data_frame['D']
print(column1)

# data=np.random.rand(7,5)
# print('Table:')
# print(data)

# data_frame =pd.DataFrame(data,columns=['A','B','C','D','E'])
# print(data_frame)

#add a column to the existing data

data_frame['Total'] = data_frame['A']+data_frame['B']+data_frame['C']+data_frame['D']
print(data_frame)

mean = data_frame.mean()
print(mean)

median=data_frame.median()
print(median)

mode=data_frame.mode()
print(mode)

#data_frame.to_csv(r'C:/Users/Sid/Desktop/siddhi_files/Table1.csv',index=True)
print("saved")