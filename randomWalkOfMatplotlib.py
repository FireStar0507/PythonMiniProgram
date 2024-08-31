import numpy as np
import matplotlib.pyplot as plt
import random
import os

def generate_random_walk_plot(num_steps, output_path):
    step = (1, 10)
    steptime = (2, 6)
    waitime = (2, 6)

    # 设置起点坐标
    current_x, current_y = 50, 50
    x = [current_x]
    y = [current_y]
    colors = []

    for step_num in range(num_steps):
        # 随机选择方向
        direction = random.choice(['up', 'down', 'left', 'right'])

        # 随机游走距离
        distance = random.randint(*step)

        if direction == 'up':
            new_y = current_y - distance
            if new_y < 0:
                new_y = 100 + new_y
            y.append(new_y)
            x.append(current_x)
        elif direction == 'down':
            new_y = current_y + distance
            if new_y >= 100:
                new_y = new_y - 100
            y.append(new_y)
            x.append(current_x)
        elif direction == 'left':
            new_x = current_x - distance
            if new_x < 0:
                new_x = 100 + new_x
            y.append(current_y)
            x.append(new_x)
        elif direction == 'right':
            new_x = current_x + distance
            if new_x >= 100:
                new_x = new_x - 100
            y.append(current_y)
            x.append(new_x)

        # 生成颜色（这里简单使用线性渐变，从蓝色到红色）
        color = (step_num / num_steps, 0, 1 - step_num / num_steps)
        colors.append(color)

    # 设置图形
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # 绘制起点和终点（更粗的点）
    ax.plot(x[0], y[0], 'bo', markersize=8)
    ax.plot(x[-1], y[-1], 'ro', markersize=8)

    # 绘制轨迹
    for i in range(len(x) - 1):
        ax.plot(x[i:i + 2], y[i:i + 2], color=colors[i])

    # 保存图片
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    num_steps = int(input("请输入游走次数："))
    output_directory = "output_images"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_path = os.path.join(output_directory, f"random_walk_{num_steps}_steps.png")
    generate_random_walk_plot(num_steps, output_path)
    print(f"图片已保存到：{output_path}")
