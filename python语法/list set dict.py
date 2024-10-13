## list
nums = [1, 2, 3]
nums.extend(nums) # 拓展两倍 使用append会导致循环引用问题

path = [0, 1, 2]
res = []
res.append(path[:]) # 切片操作拷贝一份path，后续更改path也不妨碍   

a = [7, 8 ,9]
b = [7, 8, 9]
print(a == b) # True python可以直接判断list是否相等

## set
st = set()
st = {1, 2, 3}

st.add(5)
st.remove(2) # remove() 如果元素不存在会引发 KeyError，而 discard() 不会
st.discard(8)


## dict
cnt = dict()
cnt = {'a': 1, 'p':2, 'l':1, 'e':1}

cnt['x'] = 3
cnt.pop['a']


## defaultdict 不会引发key error 
from collections import defaultdict
count = defaultdict(int)  # 默认值为 0  
count['apple'] += 1  
count['banana'] += 2  


## 子数组求和
nums = [1, 3, 5, 7, 9, 2, 4]
sub_sum = sum(nums[2:6]) # [2, 6)


## 字符与整数相加 
char = 'a'
next_char = chr(ord(char) + 1) # chr可以实现int转字符
print(next_char)  # 输出: 'b'


## 将整数转换为二进制字符串
number = 42
binary_representation = bin(number)
print(f"The binary representation of {number} is {binary_representation}")
print(bin(number)[2:]) # 去除0b


# 取模
MOD = 1_000_000_009
ans = 9929393494
ans = ans % MOD # 如果MOD = 1e9 + 9,算出来是小数


# 计数
from collections import Counter, defaultdict

nums = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
cnt = Counter(nums)


## dict排序
sorted_cnt = sorted(cnt.items(), key = lambda x: (x[1], x[0]))