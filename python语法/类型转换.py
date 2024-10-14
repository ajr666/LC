## str 和 int 互转
a = 123
s = str(a) # '123'

b = '123'
c = int(b) # 123

b = '-5' # 负数也可以直接转
c = int(b) # -5

b = '-33.4'
c = float(b)
print(c)


## int 转 list
num = 123
a = [int(d) for d in str(num)] 

num_s = str(num)