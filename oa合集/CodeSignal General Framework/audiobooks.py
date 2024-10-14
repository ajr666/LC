def solution(audiobooks, logs):
    finish = set()
    
    idx = 0
    
    for log in logs:
        if log[0] == 'L':
            ts = log[7:]
            t = int(ts)
            
            print("listen", t)
            
            while idx in finish:
                idx = (idx + 1) % len(audiobooks)
                
            audiobooks[idx] -= t
            if audiobooks[idx] == 0:
                finish.add(idx)
            
            # idx = (idx + 1) % len(audiobooks)
            
        else:
            drop_idx_s = log[5:]
            drop_idx = int(drop_idx_s)
            print("drop", drop_idx)
            finish.add(drop_idx)
            
        print(audiobooks)
        print(finish)
            
    print(audiobooks)


audiobooks = [60, 120, 90]
logs = ["LISTEN 30", "LISTEN 30", "DROP 1", "LISTEN 60"]
solution(audiobooks, logs)

audiobooks = [60, 50, 70]
logs = ["LISTEN 30", "LISTEN 20", "LISTEN 10", "LISTEN 20"]
solution(audiobooks, logs)
