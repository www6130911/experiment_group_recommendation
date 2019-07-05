import denoise_autoencoder.util as util
from denoise_autoencoder.bean import autoencoder,nn
import numpy as np
# 测试数据，x为输入，y为输出
x = np.array([[0,0,1,0,0],
            [0,1,1,0,1],
            [1,0,0,0,1],
            [1,1,1,0,0],
            [0,1,0,1,0],
            [0,1,1,1,1],
            [0,1,0,0,1],
            [0,1,1,0,1],
            [1,1,1,1,0],
            [0,0,0,1,0]])
y = np.array([[0],
            [1],
            [0],
            [1],
            [0],
            [1],
            [0],
            [1],
            [1],
            [0]])
#################################
# step1 建立autoencoder
# 弄两层autoencoder，其中5为输入的维度
nodes=[5,3,2]
# 建立auto框架
ae = util.aebuilder(nodes)
# 设置部分参数
# 训练，迭代次数为6000
ae = util.aetrain(ae, x, 6000)
##############################
# step2 微调
# 建立完全体的autoencoder，最后层数1为输出的特征数
nodescomplete = np.array([5,3,2,1])
aecomplete = nn(nodescomplete)
# 将之前训练得到的权值赋值给完全体的autoencoder
# 训练得到的权值，即原来的autoencoder网络中每一个autoencoder中的第一层到中间层的权值
for i in range(len(nodescomplete)-2):
    aecomplete.W[i] = ae.encoders[i].W[0]
# 开始进行神经网络训练，主要就是进行微调
aecomplete = util.nntrain(aecomplete, x, y, 3000)
# 打印出最后一层的输出
print(aecomplete.values[3])
