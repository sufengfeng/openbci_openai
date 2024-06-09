def ask_question(question, responses):
    print(question)
    for i, response in enumerate(responses):
        print(f"{i + 1}. {response}")
    answer_index = input("请输入你的选择(输入'q'退出)：")
    if answer_index.isdigit():
        answer_index = int(answer_index) - 1
        if 0 <= answer_index < len(responses):
            return responses[answer_index]
        else:
            print("选择错误，请重新输入。")
    elif answer_index.lower() == 'q':
        return "退出"
    else:
        print("无效输入，请重新输入。")


# 使用示例
questions = {
    "你喜欢夏天的水果吗?": [
        "苹果",
        "香蕉",
        "无",
    ],
    "你喜欢的电视剧是哪一部?": [
        "黑镜",
        "游星",
        "无",
    ],
}

while True:
    for question, responses in questions.items():
        answer = ask_question(question, responses)
        if answer == "退出":
            break
        print(f"你选择了: {answer}")
    else:
        continue
    break