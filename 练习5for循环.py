for i in range(0,21):
	print(i)
m = []
for i in range(0,1000001):
	m.append(i)#创建了1~1000000的列表
print (min (m))
print (max (m))
print (sum (m))

m = [i for i in range(0,1000001)]#创建了1~1000000的列表
print(m[0:3])
print(m[:3])


