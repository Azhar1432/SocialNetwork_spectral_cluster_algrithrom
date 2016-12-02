# encoding=utf-8
#G为连接矩阵，将G划分为G1和G2两个社区
#G1,G2与G规格相同
import numpy as np
def Divide2(G,node_G,ncV):

    #将G的对角线初始化为0
    G = G - np.diag(G)
    #G中节点数
    size_of_G = G.shape
    Number = size_of_G[0]
    #求G中的非零元素，返回一个行向量,向量元素为下标
    index_list1 = []
    #每一列相加
    index = 0
    for each in np.sum(G,axis=0):
        if(each != 0):
            index_list1.append(index)
            index = index + 1
    for each in np.sum(G,axis=1):
        if(each != 0 and each not in index_list1):
            index_list1.append(index)
    #这里的下标是python的 要注意！
    NonNumber = index_list1

    #求G中的非零元素，返回一个行向量,向量元素为下标
    index_list2 = []
    #每一列相加
    for each in np.sum(G,axis=0):
        if(each == 0):
            index_list1.append(each)
    for each in np.sum(G,axis=1):
        if(each != 0 and each in index_list2):
            index_list2.append(each)
    ZNumber = index_list2



    #清除所有零元素的行和列，？？？？？？？？？？？？这有啥用
    Gd = G
    for each in ZNumber:
        Gd[each,:] = 0
        Gd[:,each] = 0

    #初始化G1,G2都为0
    G1 = np.arange(Number).reshape(Number, 1)
    for i in range(Number):
        G1[i,0] = 0
    G2 = np.arange(Number).reshape(Number, 1)
    for i in range(Number):
        G2[i,0] = 0
    #初始化并计算tncV

    tncV = 0
    for i in range(Number):
        if(i in NonNumber):
            if(ncV[tncV] == 1):
                G1[i] = 1
                tncV = tncV + 1
            elif(ncV[tncV] == 2):
                G2[i] = 1
                tncV = tncV + 1

    #将第一个社区的节点变成矩阵
    transposed_G1 = np.transpose(G1)
    G1 = np.dot(G1, transposed_G1)
    for i in range(Number):
        for j in range(Number):
            G1[i][j] = G1[i][j] * G[i][j]


    transposed_G2 = np.transpose(G2)
    G2 = np.dot(G2,transposed_G2)
    for i in range(Number):
        for j in range(Number):
            G2[i][j] = G2[i][j] * G[i][j]
    #构造nodes_G1和 nodes_G2
    nodes_G1 = []
    nodes_G2 = []
    for i in range(Number):
        for j in range(Number):
            if(G1[j][i] == 1):
                nodes_G1.append(node_G[j])
            if(G2[j][i] == 1):
                nodes_G2.append(node_G[j])

    nodes_G1 = sorted(np.unique(nodes_G1))
    nodes_G2 = sorted(np.unique(nodes_G2))


    #删除G1和G2的全0行和列
    #下面这一段这个太难写了 我真是天才，建议好好阅读
    G1_s = G1.shape[0]
    for i in range(G1.shape[0]):
        delta = G1_s-G1.shape[0]
        i = i - delta
        if 1 not in G1[i,:]:
            G1 = np.delete(G1,i,axis=0)
    G1_s = G1.shape[1]
    for i in range(G1.shape[1]):
        delta = G1_s-G1.shape[1]
        i = i - delta
        if 1 not in G1[:,i]:
            G1 = np.delete(G1,i,axis=1)


    G2_s = G2.shape[0]
    for i in range(G2.shape[0]):
        delta = G2_s-G2.shape[0]
        i = i - delta
        if 1 not in G2[i,:]:
            G2 = np.delete(G2,i,axis=0)

    G2_s = G2.shape[1]
    for i in range(G2.shape[1]):
        delta = G2_s-G2.shape[1]
        i = i - delta
        if 1 not in G2[:,i]:
            G2 = np.delete(G2,i,axis=1)

    result_list = []
    result_list.append(G1)
    result_list.append(G2)
    result_list.append(nodes_G1)
    result_list.append(nodes_G2)

    return  result_list