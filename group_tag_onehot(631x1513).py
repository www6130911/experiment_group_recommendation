import numpy as np
import re
# np.set_printoptions(threshold=np.inf)       # 显示数组中的所有数据，去掉...

'''
Meetup Group序号: G_0——G_630
group_tag的最大长度为13
group_tag : list

Tag序号： T_0——T_1512
'''
datapath = './dataset/Meetup_data/CA/test/group_tags.txt'

def getNumber(str):
    f1 = re.findall('(\d+)', str)
    num = int(f1[0])
    return num

'''
构造一个631x1513的矩阵
'''
matrix = np.zeros((631, 1513), dtype=float)     # Group序号: G_0——G_630，Tag序号： T_0——T_1512


# 生成group-tag交互矩阵,第i行表示第i个group交互过的tag i={0,1,2,...,630}
for line in open(datapath):
    group_tag = line.strip().split(" ")
    groupLens = len(group_tag)
    groupid = getNumber(group_tag[0])
    for i in range(groupLens-1):
        temp = getNumber(group_tag[i+1])
        matrix[groupid][temp] = 1

print(matrix)

np.save('./group_tag_onehot_train.npy', matrix)



