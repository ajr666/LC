import bisect

arr = [1, 3, 4, 7, 8]

# 使用 bisect_left 查找插入位置。如果列表中存在与要插入的元素相等的元素，返回左边的位置
pos_left = bisect.bisect_left(arr, 5)
print(pos_left)  # 输出: 3，应该插入到 4 和 7 之间

# 使用 bisect_right 查找插入位置。如果列表中存在与要插入的元素相等的元素，返回右边的位置。
pos_right = bisect.bisect_right(arr, 5)
print(pos_right)  # 输出: 3，结果与 bisect_left 一致

# 使用 insort_left 插入元素，插入位置是所有x的等值元素的左侧
bisect.insort_left(arr, 5)
print(arr)  # 输出: [1, 3, 4, 5, 7, 8]

# 使用 insort_right 插入元素
bisect.insort_right(arr, 6)
print(arr)  # 输出: [1, 3, 4, 5, 6, 7, 8]


# 利用bisect寻找lower_bound
# 二分方法把有序数组分成两个区间，< tar 以及 >= tar
# lower_bound 是 >= tar的第一个数
arr = [2, 5, 8]
tar = 4
lower_bound_idx = bisect.bisect_left(arr, 4)
lower_bound = arr[lower_bound_idx]
print(lower_bound)