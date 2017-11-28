# --*--coding:utf-8--*--

'''
@version:python 2.7
@author:com0716
@file:FolderTraversal.py
@time:2017/11/28 21:28
'''


def eachFile(path):
    import os
    pathDir = os.listdir(path)#列举当前文件夹下的文件和文件夹
    for s in sorted(pathDir, key=lambda x: x[1]):
        newDir = os.path.join(path, s)
        if os.path.isfile(newDir):#判断是否为文件
            if os.path.splitext(newDir)[1] == ".py":#判断文件后缀类型
                print newDir[3:],"is a python file"
        else:
            print newDir[3:],"is a directory"
            eachFile(newDir)#递归执行

if __name__ == '__main__':
    eachFile('..')