#-*- coding:utf-8 –*-
import os
import glob
import pandas as pd

def merge(Filepath):
    readHead = False
    file = Filepath + '*.csv'
    csv_list = glob.glob(file)
    print(u'共发现%s个CSV文件'% len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fsub = open(i, 'r')
        if readHead:
            fr = fsub.readline()
        else:
            readHead = True
        fr = fsub.read()
        with open('merge.csv','a') as f:
            f.write(fr)
    print(u'合并完毕！')
    if len(csv_list) == 0:
        return False
    else:
        return True

def quchong(file):
    #df = pd.read_csv(file, header=None)
    df = pd.read_csv(file)
    datalist = df.drop_duplicates('uid', keep='last')
    #datalist.to_csv(file, index=False, header=False)
    datalist.to_csv(file, index=False)

if __name__ == "__main__":
    if merge("C:/Users/Jovan/PycharmProjects/untitled2/"):
        quchong("C:/Users/Jovan/PycharmProjects/untitled2/merge.csv")

