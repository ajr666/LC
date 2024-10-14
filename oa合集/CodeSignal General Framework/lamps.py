def solution(lamps):
    cnt = dict()
    
    for lamp in lamps:
        for idx in range(lamp[0] - lamp[1], lamp[0] + lamp[1] + 1):
            if idx not in cnt:
                cnt[idx] = 1
            else:
                cnt[idx] += 1
    
    ans = 0
    for item in cnt.items():
        if item[1] == 1:
            ans += 1
            
    print(ans)
    
lamps = [[3, 1], [7, 2], [5, 1]]
solution(lamps)


# O(NlogN)方法：扫描线方法
def solution(lamps):
    events = []

    # Step 1: Generate events for each lamp's start and end points
    for position, radius in lamps:
        start = position - radius
        end = position + radius
        events.append((start, +1))
        events.append((end + 1, -1))
    
    # Step 2: Sort events by position
    events.sort()

    # Step 3: Traverse through events to count ranges with exactly 1 illumination
    current_illumination = 0
    last_position = None
    result = 0

    for position, change in events:
        if last_position is not None and current_illumination == 1:
            result += position - last_position

        current_illumination += change
        last_position = position

    return result
