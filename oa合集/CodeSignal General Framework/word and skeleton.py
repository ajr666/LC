def solution(word, skeletons):  
    ans = []
    
    for skeleton in skeletons:
        if len(word) == len(skeleton):
            sk_st = set()
            for c in skeleton:
                if c != '-' and c not in sk_st:
                     sk_st.add(c)
            
            flag = True
            for c in word:
                if c not in sk_st:
                    flag = False
                    break
            
            if flag:
                ans.append(skeleton)
                
    print(ans)
    
    
word = "hello"
skeletons = ["he-lo", "he--o", "--ell-", "hello"]
solution(word, skeletons)