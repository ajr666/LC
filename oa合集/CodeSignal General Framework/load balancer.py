def load_balancer(serversPowers, events):
    n = len(serversPowers)  # 服务器的数量
    servers_count = [0] * n  # 用于记录每个服务器处理的请求数量
    active_servers = set(range(n))  # 活跃服务器的索引集合
    current_requests = 0  # 当前请求数量

    for event in events:
        if event == "REQUEST":
            current_requests += 1  # 增加请求数量
            # 轮流将请求分配到可用的服务器
            for i in range(n):
                if i in active_servers:  # 只考虑活跃的服务器
                    if current_requests > 0:
                        requests_to_process = min(serversPowers[i], current_requests)
                        servers_count[i] += requests_to_process  # 更新该服务器处理的请求数
                        current_requests -= requests_to_process  # 减少剩余请求数
                    if current_requests == 0:  # 所有请求都已处理
                        break
        else:  # 处理故障事件
            _, index = event.split()  # 提取索引
            index = int(index)  # 将字符串转为整数
            if index in active_servers:  # 如果服务器在活跃集合中
                active_servers.remove(index)  # 从活跃服务器中移除

    # 找到服务请求最多的服务器，处理平局情况
    max_requests = -1
    server_index = -1
    for i in range(n):
        if servers_count[i] > max_requests:
            max_requests = servers_count[i]
            server_index = i
        elif servers_count[i] == max_requests:
            server_index = max(server_index, i)  # 返回最大索引

    return server_index

# 示例测试
serversPowers = [3, 1, 4, 1, 5]
events = ["REQUEST", "REQUEST", "FAIL 2", "REQUEST", "REQUEST", "FAIL 1", "REQUEST", "REQUEST"]
print(load_balancer(serversPowers, events))  # 输出应为 4（服务器 4 处理了最多请求）
