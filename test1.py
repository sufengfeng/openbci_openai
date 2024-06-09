
# 定义一个字典，包含问题和答案的键值对
qa_pairs = {
    "你好吗？": "我很好，谢谢！",
    "今天天气怎么样？": "今天天气晴朗。",
    "Python是什么？": "Python是一种广泛使用的高级编程语言。"
}


# 定义一个函数，用于搜索问题并返回对应的答案
def get_answer(question):
    # 遍历字典中的每个问题
    for q in qa_pairs:
        # 检查输入的问题是否与字典中的问题匹配
        if question.strip() == q:
            # 如果匹配，返回对应的答案
            return qa_pairs[q]
    # 如果没有找到匹配的问题，返回一个默认回答
    return "对不起，我不知道答案。"


# 测试函数
questions_to_ask = ["你好吗？", "Python是什么？", "什么是AI？"]

for q in questions_to_ask:
    answer = get_answer(q)
    print(f"问题: {q}")
    print(f"答案: {answer}")
    print()
