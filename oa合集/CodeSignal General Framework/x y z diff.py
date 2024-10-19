def solution(queries, diff):
    from collections import defaultdict
    
    # Initialize dictionaries
    cnt = defaultdict(int)  # Counts of each number.
    pairs = defaultdict(int)  # Pairs where y - z = diff.
    triples = 0  # Total count of valid triples.
    
    # Result array
    res = []
    
    # Process each query
    for q in queries:
        op, x = q[0], int(q[1:])
        
        if op == '+':
            # Adding `x`
            # For every y such that `y - x = diff`, `pairs[(y, x)]` increases.
            triples += pairs[x - diff]
            
            # Update pairs for future triples.
            pairs[x] += cnt[x - diff]

            # Increase the count of `x`.
            cnt[x] += 1

        elif op == '-':
            # Only update if `x` is present.
            if cnt[x] > 0:
                # Decrease the count of valid triples as `x` is removed.
                triples -= pairs[x - diff]

                # Update pairs as `x` is removed.
                pairs[x] -= cnt[x - diff]

                # Decrease the count of `x`.
                cnt[x] -= 1

        # Store the current count of valid triples.
        res.append(triples)
    
    return res

print(solution(["+1", "+2", "+3", "+1", "-2", "+4"], 1))