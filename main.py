# 接收输入的字符串
text = input("请输入字符串：")
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
# 按频率降序打印字符
print("按字符出现频率降序排列：")
for char, freq in char_freq_list:
    print(f"字符 '{char}'，出现频率：{freq}")
