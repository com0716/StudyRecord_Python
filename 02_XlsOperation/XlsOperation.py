# --*--coding:utf-8--*--

'''
@version:python 2.7
@author:com0716
@file:XlsOperation.py
@time:2017/11/28 21:49
'''
def createXls(outFileName):
    import xlwt
    wb = xlwt.Workbook()
    ws = wb.add_sheet(u"result sheet")

    ws.write(0, 0, u"时间")
    for i in range(128):
        ws.write(0, i+1, i+1)

    wb.save(outFileName)

if __name__ == '__main__':
    createXls("d:/demo.xls")