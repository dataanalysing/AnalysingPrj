import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "../data/data/phone_brand_device_model.csv"
brand_data = pd.read_csv(filepath, usecols=[1, 2])

xiaomi_data = brand_data[brand_data['phone_brand'].isin(['小米'])]

xiaomi_model = xiaomi_data[['device_model']].groupby(by='device_model', as_index=False).size()

# 通过对小米手机型号出现的次数进行排名，求取较受欢迎(前5名)的小米手机型号
xiaomi_popularity = xiaomi_model.sort_values(ascending=False)
print('最受欢迎的小米手机型号及出现次数如下(排序前5)：\n', xiaomi_popularity[0:5])
print("****************************************")
# print(xiaomi_popularity)

model_name = xiaomi_popularity.index.tolist()
popular_model_name = model_name[0:12]

# 型号总数
print('小米手机型号种数为：', len(model_name))
print("****************************************")

# 饼图中所需展示的品牌名
popular_model_name.append('其他(含14个型号)')

print('直方图中呈现品牌：', popular_model_name)
print("****************************************")

model_counts = xiaomi_popularity.values.tolist()
popular_model_counts = model_counts[0:12]
# 饼图中所需展示的品牌名对应的出现次数
popular_model_counts.append(sum(model_counts[12:]))

print('直方图中呈现品牌对应的出现次数：', popular_model_counts)
print("****************************************")

plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文显示为黑体字
plt.rcParams['savefig.dpi'] = 100 # 图片像素
plt.rcParams['figure.dpi'] = 100 # 分辨率
plt.figure(figsize=(30, 7))
plt.title('小米手机型号受欢迎情况') # 标题
plt.xlabel("被使用数")
plt.ylabel("被使用数手机型号")
plt.xticks(np.arange(13), popular_model_name[0:13], rotation=45)
plt.bar(popular_model_name[0:13], popular_model_counts[0:13])
plt.show()