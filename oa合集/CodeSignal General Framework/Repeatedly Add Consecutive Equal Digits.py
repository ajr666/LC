def solution(number: str) -> str:
    num = [int(d) for d in list(number)]
    print(num)
    
    while True:
        hasChange = False
        t = []
        i = 0

        while i < len(num):
            j = i + 1
            while j < len(num) and num[j] == num[i]:
                j += 1

            if i + 1 < j:
                hasChange = True
                s = (j - i) * int(num[i])
                for d in str(s):
                    t.append(d)
            else:
                t.append(num[i])
            i = j

        new_num = ''.join([str(d) for d in t])

        if not hasChange:
            break

        num = new_num

    return "".join([str(d) for d in num])

print(solution("999433"))
print(solution("44488366664"))
print(solution("66644319333"))
print(solution("0044886"))