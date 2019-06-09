import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "../data/data/phone_brand_device_model.csv"
brand_data = pd.read_csv(filepath, usecols=[1, 2])

sanxing_data = brand_data[brand_data['phone_brand'].isin(['三星'])]

sanxing_model = sanxing_data[['device_model']].groupby(by='device_model', as_index=False).size()

# 通过对三星手机型号出现的次数进行排名，求取较受欢迎(前5名)的三星手机型号
sanxing_popularity = sanxing_model.sort_values(ascending=False)
print('最受欢迎的三星手机型号及出现次数如下(排序前5)：\n', sanxing_popularity[0:5])
print("****************************************")
print(sanxing_popularity)

model_name = sanxing_popularity.index.tolist()
popular_model_name = model_name[0:47]

# 型号总数
print('三星手机型号种数为：', len(model_name))
print("****************************************")

# 条形图中所需展示的品牌名
popular_model_name.append('其他(含113个型号)')

popular_model_name.reverse()
print('条形图中呈现品牌：', popular_model_name)
print("****************************************")

model_counts = sanxing_popularity.values.tolist()
popular_model_counts = model_counts[0:47]
# 条形图中所需展示的品牌名对应的出现次数
popular_model_counts.append(sum(model_counts[47:]))

popular_model_counts.reverse()
print('条形图中呈现品牌对应的出现次数：', popular_model_counts)
print("****************************************")

plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文显示为黑体字
plt.rcParams['savefig.dpi'] = 100 # 图片像素
plt.rcParams['figure.dpi'] = 100 # 分辨率
plt.title('三星手机型号受欢迎情况') # 标题
plt.xlabel("被使用数")
plt.ylabel("手机型号")
plt.xticks()
plt.yticks(np.arange(0, 48), popular_model_name[0:48])
plt.barh(popular_model_name[0:48], popular_model_counts[0:48])
plt.show()