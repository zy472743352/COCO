name = ['赵日天','王日地','李日空气','孙日阳','胡日月']
print  (name[0])
print  (name[1])
print  (name[2])
print  (name[3])
print  (name[4])
print  (name[0] + "喜欢" + name[3])
name[4] = "张三"#替换
print  (name[4])
name.append("李四")#增加一个新的元素
print  (name[5])
name.insert(1,"王五")#在任意位置插入元素
print  (name)
del name[0]#删除任意位置元素
print  (name)
name1 = name.pop()#pop相当于一个剪切命令，把列表中最后一个元素剪切出来
print (name1)
print  (name)
name.remove('李日空气')#当我们不知道需要删除的元素在第几位时，可以用remove
print  (name)


