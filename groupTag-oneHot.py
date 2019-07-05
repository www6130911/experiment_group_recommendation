import numpy as np
import re

'''
Meetup Group序号: G_0——G_630, 但是没有G_376。 一共有630个group
group_tag的最大长度为13
group_tag : list

Tag序号： T_0——T_1512，一共1513个tag
'''

group_tag_filepath = "./dataset/Meetup_data/CA/train/group_tags.txt"

def getNumber(str):
    f1 = re.findall('(\d+)', str)
    num = int(f1[0])
    return num

Group_Tag=np.zeros((631,1513),float)        # 631是group的总个数， 1513是tag的总个数

arr = []
for line in open(group_tag_filepath):
    group_tag = line.strip().split(" ")     # group_tag : list,  group_tag的最大长度为13,
    groupLens = len(group_tag)
    groupid = getNumber(group_tag[0])
    # print(groupid)        #输出group id

    for i in range(groupLens-1):
        temp = getNumber(group_tag[i+1])
        arr.append(temp)
    # print("\n")         # 输出完一个group的tag,就换一行
    # print(arr)        # 输出每一个group的tag
    for j in range(len(arr)):
        # print(arr[j])     #输出每一个Zgroup id的每一个tag
        Group_Tag[groupid][arr[j]] = 1

    arr = []            # 重置arr





# print(Group_Tag.shape)
print(Group_Tag)
np.save("./Group_Tag.npy", Group_Tag)    # 保存numpy array到磁盘，读取使用b = np.load("filename.npy")

# Group_Tag_concatenate = Group_Tag.reshape(1,631*1513)         # 将group中的tag使用one-hot编码，将其拼接到一起
#
#
# print(Group_Tag_concatenate)
# print(len(Group_Tag_concatenate[0]))
# np.save("./Group_Tag_concatenate.npy", Group_Tag_concatenate)    # 保存numpy array到磁盘，读取使用b = np.load("filename.npy")


# Group_Tag_concatenate.tofile("Group_Tag_concatenate.bin")


