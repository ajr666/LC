# 二维数组排序
arr = [[1, 3], [2, 2], [3, 1], [4, 1]]

sorted_arr = sorted(arr, key=lambda x: x[0])
print(sorted_arr)

sorted_arr = sorted(arr, key=lambda x: x[1])
print(sorted_arr)

sorted_arr = sorted(arr, key=lambda x: (x[1], x[0]))
print(sorted_arr)

# 递减排序，reverse=True
sorted_arr = sorted(arr, key=lambda x : (x[1], x[0]), reverse=True)


# dict 排序
my_dict = {'b': 2, 'a': 3, 'c': 1, 'd':2}
print(my_dict)
print(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))
sorted_by_key = dict(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))
print(sorted_by_key)  # 输出: {'a': 3, 'b': 2, 'c': 1}


# codesignal平台无法使用lamda, 自定义一个函数作为 key 参数来进行排序
def sort_key(x):
    return (x[1], x[0])

t = sorted(my_dict.items(), key=sort_key)
my_dict = dict(t)
print(t)

arr = sorted(arr, key=sort_key)
print(arr)


# 复杂排序 cmp_to_key
from functools import cmp_to_key

def compare(x, y):
    # 按第一个元素递减排序
    if x[0] > y[0]:
        return -1
    elif x[0] < y[0]:
        return 1
    # 如果第一个元素相等，则按第二个元素递增排序
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            return 0

# 示例数组：先按第一个元素递减，再按第二个元素递增
array = [[1, 2], [3, 1], [2, 3], [2, 1]]
# 使用 cmp_to_key 进行排序
sorted_array = sorted(array, key=cmp_to_key(compare))
print(sorted_array)
