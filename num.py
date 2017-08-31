import timeit
start=timeit.default_timer()
a=1000000000
for b in range(1000000):
    a=a+1e-6

end=timeit.default_timer()
print(a-1000000000)
print(end-start)