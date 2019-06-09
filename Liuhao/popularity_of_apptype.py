import csv
import pandas as pd
import numpy as np

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
