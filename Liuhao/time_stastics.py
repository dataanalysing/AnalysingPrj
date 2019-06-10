'''
    统计app使用时间规律
    2019-6-9
'''

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def convert_to_date(ele):
    ele = ele.split()[0]
    return ele
def convert_to_hour(ele):
    ele =ele[5:13]
    ele = ele + "时"
    return ele

def delete_year(ele):
    ele = ele[5:]
    ele = ele + "日"
    return ele

def run():
    events = pd.read_csv("../data/data/events.csv", usecols=['timestamp'])
    print(events.head())
    events['timestamp'] = events['timestamp'].apply(convert_to_hour)
    time_count = events.groupby('timestamp').size()
    time_list = time_count.index.tolist()
    count_list = time_count.values.tolist()
    print(count_list)
    events = pd.read_csv("../data/data/events.csv", usecols=['event_id', 'timestamp'], nrows=1000000)

    app_events = pd.read_csv("../data/data/app_events.csv", usecols=['event_id', 'app_id'], nrows=1000000)
    app_labels = pd.read_csv("../data/data/app_labels.csv")  # app_id , label_id
    label_categories = pd.read_csv("../data/data/label_categories.csv")  # label_id category

    app_labels = pd.merge(app_labels, label_categories, how='outer', on=None, left_on=None, right_on=None,
                          left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True,
                          indicator=False, validate=None)
    events = pd.merge(events, app_events, how='outer', on=None, left_on=None, right_on=None, left_index=False,
                      right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
    events.dropna(inplace=True)
    app_labels.dropna(inplace=True)
    events['timestamp'] = events['timestamp'].apply(convert_to_hour)
    time_count = events.groupby('timestamp').size()

    count_list1 = time_count.values.tolist()

    #绘制折线图
    plt.figure(figsize=(30, 7))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(count_list[1:169],color = 'r')
    plt.plot(count_list1[1:169], color='g')
    plt.xlabel("时间")
    plt.ylabel("活跃量")
    plt.legend(["所有app","游戏类型app"])
    plt.title("2016年5月1日至5月7日，app活跃度随时间变化情况")
    plt.ylim((0,30000))
    plt.xticks(range(1,169,4),time_list[1:169:4],rotation=45)
    plt.show()
    pass



run()

