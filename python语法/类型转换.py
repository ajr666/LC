## str 和 int 互转
a = 123
s = str(a) # '123'

b = '123'
c = int(b) # 123

b = '5'
c = int(b) # 5

b = "123"
c = int(b) # 123


## int 转 list
num = 123
a = [int(d) for d in str(num)] 