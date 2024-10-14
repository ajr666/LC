def build_and_check(operations):
    obstacles = set()  # 用来存储障碍物的位置
    result = []

    for operation in operations:
        if operation[0] == 1:
            # 操作类型 1: 在位置 x 添加障碍物
            x = operation[1]
            obstacles.add(x)
        
        elif operation[0] == 2:
            # 操作类型 2: 检查是否可以放置大小为 size 的区块从位置 x 开始
            x, size = operation[1], operation[2]
            can_place = True

            # 检查从 x 到 x + size - 1 的位置是否有障碍物
            for i in range(x, x + size):
                if i in obstacles:
                    can_place = False
                    break
            
            # 根据检查结果添加 '1' 或 '0' 到结果中
            if can_place:
                result.append('1')
            else:
                result.append('0')
    
    # 将结果列表转换为字符串并返回
    return ''.join(result)

# 示例测试
operations = [[1, 2], [2, 1, 3], [2, 2, 2], [1, 4], [2, 3, 2]]
print(build_and_check(operations))  # 输出: "000"



# SortedList实现
from sortedcontainers import SortedList
def build_and_check(operations):
    obstacles = SortedList()  # 用来存储障碍物的位置
    result = []

    for operation in operations:
        if operation[0] == 1:
            # 操作类型 1: 在位置 x 添加障碍物
            x = operation[1]
            obstacles.add(x)
        
        elif operation[0] == 2:
            # 操作类型 2: 检查是否可以放置大小为 size 的区块从位置 x 开始
            x, size = operation[1], operation[2]
            can_place = True

            # 找到第一个大于等于 x 的障碍物的位置
            idx = obstacles.bisect_left(x)

            # 检查障碍物是否在区间 [x, x + size - 1] 内
            if idx < len(obstacles) and obstacles[idx] < x + size:
                can_place = False

            # 根据检查结果添加 '1' 或 '0' 到结果中
            result.append('1' if can_place else '0')
    
    # 将结果列表转换为字符串并返回
    return ''.join(result)

# 示例测试
operations = [[1, 2], [2, 1, 3], [2, 2, 2], [1, 4], [2, 3, 2]]
print(build_and_check(operations))  # 输出: "000"