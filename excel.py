import xlrd
#import xlwt

txt=open('Family.txt','r')

xl=xlrd.open_workbook('FORITRI.xls')
sh=xl.sheet_by_index(0)
rows=sh.nrows
b=0
for n in range(0,67):
    a=txt.readline(0)
    aa=a.split("\n")
    aaa=aa[0]
    #print(aaa)
    for nn in range(1,rows):
        c=sh.cell(n,5)
        if c == aaa :
            b=b+1


print('{}\n'.format(aaa))
print(sh.cell(1,5))
#for n in range(1,rows):
#    print(sh.cell(n,5))



"""
for n in range(0,67):
    a=txt.readline()
    print(a)

"""