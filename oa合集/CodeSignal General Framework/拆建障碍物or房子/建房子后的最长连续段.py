## 恺
def solution(queries):
    length_map = {}
    max_value = 0
    res = []

    for query in queries:
        if query in length_map:
            continue  # 跳过已存在的位置

        # 获取左边和右边的区间长度（如果存在）
        left_length = length_map.get(query - 1, 0)
        right_length = length_map.get(query + 1, 0)

        # 计算当前区间的总长度
        current_length = left_length + right_length + 1

        # 更新当前位置和区间边界的长度
        length_map[query] = current_length
        length_map[query - left_length] = current_length
        length_map[query + right_length] = current_length

        # 更新最长连续区间长度
        max_value = max(max_value, current_length)

        # 将当前最大值加入结果
        res.append(max_value)

    return res

# 示例用法
queries = [2, 1, 3]
print(solution(queries))  # 输出: [1, 2, 3]





import heapq

def solution(queries):
    houses = set()
    max_heap = []
    max_len = 0
    
    result = []

    for query in queries:
        if query in houses:
            result.append(max_len)
            continue
        
        houses.add(query)
        
        left_len = 0  # Length of segment to the left
        right_len = 0  # Length of segment to the right

        # Check left neighbor
        if query - 1 in houses:
            # Find the left segment length
            left = query - 1
            while left in houses:
                left -= 1
            left_len = query - (left + 1)

        # Check right neighbor
        if query + 1 in houses:
            # Find the right segment length
            right = query + 1
            while right in houses:
                right += 1
            right_len = (right - 1) - query
        
        # Merge segments if needed
        new_length = 1 + left_len + right_len
        max_len = max(max_len, new_length)

        # Push the new segment length to the heap
        heapq.heappush(max_heap, -new_length)

        # Add the current max length to result
        result.append(max_len)
    
    return result

# Example usage
queries = [2, 1, 3]
print(solution(queries))  # Output: [1, 2, 3]






## sortedList实现
from sortedcontainers import SortedList

def solution(queries):
    houses = set()
    segments = SortedList()
    max_len = 0
    
    # Store the start and end of segments in a dictionary
    start_to_end = {}
    end_to_start = {}
    
    result = []

    for query in queries:
        if query in houses:
            continue

        houses.add(query)
        left_has_house = (query - 1 in houses)
        right_has_house = (query + 1 in houses)

        # Case 1: The new house is an isolated point, it creates a new segment
        if not left_has_house and not right_has_house:
            start_to_end[query] = query
            end_to_start[query] = query
            segments.add(1)
            max_len = max(max_len, 1)
        
        # Case 2: The new house merges with a left segment
        elif left_has_house and not right_has_house:
            start = end_to_start[query - 1]
            segments.remove(query - start)
            end_to_start.pop(query - 1)

            end_to_start[query] = start
            start_to_end[start] = query
            segments.add(query - start + 1)
            max_len = max(max_len, query - start + 1)
        
        # Case 3: The new house merges with a right segment
        elif right_has_house and not left_has_house:
            end = start_to_end[query + 1]
            segments.remove(end - (query + 1) + 1)
            start_to_end.pop(query + 1)

            start_to_end[query] = end
            end_to_start[end] = query
            segments.add(end - query + 1)
            max_len = max(max_len, end - query + 1)

        # Case 4: The new house merges two segments into one
        elif left_has_house and right_has_house:
            start = end_to_start[query - 1]
            end = start_to_end[query + 1]
            segments.remove(query - start)
            segments.remove(end - (query + 1) + 1)
            end_to_start.pop(query - 1)
            start_to_end.pop(query + 1)

            start_to_end[start] = end
            end_to_start[end] = start
            segments.add(end - start + 1)
            max_len = max(max_len, end - start + 1)
        
        result.append(max_len)
    
    return result


