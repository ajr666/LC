a = '-198'
print(int(a) + 1)

# 在 Python 中，单引号 (') 和双引号 (") 都可以用来定义字符串，它们在功能上没有区别。
# 所以，'123adk' 和 "123adk" 都表示相同的字符串 "123adk"。

#'a' 是 chr 还是 str？
# 在 Python 中，'a' 是一个字符串对象（str），而不是 chr。
# Python 并没有一个专门的字符类型，所有的字符都被看作是长度为 1 的字符串。

# chr()函数, 作用与ord()相反
# 功能：chr() 是 Python 中的一个内置函数，用于将Unicode编码值转换为对应的字符。
# 语法：chr(i)，其中 i 是一个整数，表示 Unicode 编码值。
# 返回值：返回对应 Unicode 编码值的字符。
print(chr(97))  # 输出: 'a'
print(chr(65))  # 输出: 'A'
print(chr(8364))  # 输出: '€'，这是欧元符号

# Python 中的字符串 (str) 是不可变对象，这意味着一旦创建了字符串，其内容就不能通过索引进行修改
# 如何修改字符串：先转成列表，修改完再转回字符串
s = '123456'
sl = list(s) # ['1', '2', '3', '4', '5', '6']
sl[0], sl[5] = sl[5], sl[0]
s = ''.join(sl)
print(s)

s = "Hello, World!"

# 查找和替换
print(s.find("World"))  # 输出: 7
print(s.replace("World", "Python"))  # 输出: "Hello, Python!"

# 分割和连接
sl = s.split(", ")  # 按逗号分隔 输出: ['Hello', 'World!']
print(sl)
print(" ".join(['Hello', 'Python']))  # 按空格连接list 输出: "Hello Python"

# 大小写转换
print(s.lower())  # 输出: "hello, world!"
print(s.upper())  # 输出: "HELLO, WORLD!"

# 去除空格
print("   Hello, World!   ".strip())  # 输出: "Hello, World!"

# 判断字符串
print(s.isalpha())  # 输出: False, 因为有逗号和空格
print("123".isdigit())  # 输出: True

# 翻转字符串
s = s[:: -1]
print(s)


