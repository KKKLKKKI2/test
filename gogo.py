import sayhello
import os
import timeit

path = './val'
file=open("val.txt",'w')
tstart=timeit.default_timer()
print("start")
for filename in (jpg for jpg in os.listdir(path) if jpg.endswith('.jpg')):
    a=filename[0][0]
    file.write('{}\n'.format(filename+" "+a))
file.close()
sayhello.sayhi()
tend=timeit.default_timer()
print(tend-tstart)