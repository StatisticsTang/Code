L = list(range(10))
#print(L)
#print(type(L[0]))

L2 = [str(c) for c in L] #创建一个字符串列表
print(L2)
print(type(L2[0]))

L3 = [True, "2", 3.0, 4]
print([type(item) for item in L3])
