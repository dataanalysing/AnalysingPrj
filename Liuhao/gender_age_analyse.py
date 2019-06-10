'''
    对用户的年龄、性别进行统计分析
    2019-6-10
'''
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gender_age = pd.read_csv("../data/data/gender_age_train.csv",nrows=500000)

ages = pd.cut(gender_age['age'],[0,15,20,25,30,35,40,45,50,100])

ages = {'age':ages.values}

ages = pd.DataFrame(ages)

ages = ages.groupby('age').size()

print(ages.values.tolist())

plt.figure(figsize=(15,7))
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('年龄分布情况')
plt.xlabel("年龄段")
plt.ylabel("人数")
age_list = ['15岁以下','15-20岁','20-25岁','25-30岁','30-35岁','35-40岁','40-45岁','45-50岁','50岁以上']
plt.xticks(np.arange(len(age_list)),age_list,rotation=45)
plt.bar(age_list, ages.values.tolist(),color='#ff4777')
plt.show()