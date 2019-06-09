import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app_labels = pd.read_csv("../data/data/app_labels.csv")              #app_id , label_id
label_categories = pd.read_csv("../data/data/label_categories.csv")  #label_id category

print(app_labels.head())
print(label_categories.head())


app_labels=pd.merge(app_labels, label_categories, how='outer', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)

app_labels.dropna(inplace=True)

app_labels_count = app_labels.groupby("category",as_index=False).size().sort_values(ascending=False)

type_names = app_labels_count.index.tolist()
type_counts = app_labels_count.values.tolist()

print(type_names)
print(type_counts)

plt.rcParams['font.sans-serif']=['SimHei']
plt.title('app类型热度前20名')
plt.xlabel("热度")
plt.ylabel("类型")
plt.xticks(np.arange(20),type_names[0:20],rotation=45)
plt.bar(type_names[0:20],type_counts[0:20])
plt.show()
