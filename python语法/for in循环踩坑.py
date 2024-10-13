# for in 循环 
wordLists = ['abc', 'abel22', 'Hello', 'Data']
for w in wordLists:
    w = w.upper()
    print(w)
print(wordLists)
# 在 for 循环中，w 是一个临时变量，它从 wordLists 中取出每个字符串。
# 当执行 w = w.upper() 时，这只是将 w 的值更改为大写版本，而不会影响到 wordLists 中的元素。

for i in range(len(wordLists)):
    wordLists[i] = wordLists[i].upper()
    print(wordLists[i])
print(wordLists)

# 按照第一、第二排序，不用lamda的排序
# 字典按照val 排序