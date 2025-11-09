def analyze_text(text):
    # 用于统计字符频率的字典
    char_frequency = {}
    # 遍历字符串中的每个字符
    for char in text:
        # 如果字符是字母（排除数字、标点等）
        if char.isalpha():
            # 转为小写（统一大小写，比如'A'和'a'视为同一个字母）
            lower_char = char.lower()
            # 统计频率
            char_frequency[lower_char] = char_frequency.get(lower_char, 0) + 1
    # 将字典转换为列表，并按频率降序排序
    sorted_chars = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars

# 测试
text = input("请输入一段文本：")
result = analyze_text(text)
print("按字符出现频率降序排列：")
for char, freq in result:
    print(f"字符 '{char}'，出现频率：{freq}")
