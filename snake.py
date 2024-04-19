import pygame
import random

# 初始化Pygame
pygame.init()

# 設置遊戲視窗尺寸
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("貪吃蛇")

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 定義貪吃蛇和食物
snake_block = 10
snake_speed = 8
font_style = pygame.font.SysFont(None, 50)

# 定義貪吃蛇初始位置
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], snake_block, snake_block])

# 顯示分數
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    win.blit(value, [0, 0])

# 遊戲主函數
def gameLoop():
    game_over = False
    game_close = False

    # 貪吃蛇初始位置
    x1 = width / 2
    y1 = height / 2

    # 貪吃蛇初始速度
    x1_change = 0
    y1_change = 0

    # 貪吃蛇身體
    snake_List = []
    Length_of_snake = 1

    # 食物位置
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            win.fill(white)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, black)
            win.blit(message, [width / 6, height / 3])
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # 判斷是否出界
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(white)
        pygame.draw.rect(win, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 貪吃蛇碰到自己
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        # 貪吃蛇吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.display.update()

        # 控制遊戲速度
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
