import numpy as np
import re
from sklearn import preprocessing


'''
Meetup Group序号: G_0——G_630
group_tag的最大长度为13
group_tag : list

Tag序号： T_0——T_1512
'''


group_tag_filepath = "./dataset/Meetup_data/CA/train/group_tags.txt"


def get_number(str):
    f1 = re.findall('(\d+)', str)
    num = int(f1[0])
    return num


def generate_one_hot(data, classes):
    label = np.array(data)                                 # 标签数据，标签从0开始
    classes = classes
    one_hot_label = np.zeros(shape=(label.shape[0],classes))        # 生成全0矩阵
    one_hot_label[np.arange(0, label.shape[0]), label] = 1            # 相应标签位置置1
    # print(one_hot_label)


def get_groupid_and_tagid_onehot(filepath):
    group_tag_dict = dict()
    arr = []
    for line in open(filepath):
        group_tag = line.strip().split(" ")
        groupLens = len(group_tag)

        group_name = group_tag[0]
        group_tag_dict.update(G_1=[" ".join(group_tag[1:len(group_tag)])])
        for i in range(groupLens - 1):
            temp = get_number(group_tag[i + 1])
            arr.append(temp)
            print(arr)






get_groupid_and_tagid_onehot(group_tag_filepath)



# data = [67,68,69,84]
# classes = max(data)+1
# generate_one_hot(data, classes)