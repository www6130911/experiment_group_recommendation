
'''
cooccur = {
	0: {                #groupid
		0: 1.0,         #tagid : 出现次数
		2: 3.5          #tagid : 出现次数
	},
	1: {                #groupid
		2: 0.5          #tagid : 出现次数
	},
	2: {                #groupid
		0: 3.5,         #tagid : 出现次数
		1: 0.5,         #tagid : 出现次数
		2: 1.2          #tagid : 出现次数
	}
}
'''

import numpy as np
import re
# np.set_printoptions(threshold=np.inf)       # 显示数组中的所有数据，去掉...




datapath = 'D:/PythonProject/Experiments/dataset/Meetup_data/CA/train/group_tags.txt'

def getNumber(str):
    f1 = re.findall('(\d+)', str)
    num = int(f1[0])
    return num

matrix = []
group_count = 630
tag_count = 1513
for line in open(datapath):
    group_tag = line.strip().split(" ")
    matrix.append(group_tag[1:len(group_tag)])

# print(matrix)

cooccurrence = [[0 for i in range(group_count)] for j in range(group_count)]
i_index = 0
j_index = 0
for i in matrix:
    # print(i)        # 0,1,2,3,4
    for j in matrix:
        if j != i:
            for count in range(len(j)):
                if j[count] in i:
                    cooccurrence[i_index][j_index] += 1
        j_index += 1
    i_index += 1
    j_index = 0


# cooccurrence_np = np.array(cooccurrence)            # 将list转化成numpy格式
# # print(cooccurrence_np)
# np.save("./cooccurrence_np.npy", cooccurrence_np)    # 保存numpy array到磁盘，读取使用b = np.load("filename.npy")





coocs = np.transpose(np.nonzero(cooccurrence))    # 现在 coocs的每一行就是非零元素所在的坐标

# print(cooccurrence[0][9])
# print(coocs)            # coocs[0]表示 [0 7],coocs[0][0] 表示0 coocs[0][1] 表示7


# 创造嵌套字典模式
cooccurrence_dict = {}
temp_dict = {}

for i in range(630):
    for j in coocs:
        if j[0] == i:
            temp = dict({j[1]: cooccurrence[j[0]][j[1]]})
            temp_dict.update(temp)
        else:
            cooccurrence_dict.update(dict({i: temp_dict}))
            temp_dict = {}
            break
# print(cooccurrence_dict)


import glove

model = glove.Glove(cooccurrence_dict, d=50, alpha=0.75, x_max=100.0)

for epoch in range(25):
	err = model.train(workers=9, batch_size=50)
	print("epoch %d, error %.3f" % (epoch, err), flush=True)


print(model.W)		# The trained embeddings are now present under model.W.

# np.save("./cooccurrence_WeightMatrix.npy", model.W)     # 保存共现矩阵的权重

