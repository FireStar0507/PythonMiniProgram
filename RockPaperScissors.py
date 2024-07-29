import random

def rock_paper_scissors():
    # 定义可能的选择
    choices = ["r", "p", "s"]
    # 玩家选择
    player_choice = input("请选择你的手势（r/石头，p/剪刀，s/布）：")
    # 电脑选择
    computer_choice = random.choice(choices)
    # 输出双方的选择
    print("你选择了：", player_choice)
    print("电脑选择了：", computer_choice)
    # 判断胜负
    if (player_choice == "r" and computer_choice == "p") or (player_choice == "p" and computer_choice == "s") or (player_choice == "s" and computer_choice == "r"):
        print("你赢了！")
    elif player_choice == computer_choice:
        print("平局！")
    else:
        print("你输了！")

if __name__ == "__main__":
    rock_paper_scissors()
if __name__ == "__main__":
    input("游戏结束，按回车键退出...")
