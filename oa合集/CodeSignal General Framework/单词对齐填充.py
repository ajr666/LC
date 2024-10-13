def solution(paragraphs, aligns, width):
    result = ["*" * width]  # 添加顶部边界线

    for words, align in zip(paragraphs, aligns):
        line = []
        current_line = ""

        # 将单词填充到当前行
        for word in words:
            if len(current_line) + len(word) + (1 if current_line else 0) <= width:
                # 如果加上当前单词后不超过宽度
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
            else:
                # 当前行已满，存储并重置
                line.append(current_line)
                current_line = word

        # 添加最后一行
        if current_line:
            line.append(current_line)

        # 对每一行进行对齐
        for l in line:
            if align == "LEFT":
                result.append(l.ljust(width))
            elif align == "RIGHT":
                result.append(l.rjust(width))

    result.append("*" * width)  # 添加底部边界线
    return result

# 示例输入
paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and align", "to right"]]
aligns = ["LEFT", "RIGHT", "RIGHT"]
width = 16

# 调用函数并输出结果
output = solution(paragraphs, aligns, width)
for line in output:
    print(line)