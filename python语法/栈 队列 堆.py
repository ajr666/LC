## 栈 使用list模拟
st = []
st.append(1)
st.pop()

if st: # 非空为true
    st[-1] = 5 # 栈顶


## 队列
from collections import deque

queue = deque()
queue.append(10) # 入队（在队尾添加元素）
queue.append(20)
queue.append(30)

first_item = queue.popleft()  # 返回 10
print(first_item)  # 输出：10

print(queue)  # 输出：deque([20, 30])


# 堆
import heapq

heap = [] # 创建一个空的堆

heapq.heappush(heap, 10) # 将元素推入堆中
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

min_element = heapq.heappop(heap) # 弹出最小的元素
print(min_element)  # 输出 1

print(heap)  # 查看当前堆 输出 [5, 10]

a = heap[0] # 访问堆顶元素

nums = [3, 7, 1, 4] # 批量转换为堆
heapq.heapify(nums)
print(nums)  # 输出 [1, 4, 3, 7]，变成了堆结构
# heapq 默认是最小堆，即堆顶（第一个元素）是最小值。如果需要实现最大堆，可以在插入时将所有值取反，间接实现