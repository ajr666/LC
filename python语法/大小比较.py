## 字符可以比较大小
'a' > 'c'  # False
print('a' < 'c')  # 输出: True
print('a' == 'a') # 输出: True


# 字符串字典序比较
print("apple" < "banana")  # True
print("abc" < "abcd")      # True
print("abcd" > "abcf")     # False


# 字典序比较大小写敏感
print("Apple" < "apple")   # True, 'A' 的 Unicode 值小于 'a'


# 空字符串始终小于任何非空字符串
print("" < "abc")          # True