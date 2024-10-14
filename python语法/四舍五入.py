# 四舍五入
print(round(3.5))  # 输出: 4
print(round(3.4))  # 输出: 3
print(round(2.5))  # 输出: 2 当值在小数点 .5 的位置时，round默认对偶数进行舍入

import math
# 向上取整
print(math.ceil(3.1))  # 输出: 4
print(math.ceil(-3.1)) # 输出: -3

# 向下取整
print(math.floor(3.9))  # 输出: 3
print(math.floor(-3.1)) # 输出: -4

# 截断取整
print(math.trunc(3.9))   # 输出: 3
print(math.trunc(-3.9))  # 输出: -3