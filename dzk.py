import pygame

# 初始化 pygame
pygame.init()

# 定义游戏窗口大小
screen_width = 480
screen_height = 600

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏窗口标题
pygame.display.set_caption("打砖块游戏")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)

# 定义砖块的大小和数量
brick_width = 50
brick_height = 20
brick_rows = 5
brick_cols = 10

# 定义球的大小和速度
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5

# 定义 paddle 的大小和速度
paddle_width = 100
paddle_height = 10
paddle_speed = 5

# 定义砖块列表
bricks = []

# 初始化砖块
for row in range(brick_rows):
    brick_row = []
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_row.append(brick)
    bricks.append(brick_row)

# 定义球
ball = pygame.Rect(screen_width // 2 - ball_radius, screen_height - paddle_height - ball_radius * 2, ball_radius * 2, ball_radius * 2)

# 定义 paddle
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height, paddle_width, paddle_height)

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动 paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # 移动球
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 处理球与边界的碰撞
    if ball.left < 0 or ball.right > screen_width:
        ball_speed_x = -ball_speed_x
    if ball.top < 0:
        ball_speed_y = -ball_speed_y

    # 处理球与砖块的碰撞
    for row in range(brick_rows):
        for col in range(brick_cols):
            brick = bricks[row][col]
            if brick.colliderect(ball):
                bricks[row][col] = None
                ball_speed_y = -ball_speed_y

    # 处理球与 paddle 的碰撞
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    # 绘制背景
    screen.fill(black)

    # 绘制砖块
    for row in range(brick_rows):
        for col in range(brick_cols):
            brick = bricks[row][col]
            if brick:
                pygame.draw.rect(screen, white, brick)

    # 绘制球
    pygame.draw.circle(screen, white, (ball.x + ball_radius, ball.y + ball_radius), ball_radius)

    # 绘制 paddle
    pygame.draw.rect(screen, white, paddle)

    # 刷新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()