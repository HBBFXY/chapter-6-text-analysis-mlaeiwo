def analyze_text(text):
    # 用于统计字符频率的字典
    char_freq = {}
    # 遍历字符串，统计每个字符的频率
    for char in text:
        # 如果字符已经在字典中，频率加1
        if char in char_freq:
            char_freq[char] += 1
        # 如果字符不在字典中，初始化频率为1
        else:
            char_freq[char] = 1
    # 将字典转换为包含(字符, 频率)的元组列表
    char_freq_list = list(char_freq.items())
    # 按照频率降序排序
    char_freq_list.sort(key=lambda x: x[1], reverse=True)
    # 提取排序后的字符，组成列表
    sorted_chars = [char for char, freq in char_freq_list]
    return sorted_chars

# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("====================")
    print("请输入一段文本（输入空行结束）：")

    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break

    # 合并输入文本
    text = "\n".join(lines)

    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)

        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))

        # 提示用户比较不同语言
        print("\n提示：尝试输入中英文文章片段，比较不同语言之间字符频率的差别")

