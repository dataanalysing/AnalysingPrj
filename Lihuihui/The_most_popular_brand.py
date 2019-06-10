import pandas as pd
import matplotlib.pyplot as plt


filepath = "../data/data/phone_brand_device_model.csv"
brand_data = pd.read_csv(filepath, index_col=0)

print("****************************************")
# 使用info打印每列的信息
print('数据集的大小为：', brand_data.shape)
print("****************************************")
# 查看数据前五行
print('数据集的前五行为：', brand_data.head())
print("****************************************")
# describe Test 描述统计
print('手机品牌及型号数据的描述性统计为：', brand_data.describe())
print("****************************************")

brand_group = brand_data[['phone_brand']].groupby(by='phone_brand', as_index=False).size()


# 通过对手机品牌出现的次数进行排名，求取较受欢迎(前6名)的手机品牌
brand_popularity = brand_group.sort_values(ascending=False)
print('最受欢迎的手机品牌及出现次数如下(排序前6)：\n', brand_popularity[0:6])
print("****************************************")

brand_name = brand_popularity.index.tolist()
popular_brand_name = brand_name[0:6]
# 品牌总数
print('手机品牌总数为：', len(brand_name))
print("****************************************")

# 饼图中所需展示的品牌名
popular_brand_name.append('其他(含125个品牌)')

print('饼图中呈现品牌：', popular_brand_name)
print("****************************************")

brand_counts = brand_popularity.values.tolist()
popular_brand_counts = brand_counts[0:6]
# 饼图中所需展示的品牌名对应的出现次数
popular_brand_counts.append(sum(brand_counts[6:]))

print('饼图中呈现品牌对应的出现次数：', popular_brand_counts)
print("****************************************")

# 所有品牌的出现次数总和
print(sum(brand_counts))
print("****************************************")

plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文显示为黑体字
plt.rcParams['savefig.dpi'] = 100 # 图片像素
plt.rcParams['figure.dpi'] = 100 # 分辨率
plt.title('手机品牌受欢迎占比情况') # 标题
label = popular_brand_name # 饼图中各项的名称
explode = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01] # 饼图中各项离圆心的距离(n个半径)
plt.pie(popular_brand_counts, explode=explode, labels=popular_brand_name, autopct='%1.1f%%', radius=1)

plt.show()