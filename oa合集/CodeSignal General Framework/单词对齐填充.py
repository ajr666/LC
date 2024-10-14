def solution(paragraphs, aligns, width):
    # Store the final result with borders.
    result = []

    # Add the top border.
    border = "*" * (width + 2)
    result.append(border)

    # Process each paragraph.
    for i in range(len(paragraphs)):
        words = paragraphs[i]
        align = aligns[i]
        current_line = ""
        lines = []

        # Construct lines within the width limit.
        for word in words:
            if len(current_line) + len(word) + (1 if current_line else 0) <= width:
                # Add a space if it's not the start of the line.
                if current_line:
                    current_line += " "
                current_line += word
            else:
                # If the word can't fit in the current line, add the current line to lines.
                lines.append(current_line)
                current_line = word

        # Add the last line if it exists.
        if current_line:
            lines.append(current_line)

        # Align each line and add to result.
        for line in lines:
            if align == "LEFT":
                # Add trailing spaces for left alignment.
                aligned_line = line.ljust(width)
            elif align == "RIGHT":
                # Add leading spaces for right alignment.
                aligned_line = line.rjust(width)
            result.append(f"*{aligned_line}*")
    
    # Add the bottom border.
    result.append(border)
    
    return result
    
# 示例输入
paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and align", "to right"]]
aligns = ["LEFT", "RIGHT", "RIGHT"]
width = 16

# 调用函数并输出结果
output = solution(paragraphs, aligns, width)
for line in output:
    print(line)
